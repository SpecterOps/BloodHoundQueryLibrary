# BloodHound Query Library 
![Syntax test](https://github.com/SpecterOps/BloodHoundQueryLibrary/actions/workflows/syntax.yml/badge.svg)

The BloodHound Query Library is a collection of BloodHound [queries](https://support.bloodhoundenterprise.io/hc/en-us/articles/16721164740251) stored in a human readable format (YAML). These queries can identify security issues, attack paths, and misconfigurations in your identity environment when used with [BloodHound Enterprise](https://specterops.io/bloodhound-overview/) and [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound).


The library contains queries from multiple sources, including:
- Queries from community "cheat sheets"
- Queries that cover test cases from various security tools (see [security-tools.md](security-tools.md))
- Queries used by us at SpecterOps

All individual query files are automatically combined into a single JSON file [Queries.json](/Queries.json), which is used by the web-based search app.

The library's structure matches that of BloodHound's Pre-Built Searches. The root containing all queries is the [Queries](/Queries) directory, with subsequent levels describing Platform, Category, and lastly the individual query YAML files.

```
Queries/
├─ Active Directory/
│  ├─ Domain Information/
│  │  └─ AdminSDHolder protected Accounts and Groups.yml
│  ├─ Kerberos Interaction/
│  │  └─ Principal with SPN keyword.yml
│  ├─ Misc/
│  ├─ Owned/
│  ├─ Tool - MDI/
│  │  ├─ Accounts with non-default Primary Group ID.yml
│  │  ├─ Admin SDHolder permissions.yml
│  │  ├─ Built-in Active Directory Guest account is enabled.yml
│  │  └─ ...
└─ Azure/
```

The query definition files use the following YAML structure:

```yaml
name: AdminSDHolder protected Accounts and Groups
platform: Active Directory
category: Domain Information
description: Objects whose permissions are set by SDProp to the template AdminSDHolder object as per MS-ADTS 3.1.1.6.1.2 Protected Objects. Does not exclude objects if specified in dSHeuristics dwAdminSDExMask
query: |-
  MATCH (n:Base)-[:MemberOf*0..]->(m:Group)
  WHERE (
    n.objectid =~ ".*-(S-1-5-32-544|S-1-5-32-548|S-1-5-32-549|S-1-5-32-550|S-1-5-32-551|S-1-5-32-552|518|512|519)" // Groups
    OR m.objectid =~ ".*-(S-1-5-32-544|S-1-5-32-548|S-1-5-32-549|S-1-5-32-550|S-1-5-32-551|S-1-5-32-552|518|512|519)" // Members of groups
    OR n.objectid =~ ".*-(500|502|516|521)" // Direct objects
  )
  RETURN n
note: 
revision: 1
resources:
  - https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/a0d0b4fa-2895-4c64-b182-ba64ad0f84b8
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory
acknowledgement: 
submitter: Martin Sohn Christensen, @martinsohndk
tags:
  - OptionalTag
```

### Utilities
The library has utilities that can run/import/validate single or bulk queries.

Utilities that interact with BloodHound require [BloodHound Operator](https://github.com/SadProcessor/BloodHoundOperator)

Utilities that interact with YAML require [powershell-yaml](https://www.powershellgallery.com/packages/powershell-yaml) which you can install with `Install-Module -Name powershell-yaml`

- Invoke-BHCypherLibrary.ps1
  - Use the queries of the library with BloodHound: import as saved, or run and output results
- Validate-YAML.ps1
  - Validate the syntax of a single YAML file
- Validate-Repo.ps1
  - Validate the syntax of all YAML files in the [Cypher directory](/Cypher) directory
- ConvertFrom-YamlToSingleJson.ps1
  - Mirror all YAML files in the [/Cypher](/Cypher) directory into the single JSON file [cypher.json](/cypher.json)

Import all library queries to BloodHound saved queries:
```PowerShell
> . .\Utilities\Invoke-BHCypherLibrary.ps1
> Invoke-BHCypherLibrary -Import -AllFromJSON
```

Run all library queries in BloodHound and output results:
```PowerShell
> . .\Utilities\Invoke-BHCypherLibrary.ps1
> Invoke-BHCypherLibrary -Run -AllFromJSON
# Running query: AD: Domain Information // AdminSDHolder protected Accounts and Groups

label         : DOMAIN ADMINS@MARVEL.LOCAL
kind          : Group
objectId      : S-1-5-21-3713885868-1133516855-2403871545-512
isTierZero    : True
isOwnedObject : False
lastSeen      : 2025-02-06T16:59:09.378402702Z

[SNIP]

# Running query: AD: Tool - MDI // Change password for krbtgt account
label         : KRBTGT@MARVEL.LOCAL
kind          : User
objectId      : S-1-5-21-3713885868-1133516855-2403871545-502
isTierZero    : False
isOwnedObject : False
lastSeen      : 2025-02-06T16:59:09.378402702Z

[SNIP]
```

To remove **all** BloodHound saved queries, including those not from this library:
```
Get-BHPathQuery | Remove-BHPathQuery -Force
```

## Learning Cypher
Cypher is a powerful but sometimes underutilized feature of BloodHound, often because it requires learning the Cypher query language. However, with some effort, Cypher allows you to analyze BloodHound data in custom ways, helping you understand your specific identity relationships and risks. If you get stuck learning, connect with the [BloodHound Community](https://support.bloodhoundenterprise.io/hc/en-us/articles/16730536907547) on Slack.

- [BloodHound documentation: Searching with Cypher](https://support.bloodhoundenterprise.io/hc/en-us/articles/16721164740251)
- [openCypher resources](https://opencypher.org/resources/)
- [Neo4j Cypher Cheat Sheet](https://opencypher.org/resources/)

## Contributing

You can contribute by creating a pull request.

Before comitting, please ensure that:
- The query follows the [YAML query structure](query-structure.yml).
- The query is compatible with the [latest BloodHound CE version](https://github.com/SpecterOps/BloodHound)
- The query passess all automated CI/CD tests

