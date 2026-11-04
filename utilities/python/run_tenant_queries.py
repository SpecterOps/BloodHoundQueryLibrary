r"""Run every query in the library against a BloodHound tenant, one at a time.

Credentials are read from the repository's .env file. The file may use either
KEY=value entries or BloodHound's defautlt output format: ``Key: value`` / ``ID: value``

Run with:
.\.venv\Scripts\python.exe utilities\python\run_tenant_queries.py --tenant https://localhost:8080 --show-http-200
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
from pathlib import Path
import sys
from datetime import datetime
from collections import Counter
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
ENDPOINT = "/api/v2/graphs/cypher"


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.is_file():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        separators = [position for position in (line.find("="), line.find(":")) if position >= 0]
        if not separators:
            continue
        position = min(separators)
        name, value = line[:position], line[position + 1:]
        values[name.strip().lower()] = value.strip().strip("\"'")
    return values


def credentials() -> tuple[str, str]:
    env = load_env(REPOSITORY_ROOT / ".env")
    key = os.environ.get("BH_API_KEY") or env.get("key") or env.get("bh_api_key")
    token_id = os.environ.get("BH_API_ID") or env.get("id") or env.get("bh_api_id")
    if not key or not token_id:
        raise ValueError(".env must contain Key: <API key> and ID: <API key ID> (or set BH_API_KEY and BH_API_ID).")
    return token_id, key


def signed_request(url: str, token_id: str, token_key: str, body: bytes, timeout: int):
    request_date = datetime.now().astimezone().isoformat("T")
    digester = hmac.new(token_key.encode(), ("POST" + ENDPOINT).encode(), hashlib.sha256)
    digester = hmac.new(digester.digest(), request_date[:13].encode(), hashlib.sha256)
    digester = hmac.new(digester.digest(), body, hashlib.sha256)
    request = Request(
        url.rstrip("/") + ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": f"bhesignature {token_id}",
            "RequestDate": request_date,
            "Signature": base64.b64encode(digester.digest()).decode(),
            "Content-Type": "application/json",
            "User-Agent": "BloodHoundQueryLibrary tenant query runner",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8", errors="replace")
    except HTTPError as error:
        return error.code, error.read().decode("utf-8", errors="replace")
    except URLError as error:
        raise RuntimeError(f"Request failed: {error.reason}") from error


def is_api_error(status: int, payload: object) -> bool:
    if not 200 <= status < 300:
        return True
    if isinstance(payload, dict):
        if payload.get("errors"):
            return True
        status_value = str(payload.get("status", "")).lower()
        if status_value in {"error", "failed"}:
            return True
    return False


def result_count(payload: object) -> int | None:
    if not isinstance(payload, dict):
        return None
    data = payload.get("data")
    if isinstance(data, dict):
        graph_keys = ("nodes", "edges", "literals")
        if any(key in data for key in graph_keys):
            return sum(
                len(data[key])
                for key in graph_keys
                if isinstance(data.get(key), (dict, list))
            )
        for key in ("nodes", "rows", "results"):
            value = data.get(key)
            if isinstance(value, (dict, list)):
                return len(value)
    if isinstance(data, list):
        return len(data)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tenant", required=True, help="BloodHound tenant base URL, for example https://tenant.example.com")
    parser.add_argument("--queries", type=Path, default=REPOSITORY_ROOT / "queries")
    parser.add_argument("--timeout", type=int, default=1800, help="Per-query HTTP timeout in seconds (default: 1800).")
    parser.add_argument(
        "--show-http-200",
        action="store_true",
        help="Print each successful HTTP 200 response and its result content.",
    )
    args = parser.parse_args()

    try:
        token_id, token_key = credentials()
    except ValueError as error:
        parser.error(str(error))

    files = sorted(args.queries.rglob("*.yml"))
    if not files:
        print(f"No query YAML files found in {args.queries}", file=sys.stderr)
        return 2

    failures = 0
    empty_results = 0
    http_status_counts: Counter[int] = Counter()
    print(f"Running {len(files)} queries against {args.tenant} sequentially (timeout {args.timeout}s each).")
    for index, path in enumerate(files, 1):
        try:
            query_doc = yaml.safe_load(path.read_text(encoding="utf-8"))
            name = query_doc["name"]
            query = query_doc["query"]
            body = json.dumps({"query": query, "include_properties": False}).encode("utf-8")
            status, response_text = signed_request(args.tenant, token_id, token_key, body, args.timeout)
            http_status_counts[status] += 1
            try:
                payload = json.loads(response_text)
            except json.JSONDecodeError:
                payload = {"response": response_text}
            count = result_count(payload)
            state = "FAIL" if is_api_error(status, payload) else "PASS"
            if state == "FAIL":
                failures += 1
            elif count == 0:
                empty_results += 1
                state = "INFO"
            if status != 200 or args.show_http_200:
                print(f"\n[{index}/{len(files)}] {state} {name} ({path.name}) HTTP {status}")
                if count is not None:
                    print(f"Result items: {count}" + (" (no results; this may reflect tenant data or query conditions)" if count == 0 else ""))
                print(json.dumps(payload, indent=2, ensure_ascii=False))
        except Exception as error:  # Keep processing subsequent queries.
            failures += 1
            print(f"\n[{index}/{len(files)}] FAIL {path.name}: {type(error).__name__}: {error}")

    print(
        f"\nCompleted: {len(files) - failures} passed/informational, {failures} failed, "
        f"{empty_results} with no results."
    )
    if http_status_counts:
        print("HTTP status counts:")
        for status, count in sorted(http_status_counts.items()):
            print(f"  HTTP {status}: {count}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
