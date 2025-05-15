# BloodHound Queries for Security Tools
BloodHound was designed to solve the complex problem of attack paths. However, using the powerful Cypher query language, BloodHound users can also leverage its versatile database to validate simpler security scenarios tested by various other tools, such as "Users with passwords not reset for 365 days.

This page gives an overview of Cypher tests covering other security tools:
- Tool information and test coverage
- Query file locations within the library
- How the query files map specific Key/Values in their [YAML Query Structure](query-structure.yml) to the security tool

> [!IMPORTANT]
> These queries are provided "as is" with [Limitation of Liability](/LICENSE). While every effort has been made to ensure their accuracy, they have been created based on public documentation and there is no guarantee they will work perfectly or meet all needs. Please contribute to the project if you identify any inaccuracies by opening an Issue or submitting a Pull Request. We recommend using multiple tools to ensure comprehensive test coverage and accuracy.


# PingCastle
Test Overview: https://www.pingcastle.com/PingCastleFiles/ad_hc_rules_list.html
Attribution Notice: https://github.com/netwrix/pingcastle

Test Coverage: 108/186 (58.1 %)

Queries are found in:
- [Queries/Active Directory/Tool - PingCastle](https://github.com/SpecterOps/BloodHoundCypherLibrary/tree/main/Queries/Active%20Directory/Tool%20-%20PingCastle)

YAML structure mapping:
| **Key**     | **Value**                 | **Value example**                                                     |
|-------------|---------------------------|-----------------------------------------------------------------------|
| Name        | Title                     | \[M]Check if all cluster are using regular password change practices. |
| Description | Group - Category: Rule ID | Stale Objects - Inactive user or computer: S-PwdLastSet-Cluster       |
	
# Microsoft Defender for Identity: Security Posture Assessment
Test Overview: https://learn.microsoft.com/en-us/defender-for-identity/security-assessment

Test Coverage: 38/45 (84.4 %)

Queries are found in:
- [Queries/Active Directory/Tool - MDI](https://github.com/SpecterOps/BloodHoundCypherLibrary/tree/main/Queries/Active%20Directory/Tool%20-%20MDI)

YAML structure mapping:
| **Key**     | **Value**         | **Value example**                                                                      |
|-------------|-------------------|----------------------------------------------------------------------------------------|
| Name        | Title             | Accounts with non-default Primary Group ID                                             |
| Description | Category/dropdown | Accounts                                                                               |
| Resource    | Test resource     | https://learn.microsoft.com/en-us/defender-for-identity/accounts-with-non-default-pgid |

# Tenable Nessus: Active Directory Starter Scan
Test Overview: https://www.tenable.com/blog/new-in-nessus-find-and-fix-these-10-active-directory-misconfigurations

Test Coverage: 10/10 (100.0 %)

Queries are found in:
- [Queries/Active Directory/Tool - Nessus](https://github.com/SpecterOps/BloodHoundCypherLibrary/tree/main/Queries/Active%20Directory/Tool%20-%20Nessus)

YAML structure mapping:
| **Key**     | **Value**   | **Value example**                                                                     |
|-------------|-------------|---------------------------------------------------------------------------------------|
| Name        | Plugin name | Kerberoasting                                                                         |
| Description | Description | A Domain admin or Enterprise admin account is vulnerable to the Kerberoasting attack. |
