<p align="center">
    <a href="https://github.com/SpecterOps/BloodHoundQueryLibrary">
        <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fspecterops%2F.github%2Fmain%2Fconfig%2Fshield.json"
        alt="Sponsored by SpecterOps"/>
    </a>
    <a href="https://ghst.ly/BHSlack">
        <img src="https://img.shields.io/badge/Slack-%23cypher_queries-blueviolet?logo=slack" 
        alt="Slack"/>
    </a>
    <a href="https://github.com/SpecterOps/BloodHoundQueryLibrary/actions">
        <img src="https://github.com/SpecterOps/BloodHoundQueryLibrary/actions/workflows/syntax.yml/badge.svg"
        alt="Syntax check"/>
    </a>
</p>


# BloodHound Query Library

The BloodHound Query Library is a community-driven collection of [Cypher queries](https://support.bloodhoundenterprise.io/hc/en-us/articles/16721164740251) designed to help [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound) and [BloodHound Enterprise](https://specterops.io/bloodhound-overview/) users to unlock the full potential of the flexible BloodHound platform by creating an open query ecosystem.

The library is a free tool for the community maintained in a human-readable format (YAML) through this repository and the searchable front-end at https://queries.specterops.io/

![BloodHound Query Library frontend screenshot](queries.specterops.io.png)

You can also easily bulk import all queries into BloodHound:

1. Download [Queries.zip](https://github.com/SpecterOps/BloodHoundQueryLibrary/releases/latest/download/Queries.zip) from Releases.
2. Import `Queries.zip` by either:
   - UI: Explore -> Cypher -> Import
   - API: [/api/v2/saved-queries/import](https://bloodhound.specterops.io/reference/cypher/import-one-or-more-cypher-queries)

For an introduction to the project, please read the blog posts:

- [Jun 17, 2025: Introducing the BloodHound Query Library](https://specterops.io/blog/2025/06/17/introducing-the-bloodhound-query-library/)
- [Apr 15, 2026: What’s New in the BloodHound Query Library: BYOL, OpenGraph, Multi-Server, and More](https://specterops.io/blog/2026/04/15/whats-new-in-the-bloodhound-query-library-byol-opengraph-multi-server-and-more/)

## Deprecation Notice: `system_tags` Queries

Queries in the library currently use two methods to scope nodes to Tier Zero and Owned, supporting both old and new versions of BloodHound. At the end of July 2026, all queries will be updated to use the newer simpler method.

Old versions require scoping with a node property and null handling:

```cypher
WHERE COALESCE(n.system_tags, '') CONTAINS 'admin_tier_0'
```

New versions can use node labels directly:

```cypher
WHERE (n:Tag_Tier_Zero)
```

The simpler label-based approach was introduced with [Privilege Zones](https://specterops.io/privilege-zones/), which became generally available in [v2026.03.23](https://bloodhound.specterops.io/resources/release-notes/2026-03-23). Upgrade your BloodHound version to ensure queries from the library continue to work.

## Overview

The library contains queries that demonstrate BloodHound's versatility beyond traditional attack path analysis. This includes:
- All existing pre-built queries from BloodHound
- Cherry-picked community queries
- SpecterOps-created queries BloodHound Enterprise customers found valuable
- Community contributed queries (see [Contributing](#contributing))
- Novel queries to further showcase BloodHound's security assessment capabilities (see [security-assessment-mapping.md](/docs/security-assessment-mapping.md))

Individual query files are stored in [/queries](/queries/) as `.yml` and are automatically combined into a single Queries.json/Queries.zip as part of our [releases](https://github.com/SpecterOps/BloodHoundQueryLibrary/releases).

The query files use the YAML structure found in [query-structure.yml](/docs/query-structure.yml), for example:

```yaml
name: Entra ID SSO accounts not rolling Kerberos decryption key
guid: 1867abf8-08e3-4ea8-8f65-8366079d35c4
prebuilt: false
platforms: 
- Active Directory
- Azure
category: Configuration Weakness
description: Microsoft highly recommends that you roll over the Entra ID SSO Kerberos decryption key at least every 30 days.
query: |-
  MATCH (n:Computer)
  WHERE n.name STARTS WITH "AZUREADSSOACC."
  AND n.pwdlastset < (datetime().epochseconds - (30 * 86400))
  RETURN n
revision: 1
resources: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso-faq#how-can-i-roll-over-the-kerberos-decryption-key-of-the--azureadsso--computer-account-
acknowledgements: Martin Sohn Christensen, @martinsohndk
```

Whenever new queries are added, the syntax is automatically validated, ensuring that only syntactically compatible queries are added.

## Security Assessment Mapping

BloodHound queries in this library have been mapped to controls from common security assessment tools, demonstrating how BloodHound can validate findings typically associated with dedicated tools like PingCastle, Microsoft Defender for Identity, and Tenable Nessus.

For full coverage details and mapping structure, see [security-assessment-mapping.md](/docs/security-assessment-mapping.md).

## Learning Cypher Queries

One of BloodHound’s key features is its flexibility through Cypher queries – a query language to search the BloodHound graph database.

Queries can answer anything from simple questions (e.g., “*Which users haven’t reset their passwords in 180 days?*”), to complex identity attack path problems (e.g., “*Which low-privileged users can compromise computers hosting a gMSA with unconstrained delegation?*”).

The library gives you practical examples for learning Cypher and can be combined with these resources:
- [BloodHound documentation: Searching with Cypher](https://bloodhound.specterops.io/analyze-data/explore/cypher-search)
- [queries.specterops.io Cheat Sheet](https://queries.specterops.io/cheatsheet)
- [openCypher resources](https://opencypher.org/resources/)
- [Neo4j Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/current/lists/)

You can also learn with the community by joining the #cypher_queries channel in the [BloodHound community Slack](https://bloodhound.specterops.io/resources/community-support/getting-help).

## BloodHound Operator usage example

Command line usage is easy with the [BloodHound Operator](https://github.com/SadProcessor/BloodHoundOperator) PowerShell module.

First load the `Queries.json`:

```powershell
$queries = Invoke-RestMethod "https://github.com/SpecterOps/BloodHoundQueryLibrary/releases/latest/download/Queries.json"
```

Example: Run a query in BloodHound:

```powershell
$queries[0] | BHInvoke
```

```powershell
Name      : Tier Zero / High Value external Entra ID users
Query     : MATCH (n:AZUser)
            WHERE ((n:Tag_Tier_Zero) OR COALESCE(n.system_tags, '') CONTAINS 'admin_tier_0')
            AND n.name CONTAINS '#EXT#@'
            RETURN n
            LIMIT 100
Result    : {@{label=ASADMIN_PHANTOMCORP.ONMICROSOFT.COM#EXT#@PHANTOMCORP.ONMICROSOFT.COM; kind=AZUser; objectId=D5C8A563-34C0-41EB-BC89-14
            A2ECB4CA62; isTierZero=True; isOwnedObject=False; lastSeen=2025-06-17T13:29:14.601282321Z; properties=}, @{label=RHADMIN_PHANTO
            MCORP.ONMICROSOFT.COM#EXT#@PHANTOMCORP.ONMICROSOFT.COM; kind=AZUser; objectId=C1C0F17B-58F1-4B04-B50C-2B194B74E75D; isTierZero=
            True; isOwnedObject=False; lastSeen=2025-06-17T13:29:24.198Z; properties=}}
Count     : 1
Timestamp : 17-06-2025 13:55:27
Duration  : 00:00:00.0265562
```

Example: Import a few queries to BloodHound's Custom Searches:

```powershell
$queries[0..4] | New-BHPathQuery
```

Example: Test all queries

```powershell
$results = [System.Collections.ArrayList]::new()
$queries | % { 
    "$($results.Count + 1)/$($queries.Count) $($_.name)"
    $results.Add([PSCustomObject]@{
        Name = $_.name
        Time = (Measure-Command { 
            $errorMsg = $null
            try {
                $result = $_ | BHInvoke -WarningAction "Stop"
            } catch {
                $errorMsg = $_.Exception.Message
            }
        }).TotalSeconds
        Result = $result
        Error = $errorMsg
    }) | Out-Null
}
```

## Contributing

The BloodHound Query Library's success depends on community participation. BloodHound users who have developed useful queries are encouraged to contribute them to the library.

Before committing, please ensure that:
- The query follows the [YAML query structure](docs/query-structure.yml).
- The query is compatible with the [latest BloodHound CE version](https://github.com/SpecterOps/BloodHound)
- The query passes all automated CI/CD tests
