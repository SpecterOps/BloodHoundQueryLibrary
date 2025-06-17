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

The library is a free tool for the community maintained in a human-readable format (YAML) through this repository and the sleek and searchable front-end is found at https://queries.specterops.io/

![BloodHound Query Library frontend screenshot](queries.specterops.io.png)

For an introduction to the project, please read our blog post:

- [Introducing the BloodHound Query Library](https://specterops.io/blog/2025/06/17/introducing-the-bloodhound-query-library/)

# Overview

The library contains queries that demonstrate BloodHound's versatility beyond traditional attack path analysis. This includes:
- All existing pre-built queries from BloodHound
- Cherry-picked community queries
- SpecterOps-created queries BloodHound Enterprise customers found valuable
- Community contributed queries (see [Contributing](#contributing))
- Novel queries to further showcase BloodHound's security assessment capabilities (see [security-assessment-mapping.md](/docs/security-assessment-mapping.md))

Individual query files are stored in stored in [/Queries](/Queries/) as `.yml` and are automatically combined into a single  [Queries.json](/Queries.json) file that powers the front-end.

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

## Learning Cypher Queries

One of BloodHound’s key features is its flexibility through Cypher queries – a query language to search the BloodHound graph database.

Queries can answer anything from simple questions (e.g., “*Which users haven’t reset their passwords in 180 days?*”), to complex identity attack path problems (e.g., “*Which low-privileged users can compromise computers hosting a gMSA with unconstrained delegation?*”).

The library gives you practical examples for learning Cypher and can be combined with these resources:
- [BloodHound documentation: Searching with Cypher](https://support.bloodhoundenterprise.io/hc/en-us/articles/16721164740251)
- [openCypher resources](https://opencypher.org/resources/)
- [Neo4j Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/current/lists/)

You can also learn with the communty by joining the #cypher_queries channel in the [BloodHound community Slack](https://support.bloodhoundenterprise.io/hc/en-us/articles/16730536907547).

## BloodHound Operator usage example

Command line usage is easy with the [BloodHound Operator](https://github.com/SadProcessor/BloodHoundOperator) PowerShell module.

First load the `Queries.json`:

```powershell
> $queries = Invoke-RestMethod "https://raw.githubusercontent.com/SpecterOps/BloodHoundQueryLibrary/refs/heads/main/Queries.json"
```

Example: Run a query in BloodHound:

```powershell
> $queries[0] | BHInvoke


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

Example:  Import a few queries to BloodHound's Custom Searches:

```powershell
> $queries[0..4] | New-BHPathQuery
```

## Contributing

The BloodHound Query Library's success depends on community participation. BloodHound users who have developed useful queries are encouraged to contribute them to the library.

Before comitting, please ensure that:
- The query follows the [YAML query structure](docs/query-structure.yml).
- The query is compatible with the [latest BloodHound CE version](https://github.com/SpecterOps/BloodHound)
- The query passess all automated CI/CD tests