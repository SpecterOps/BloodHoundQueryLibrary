"""Audit Query Library prebuilt queries against the BloodHound product catalog.

Usage:
    python utilities/python/compare_prebuilt.py <path-to-BloodHound>

The read-only audit combines CommonSearches from commonSearchesAGI.ts and
commonSearchesAGT.ts. A Query Library entry is synchronized when its Cypher
matches either valid product implementation. UncommonSearches is excluded.

Queries are matched by platform, category, and the YAML name field, never by
filename. Terminal (AD) and (AZ) suffixes are normalized only for a query's
sole matching platform. Multi-platform library queries can match the
corresponding BloodHound platform.

Intentional TypeScript representations for attack-path edge sets, AGI system
tags, AGT labels, and the privileged-role regular expression are resolved
before comparison. Other Cypher differences are preserved and emitted as
unified diffs. The report also identifies product-only queries, library-only
prebuilt queries, ambiguous identities, and malformed catalog structures.

The command requires PyYAML but not the repository's Pydantic test
dependencies. Install it, if needed, with:
    python -m pip install PyYAML

Run the audit-specific tests without loading the repository-wide Jinja2 report
fixture:
    python -m pytest --noconftest tests/test_compare_prebuilt.py

Exit codes:
    0  Catalogs are synchronized.
    1  Query content or inventory drift was detected.
    2  A path, dependency, or catalog structure is invalid.

Neither repository is modified. Reconcile findings in the intended source and
increment a Query Library revision when its YAML changes.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
import difflib
from pathlib import Path
import re
import sys

try:
    import yaml
except ModuleNotFoundError:
    yaml = None


CATALOG_RELATIVE_PATH = Path("packages/javascript/bh-shared-ui/src")
DEFAULT_QUERY_DIRECTORY = Path(__file__).resolve().parents[2] / "queries"
VARIANTS = ("AGI", "AGT")
PLATFORM_SUFFIXES = {
    "Active Directory": "AD",
    "Azure": "AZ",
}

CLI_EPILOG = """matching:
  Product queries are read from both AGI and AGT CommonSearches catalogs.
  Library queries are matched by platform, category, and YAML name. A body may
  match either product variant. The audit never modifies either repository.

exit codes:
  0  synchronized
  1  content or inventory drift
  2  invalid path, dependency, or catalog structure
