from pathlib import Path
import sys

import pytest
import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "utilities" / "python"))

import compare_prebuilt  # noqa: E402
from compare_prebuilt import (  # noqa: E402
    AuditError,
    AuditResult,
    CATALOG_RELATIVE_PATH,
    CatalogParseError,
    QueryIdentity,
    audit_repositories,
    parse_catalog,
    render_result,
)


def write_constants(source_directory: Path) -> None:
    source_directory.mkdir(parents=True, exist_ok=True)
    (source_directory / "constants.ts").write_text(
        "\n".join(
            (
                "export const OWNED_OBJECT_TAG = 'owned';",
                "export const TIER_ZERO_TAG = 'admin_tier_0';",
                "export const TAG_TIER_ZERO_AGT = 'Tag_Tier_Zero';",
                "export const TAG_OWNED_AGT = 'Tag_Owned';",
            )
        ),
        encoding="utf-8",
    )


def write_catalog(
    repository: Path,
    variant: str,
    groups: list[tuple[str, str, list[tuple[str, str]]]],
    uncommon_query: tuple[str, str] | None = None,
) -> Path:
    source_directory = repository / CATALOG_RELATIVE_PATH
    write_constants(source_directory)

    lines = [
        "const categoryAD = 'Active Directory';",
        "const categoryAzure = 'Azure';",
        "const highPrivilegedRoleDisplayNameRegex =",
        "    '^(Global Administrator|User Administrator).*$';",
        "export const CommonSearches: CommonSearchType[] = [",
    ]
    for platform, category, queries in groups:
        category_symbol = (
            "categoryAD" if platform == "Active Directory" else "categoryAzure"
        )
        lines.extend(
            (
                "    {",
                f"        subheader: '{category}',",
                f"        category: {category_symbol},",
                "        queries: [",
            )
        )
        for name, query in queries:
            lines.extend(
                (
                    "            {",
                    f"                name: '{name}',",
                    "                description: '',",
                    f"                query: `{query}` ,".replace("` ,", "`,"),
                    "            },",
                )
            )
        lines.extend(("        ],", "    },"))
    lines.append("];")

    if uncommon_query is not None:
        name, query = uncommon_query
        lines.extend(
            (
                "export const UncommonSearches: CommonSearchType[] = [",
                "    {",
                "        subheader: 'Browser Limit Test',",
                "        category: categoryAD,",
                "        queries: [",
                "            {",
                f"                name: '{name}',",
                "                description: '',",
                f"                query: `{query}` ,".replace("` ,", "`,"),
                "            },",
                "        ],",
                "    },",
                "];",
            )
        )

    path = source_directory / f"commonSearches{variant}.ts"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_library_query(
    query_directory: Path,
    filename: str,
    name: str,
    platforms: str | list[str],
    category: str,
    query: str,
    prebuilt: bool = True,
) -> Path:
    query_directory.mkdir(parents=True, exist_ok=True)
    path = query_directory / filename
    path.write_text(
        yaml.safe_dump(
            {
                "name": name,
                "guid": f"guid-{filename}",
                "prebuilt": prebuilt,
                "platforms": platforms,
                "category": category,
                "description": "Library-only metadata",
                "query": query,
                "revision": 1,
                "resources": None,
                "acknowledgements": None,
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return path


def test_parse_catalog_normalizes_interpolations_and_excludes_uncommon(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "BloodHound"
    query = (
        "MATCH (n:${TAG_TIER_ZERO_AGT})"
        "-[:${adTransitEdgeTypes}|${azureTransitEdgeTypes}]->"
        "(o:${TAG_OWNED_AGT})\\n"
        "WHERE n.name =~ '${highPrivilegedRoleDisplayNameRegex}'"
    )
    path = write_catalog(
        repository,
        "AGT",
        [("Active Directory", "Domain Information", [("Map trusts", query)])],
        uncommon_query=("Query Parse Error", "not valid cypher"),
    )

    parsed = parse_catalog(path, "AGT")

    assert len(parsed) == 1
    assert parsed[0].query == (
        "MATCH (n:Tag_Tier_Zero)-[:AD_ATTACK_PATHS|AZ_ATTACK_PATHS]->"
        "(o:Tag_Owned)\n"
        "WHERE n.name =~ '^(Global Administrator|User Administrator).*$'"
    )


def test_parse_catalog_supports_multiline_templates_and_agi_constants(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "BloodHound"
    path = write_catalog(
        repository,
        "AGI",
        [
            (
                "Active Directory",
                "Domain Information",
                [
                    (
                        "Locations of privileged objects",
                        "MATCH (n)\n"
                        "WHERE COALESCE(n.system_tags, '') CONTAINS "
                        "'${TIER_ZERO_TAG}'\n"
                        "AND COALESCE(n.system_tags, '') CONTAINS "
                        "'${OWNED_OBJECT_TAG}'\n"
                        "RETURN n",
                    )
                ],
            )
        ],
    )

    parsed = parse_catalog(path, "AGI")

    assert parsed[0].query.endswith(
        "CONTAINS 'admin_tier_0'\n"
        "AND COALESCE(n.system_tags, '') CONTAINS 'owned'\nRETURN n"
    )


def test_audit_matches_either_variant_and_ignores_filename(tmp_path: Path) -> None:
    repository = tmp_path / "BloodHound"
    query_directory = tmp_path / "queries"
    groups_agi = [
        (
            "Active Directory",
            "Domain Information",
            [
                ("Map domain trusts", "RETURN 'shared'\n"),
                ("Variant query", "RETURN 'legacy'"),
                ("Legacy only", "RETURN 'legacy only'"),
            ],
        )
    ]
    groups_agt = [
        (
            "Active Directory",
            "Domain Information",
            [
                ("Map domain trusts", "RETURN 'shared'\n"),
                ("Variant query", "RETURN 'current'"),
                ("Current only", "RETURN 'current only'"),
            ],
        )
    ]
    write_catalog(repository, "AGI", groups_agi)
    write_catalog(repository, "AGT", groups_agt)
    write_library_query(
        query_directory,
        "filename-does-not-match.yml",
        "Map domain trusts",
        "Active Directory",
        "Domain Information",
        "RETURN 'shared'",
    )
    write_library_query(
        query_directory,
        "variant.yml",
        "Variant query",
        "Active Directory",
        "Domain Information",
        "RETURN 'current'",
    )
    write_library_query(
        query_directory,
        "legacy.yml",
        "Legacy only",
        "Active Directory",
        "Domain Information",
        "RETURN 'legacy only'",
    )
    write_library_query(
        query_directory,
        "current.yml",
        "Current only",
        "Active Directory",
        "Domain Information",
        "RETURN 'current only'",
    )

    result = audit_repositories(repository, query_directory)
    matches = {
        comparison.identity.name: comparison.matching_variants
        for comparison in result.comparisons
    }

    assert not result.has_drift
    assert matches == {
        "Current only": ("AGT",),
        "Legacy only": ("AGI",),
        "Map domain trusts": ("AGI", "AGT"),
        "Variant query": ("AGT",),
    }
    implementation_statuses = {
        comparison.identity.name: comparison.implementation_status
        for comparison in result.comparisons
    }
    assert implementation_statuses == {
        "Current only": "AGT only",
        "Legacy only": "AGI only",
        "Map domain trusts": "identical AGI/AGT",
        "Variant query": "distinct AGI/AGT",
    }


def test_platform_suffixes_disambiguate_duplicate_product_names(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "BloodHound"
    query_directory = tmp_path / "queries"
    groups = [
        (
            "Active Directory",
            "Hygiene",
            [("Disabled privileged principals", "RETURN 'AD'")],
        ),
        (
            "Azure",
            "Hygiene",
            [("Disabled privileged principals", "RETURN 'AZ'")],
        ),
    ]
    write_catalog(repository, "AGI", groups)
    write_catalog(repository, "AGT", groups)
    write_library_query(
        query_directory,
        "disabled-ad.yml",
        "Disabled privileged principals (AD)",
        "Active Directory",
        "Hygiene",
        "RETURN 'AD'",
    )
    write_library_query(
        query_directory,
        "disabled-az.yml",
        "Disabled privileged principals (AZ)",
        "Azure",
        "Hygiene",
        "RETURN 'AZ'",
    )

    result = audit_repositories(repository, query_directory)

    assert not result.has_drift
    assert result.body_match_count == 2


def test_multiplatform_library_query_matches_product_platform(tmp_path: Path) -> None:
    repository = tmp_path / "BloodHound"
    query_directory = tmp_path / "queries"
    groups = [
        (
            "Azure",
            "Cross Platform Attack Paths",
            [("Cross-platform query", "RETURN 1")],
        )
    ]
    write_catalog(repository, "AGI", groups)
    write_catalog(repository, "AGT", groups)
    write_library_query(
        query_directory,
        "cross-platform.yml",
        "Cross-platform query",
        ["Active Directory", "Azure"],
        "Cross Platform Attack Paths",
        "RETURN 1",
    )

    result = audit_repositories(repository, query_directory)

    assert not result.has_drift
    assert result.body_match_count == 1


def test_audit_reports_inventory_and_body_drift(tmp_path: Path) -> None:
    repository = tmp_path / "BloodHound"
    query_directory = tmp_path / "queries"
    groups = [
        (
            "Active Directory",
            "Domain Information",
            [("Different body", "RETURN 'BloodHound'"), ("Product only", "RETURN 2")],
        )
    ]
    write_catalog(repository, "AGI", groups)
    write_catalog(repository, "AGT", groups)
    write_library_query(
        query_directory,
        "different.yml",
        "Different body",
        "Active Directory",
        "Domain Information",
        "RETURN 'Library'",
    )
    write_library_query(
        query_directory,
        "library-only.yml",
        "Library only",
        "Active Directory",
        "Domain Information",
        "RETURN 3",
    )

    result = audit_repositories(repository, query_directory)
    rendered = render_result(result)

    assert result.has_drift
    assert result.bloodhound_only == (
        QueryIdentity("Active Directory", "Domain Information", "Product only"),
    )
    assert [query.name for query in result.library_only] == ["Library only"]
    assert "[matches: neither]" in rendered
    assert "--- BloodHound (AGI+AGT)" in rendered
    assert "+RETURN 'Library'" in rendered


def test_render_diffs_each_distinct_product_variant(tmp_path: Path) -> None:
    repository = tmp_path / "BloodHound"
    query_directory = tmp_path / "queries"
    write_catalog(
        repository,
        "AGI",
        [
            (
                "Active Directory",
                "Domain Information",
                [("Variant body", "RETURN 'AGI'")],
            )
        ],
    )
    write_catalog(
        repository,
        "AGT",
        [
            (
                "Active Directory",
                "Domain Information",
                [("Variant body", "RETURN 'AGT'")],
            )
        ],
    )
    write_library_query(
        query_directory,
        "variant-body.yml",
        "Variant body",
        "Active Directory",
        "Domain Information",
        "RETURN 'Library'",
    )

    rendered = render_result(audit_repositories(repository, query_directory))

    assert "--- BloodHound (AGI)" in rendered
    assert "--- BloodHound (AGT)" in rendered
    assert rendered.count("+RETURN 'Library'") == 2


def test_audit_reports_ambiguous_library_identity(tmp_path: Path) -> None:
    repository = tmp_path / "BloodHound"
    query_directory = tmp_path / "queries"
    groups = [
        ("Active Directory", "Domain Information", [("Duplicate", "RETURN 1")])
    ]
    write_catalog(repository, "AGI", groups)
    write_catalog(repository, "AGT", groups)
    for filename in ("first.yml", "second.yml"):
        write_library_query(
            query_directory,
            filename,
            "Duplicate",
            "Active Directory",
            "Domain Information",
            "RETURN 1",
        )

    result = audit_repositories(repository, query_directory)

    assert result.has_drift
    assert len(result.ambiguous) == 1
    assert {query.path.name for query in result.ambiguous[0].library_queries} == {
        "first.yml",
        "second.yml",
    }


def test_parse_catalog_rejects_unknown_interpolation(tmp_path: Path) -> None:
    repository = tmp_path / "BloodHound"
    path = write_catalog(
        repository,
        "AGT",
        [
            (
                "Active Directory",
                "Domain Information",
                [("Unsupported", "RETURN '${notSupported}'")],
            )
        ],
    )

    with pytest.raises(CatalogParseError, match="Unsupported interpolation"):
        parse_catalog(path, "AGT")


def test_parse_catalog_rejects_missing_common_searches(tmp_path: Path) -> None:
    path = tmp_path / "commonSearchesAGI.ts"
    path.write_text("export const SomethingElse = [];\n", encoding="utf-8")

    with pytest.raises(CatalogParseError, match="CommonSearches array was not found"):
        parse_catalog(path, "AGI")


def test_cli_exit_codes(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert compare_prebuilt.main([str(tmp_path / "missing")]) == 2
    assert "repository path does not exist" in capsys.readouterr().err

    clean_result = AuditResult(0, 0, (), (), (), ())
    drift_result = AuditResult(
        1,
        0,
        (),
        (QueryIdentity("Active Directory", "Domain Information", "Missing"),),
        (),
        (),
    )

    monkeypatch.setattr(
        compare_prebuilt, "audit_repositories", lambda repository: clean_result
    )
    assert compare_prebuilt.main([str(tmp_path)]) == 0
    capsys.readouterr()

    monkeypatch.setattr(
        compare_prebuilt, "audit_repositories", lambda repository: drift_result
    )
    assert compare_prebuilt.main([str(tmp_path)]) == 1
    capsys.readouterr()

    def raise_audit_error(repository: Path) -> AuditResult:
        raise AuditError("invalid fixture")

    monkeypatch.setattr(compare_prebuilt, "audit_repositories", raise_audit_error)
    assert compare_prebuilt.main([str(tmp_path)]) == 2
    assert "Error: invalid fixture" in capsys.readouterr().err

    def raise_catalog_error(repository: Path) -> AuditResult:
        raise CatalogParseError("invalid TypeScript")

    monkeypatch.setattr(compare_prebuilt, "audit_repositories", raise_catalog_error)
    assert compare_prebuilt.main([str(tmp_path)]) == 2
    assert (
        "Malformed BloodHound catalog: invalid TypeScript"
        in capsys.readouterr().err
    )