"""

class AuditError(Exception):
    """Base error for invalid audit inputs."""


class CatalogParseError(AuditError):
    """Raised when a BloodHound TypeScript catalog cannot be parsed safely."""


@dataclass(frozen=True, order=True)
class QueryIdentity:
    platform: str
    category: str
    name: str

    def display(self) -> str:
        return f"{self.platform} / {self.category} / {self.name}"


@dataclass(frozen=True)
class ProductQuery:
    identity: QueryIdentity
    query: str
    variant: str


@dataclass(frozen=True)
class LibraryQuery:
    path: Path
    name: str
    platforms: tuple[str, ...]
    category: str
    query: str

    def display_name(self) -> str:
        if len(self.platforms) != 1:
            return self.name

        suffix = PLATFORM_SUFFIXES.get(self.platforms[0])
        if suffix is None:
            return self.name

        terminal_suffix = f" ({suffix})"
        if self.name.endswith(terminal_suffix):
            return self.name[: -len(terminal_suffix)]
        return self.name

    def identities(self) -> tuple[QueryIdentity, ...]:
        return tuple(
            QueryIdentity(platform, self.category, self.display_name())
            for platform in self.platforms
        )


@dataclass(frozen=True)
class QueryComparison:
    identity: QueryIdentity
    library_query: LibraryQuery
    product_queries: tuple[ProductQuery, ...]
    matching_variants: tuple[str, ...]

    @property
    def matches(self) -> bool:
        return bool(self.matching_variants)

    @property
    def implementation_status(self) -> str:
        if len(self.product_queries) == 1:
            return f"{self.product_queries[0].variant} only"
        if len({query.query for query in self.product_queries}) == 1:
            return "identical AGI/AGT"
        return "distinct AGI/AGT"


@dataclass(frozen=True)
class AmbiguousMatch:
    identity: QueryIdentity
    library_queries: tuple[LibraryQuery, ...]


@dataclass(frozen=True)
class AuditResult:
    product_identity_count: int
    library_query_count: int
    comparisons: tuple[QueryComparison, ...]
    bloodhound_only: tuple[QueryIdentity, ...]
    library_only: tuple[LibraryQuery, ...]
    ambiguous: tuple[AmbiguousMatch, ...]

    @property
    def body_match_count(self) -> int:
        return sum(comparison.matches for comparison in self.comparisons)

    @property
    def has_drift(self) -> bool:
        return bool(
            self.bloodhound_only
            or self.library_only
            or self.ambiguous
            or any(not comparison.matches for comparison in self.comparisons)
        )


_CONST_LITERAL_PATTERN = re.compile(
    r"\bconst\s+(?P<name>[A-Za-z_$][\w$]*)\s*=\s*"
    r"'(?P<value>(?:\\.|[^'\\])*)'\s*;",
    re.DOTALL,
)
_COMMON_SEARCHES_PATTERN = re.compile(
    r"export\s+const\s+CommonSearches\s*:\s*CommonSearchType\[\]\s*=\s*\["
)
_SUBHEADER_PATTERN = re.compile(
    r"^\s*subheader:\s*'(?P<value>(?:\\.|[^'\\])*)',\s*$"
)
_CATEGORY_PATTERN = re.compile(
    r"^\s*category:\s*(?P<value>[A-Za-z_$][\w$]*),\s*$"
)
_NAME_PATTERN = re.compile(
    r"^\s*name:\s*'(?P<value>(?:\\.|[^'\\])*)',\s*$"
)
_QUERY_PATTERN = re.compile(
    r"^\s*query:\s*`(?P<value>(?:\\.|[^`\\])*)`,\s*$",
    re.DOTALL,
)
_INTERPOLATION_PATTERN = re.compile(r"\$\{(?P<name>[A-Za-z_$][\w$]*)\}")


def _decode_javascript_string(value: str) -> str:
    decoded: list[str] = []
    index = 0
    escapes = {
        "n": "\n",
        "r": "\r",
        "t": "\t",
        "b": "\b",
        "f": "\f",
        "v": "\v",
        "0": "\0",
        "\\": "\\",
        "'": "'",
        '"': '"',
        "`": "`",
        "$": "$",
    }

    while index < len(value):
        if value[index] != "\\":
            decoded.append(value[index])
            index += 1
            continue

        index += 1
        if index >= len(value):
            raise CatalogParseError("TypeScript string ends with an incomplete escape")

        escape = value[index]
        if escape == "u":
            digits = value[index + 1 : index + 5]
            if len(digits) != 4 or not all(
                character in "0123456789abcdefABCDEF" for character in digits
            ):
                raise CatalogParseError(
                    "TypeScript string contains an invalid Unicode escape"
                )
            decoded.append(chr(int(digits, 16)))
            index += 5
            continue

        if escape == "x":
            digits = value[index + 1 : index + 3]
            if len(digits) != 2 or not all(
                character in "0123456789abcdefABCDEF" for character in digits
            ):
                raise CatalogParseError(
                    "TypeScript string contains an invalid hex escape"
                )
            decoded.append(chr(int(digits, 16)))
            index += 3
            continue

        decoded.append(escapes.get(escape, escape))
        index += 1

    return "".join(decoded)


def _normalize_query(query: str) -> str:
    return query.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")


def _literal_constants(source: str) -> dict[str, str]:
    return {
        match.group("name"): _decode_javascript_string(match.group("value"))
        for match in _CONST_LITERAL_PATTERN.finditer(source)
    }


def _extract_array_body(source: str, opening_bracket: int, path: Path) -> str:
    depth = 0
    quote: str | None = None
    escaped = False
    line_comment = False
    block_comment = False
    body_start = opening_bracket + 1
    index = opening_bracket

    while index < len(source):
        character = source[index]
        next_character = source[index + 1] if index + 1 < len(source) else ""

        if line_comment:
            if character == "\n":
                line_comment = False
            index += 1
            continue

        if block_comment:
            if character == "*" and next_character == "/":
                block_comment = False
                index += 2
            else:
                index += 1
            continue

        if quote is not None:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote:
                quote = None
            index += 1
            continue

        if character == "/" and next_character == "/":
            line_comment = True
            index += 2
            continue
        if character == "/" and next_character == "*":
            block_comment = True
            index += 2
            continue
        if character in ("'", '"', "`"):
            quote = character
            index += 1
            continue
        if character == "[":
            depth += 1
        elif character == "]":
            depth -= 1
            if depth == 0:
                return source[body_start:index]
        index += 1

    raise CatalogParseError(f"Unterminated CommonSearches array in {path}")


def _resolve_interpolations(
    value: str, symbols: dict[str, str], path: Path, line_number: int
) -> str:
    def replace(match: re.Match[str]) -> str:
        name = match.group("name")
        if name not in symbols:
            raise CatalogParseError(
                f"Unsupported interpolation ${{{name}}} in {path}:{line_number}"
            )
        return symbols[name]

    return _INTERPOLATION_PATTERN.sub(replace, value)


def parse_catalog(path: Path, variant: str) -> tuple[ProductQuery, ...]:
    if variant not in VARIANTS:
        raise CatalogParseError(f"Unknown BloodHound catalog variant: {variant}")

    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exception:
        raise CatalogParseError(f"Unable to read {path}: {exception}") from exception

    common_searches = _COMMON_SEARCHES_PATTERN.search(source)
    if common_searches is None:
        raise CatalogParseError(f"CommonSearches array was not found in {path}")

    constants_source = ""
    constants_path = path.with_name("constants.ts")
    if constants_path.exists():
        try:
            constants_source = constants_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exception:
            raise CatalogParseError(
                f"Unable to read {constants_path}: {exception}"
            ) from exception

    symbols = _literal_constants(constants_source)
    symbols.update(_literal_constants(source))
    symbols.update(
        {
            "adTransitEdgeTypes": "AD_ATTACK_PATHS",
            "azureTransitEdgeTypes": "AZ_ATTACK_PATHS",
        }
    )

    opening_bracket = common_searches.end() - 1
    body = _extract_array_body(source, opening_bracket, path)
    first_line = source.count("\n", 0, opening_bracket) + 1

    category: str | None = None
    platform: str | None = None
    pending_name: str | None = None
    queries: list[ProductQuery] = []
    query_lines = 0
    name_lines = 0

    physical_lines = body.splitlines()
    logical_lines: list[tuple[int, str]] = []
    offset = 0
    while offset < len(physical_lines):
        line = physical_lines[offset]
        start_offset = offset + 1
        if re.match(r"^\s*query:\s*", line):
            while _QUERY_PATTERN.match(line) is None:
                offset += 1
                if offset >= len(physical_lines):
                    raise CatalogParseError(
                        f"Unterminated query template in {path}:"
                        f"{first_line + start_offset}"
                    )
                line += "\n" + physical_lines[offset]
        logical_lines.append((start_offset, line))
        offset += 1

    for offset, line in logical_lines:
        line_number = first_line + offset

        if match := _SUBHEADER_PATTERN.match(line):
            category = _decode_javascript_string(match.group("value"))
            platform = None
            continue

        if match := _CATEGORY_PATTERN.match(line):
            category_symbol = match.group("value")
            if category_symbol not in symbols:
                raise CatalogParseError(
                    f"Unknown category constant {category_symbol} in "
                    f"{path}:{line_number}"
                )
            platform = symbols[category_symbol]
            continue

        if re.match(r"^\s*name:\s*", line):
            name_lines += 1
            match = _NAME_PATTERN.match(line)
            if match is None:
                raise CatalogParseError(
                    f"Unsupported query name syntax in {path}:{line_number}"
                )
            if pending_name is not None:
                raise CatalogParseError(
                    f"Query {pending_name!r} has no query body before "
                    f"{path}:{line_number}"
                )
            pending_name = _decode_javascript_string(match.group("value"))
            continue

        if re.match(r"^\s*query:\s*", line):
            query_lines += 1
            match = _QUERY_PATTERN.match(line)
            if match is None:
                raise CatalogParseError(
                    f"Unsupported query template syntax in {path}:{line_number}"
                )
            if pending_name is None or category is None or platform is None:
                raise CatalogParseError(
                    f"Incomplete query metadata in {path}:{line_number}"
                )

            resolved = _resolve_interpolations(
                match.group("value"), symbols, path, line_number
            )
            identity = QueryIdentity(platform, category, pending_name)
            queries.append(
                ProductQuery(
                    identity=identity,
                    query=_normalize_query(_decode_javascript_string(resolved)),
                    variant=variant,
                )
            )
            pending_name = None

    if pending_name is not None:
        raise CatalogParseError(f"Query {pending_name!r} has no query body in {path}")
    if not queries:
        raise CatalogParseError(f"No product queries were parsed from {path}")
    if name_lines != query_lines or query_lines != len(queries):
        raise CatalogParseError(
            f"Parsed {len(queries)} of {name_lines} names and {query_lines} query "
            f"bodies in {path}"
        )

    seen: set[QueryIdentity] = set()
    for query in queries:
        if query.identity in seen:
            raise CatalogParseError(
                f"Duplicate {variant} product identity: {query.identity.display()}"
            )
        seen.add(query.identity)

    return tuple(queries)


def load_product_catalog(
    bloodhound_repository: Path,
) -> dict[QueryIdentity, tuple[ProductQuery, ...]]:
    source_directory = bloodhound_repository / CATALOG_RELATIVE_PATH
    product_queries: dict[QueryIdentity, list[ProductQuery]] = defaultdict(list)

    for variant in VARIANTS:
        path = source_directory / f"commonSearches{variant}.ts"
        for query in parse_catalog(path, variant):
            product_queries[query.identity].append(query)

    return {
        identity: tuple(sorted(queries, key=lambda query: query.variant))
        for identity, queries in product_queries.items()
    }


def load_library_queries(query_directory: Path) -> tuple[LibraryQuery, ...]:
    if not query_directory.is_dir():
        raise AuditError(f"Query directory does not exist: {query_directory}")
    if yaml is None:
        raise AuditError(
            "PyYAML is required to read Query Library files. Install it with "
            "'python -m pip install PyYAML'."
        )

    queries: list[LibraryQuery] = []
    for path in sorted(query_directory.rglob("*.yml")):
        try:
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, yaml.YAMLError) as exception:
            raise AuditError(f"Unable to load {path}: {exception}") from exception

        if not isinstance(value, dict):
            raise AuditError(f"Expected a YAML object in {path}")
        if value.get("prebuilt") is not True:
            continue

        name = value.get("name")
        platforms_value = value.get("platforms")
        category = value.get("category")
        query = value.get("query")

        if not isinstance(name, str) or not name:
            raise AuditError(f"Invalid prebuilt query name in {path}")
        if isinstance(platforms_value, str):
            platforms = (platforms_value,)
        elif isinstance(platforms_value, list) and all(
            isinstance(platform, str) and platform for platform in platforms_value
        ):
            platforms = tuple(platforms_value)
        else:
            raise AuditError(f"Invalid platforms for prebuilt query {path}")
        if not platforms:
            raise AuditError(f"Prebuilt query has no platforms: {path}")
        if not isinstance(category, str) or not category:
            raise AuditError(f"Invalid category for prebuilt query {path}")
        if not isinstance(query, str):
            raise AuditError(f"Invalid Cypher body for prebuilt query {path}")

        queries.append(
            LibraryQuery(
                path=path,
                name=name,
                platforms=platforms,
                category=category,
                query=_normalize_query(query),
            )
        )

    return tuple(queries)


def audit_repositories(
    bloodhound_repository: Path, query_directory: Path = DEFAULT_QUERY_DIRECTORY
) -> AuditResult:
    product_catalog = load_product_catalog(bloodhound_repository)
    library_queries = load_library_queries(query_directory)

    library_by_identity: dict[QueryIdentity, list[LibraryQuery]] = defaultdict(list)
    for library_query in library_queries:
        for identity in library_query.identities():
            library_by_identity[identity].append(library_query)

    comparisons: list[QueryComparison] = []
    bloodhound_only: list[QueryIdentity] = []
    ambiguous: list[AmbiguousMatch] = []
    used_library_paths: set[Path] = set()

    for identity in sorted(product_catalog):
        candidates = library_by_identity.get(identity, [])
        if not candidates:
            bloodhound_only.append(identity)
            continue
        if len(candidates) > 1:
            ambiguous.append(
                AmbiguousMatch(
                    identity,
                    tuple(sorted(candidates, key=lambda item: item.path)),
                )
            )
            used_library_paths.update(candidate.path for candidate in candidates)
            continue

        library_query = candidates[0]
        used_library_paths.add(library_query.path)
        product_queries = product_catalog[identity]
        matching_variants = tuple(
            query.variant
            for query in product_queries
            if query.query == library_query.query
        )
        comparisons.append(
            QueryComparison(
                identity=identity,
                library_query=library_query,
                product_queries=product_queries,
                matching_variants=matching_variants,
            )
        )

    library_only = tuple(
        query for query in library_queries if query.path not in used_library_paths
    )

    return AuditResult(
        product_identity_count=len(product_catalog),
        library_query_count=len(library_queries),
        comparisons=tuple(comparisons),
        bloodhound_only=tuple(bloodhound_only),
        library_only=library_only,
        ambiguous=tuple(ambiguous),
    )


def _render_section(lines: list[str], title: str, values: list[str]) -> None:
    if not values:
        return
    lines.extend(("", title))
    lines.extend(f"  {value}" for value in values)


def render_result(result: AuditResult) -> str:
    lines = [
        "BloodHound product query audit",
        f"Product identities: {result.product_identity_count}",
        f"Query Library prebuilt queries: {result.library_query_count}",
        f"Matching query bodies: {result.body_match_count}",
        "",
        "Product query status:",
    ]

    for comparison in result.comparisons:
        variants = ", ".join(comparison.matching_variants) or "neither"
        lines.append(
            f"  [matches: {variants}] "
            f"[product: {comparison.implementation_status}] "
            f"{comparison.identity.display()} "
            f"({comparison.library_query.path.name})"
        )

    _render_section(
        lines,
        "BloodHound-only product queries:",
        [identity.display() for identity in result.bloodhound_only],
    )
    _render_section(
        lines,
        "Query Library-only prebuilt queries:",
        [
            f"{query.name} ({query.path.name})"
            for query in sorted(result.library_only, key=lambda item: item.path)
        ],
    )
    _render_section(
        lines,
        "Ambiguous query identities:",
        [
            f"{match.identity.display()}: "
            + ", ".join(query.path.name for query in match.library_queries)
            for match in result.ambiguous
        ],
    )

    mismatches = [
        comparison for comparison in result.comparisons if not comparison.matches
    ]
    if mismatches:
        lines.extend(("", "Query body differences:"))

    for comparison in mismatches:
        lines.append("")
        lines.append(f"  {comparison.identity.display()}")

        variants_by_query: dict[str, list[str]] = defaultdict(list)
        for product_query in comparison.product_queries:
            variants_by_query[product_query.query].append(product_query.variant)

        for expected_query, variants in variants_by_query.items():
            variant_label = "+".join(variants)
            diff = difflib.unified_diff(
                expected_query.splitlines(),
                comparison.library_query.query.splitlines(),
                fromfile=f"BloodHound ({variant_label})",
                tofile=f"Query Library ({comparison.library_query.path.name})",
                lineterm="",
            )
            lines.extend(f"    {line}" for line in diff)

    status = "Drift detected." if result.has_drift else "Catalogs are synchronized."
    lines.extend(("", status))
    return "\n".join(lines)


def main(arguments: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compare BloodHound product queries with Query Library prebuilt "
            "queries."
        ),
        epilog=CLI_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "bloodhound_repository",
        type=Path,
        help="Path to a local BloodHound repository checkout.",
    )
    parsed_arguments = parser.parse_args(arguments)
    bloodhound_repository = parsed_arguments.bloodhound_repository.resolve()

    if not bloodhound_repository.is_dir():
        print(
            f"Error: BloodHound repository path does not exist: "
            f"{bloodhound_repository}",
            file=sys.stderr,
        )
        return 2

    try:
        result = audit_repositories(bloodhound_repository)
    except CatalogParseError as exception:
        print(f"Malformed BloodHound catalog: {exception}", file=sys.stderr)
        return 2
    except AuditError as exception:
        print(f"Error: {exception}", file=sys.stderr)
        return 2

    print(render_result(result))
    return 1 if result.has_drift else 0


if __name__ == "__main__":
    raise SystemExit(main())
