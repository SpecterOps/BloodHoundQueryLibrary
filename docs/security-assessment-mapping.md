# BloodHound as a Comprehensive Assessment Platform
BloodHound was designed to solve the complex problem of attack paths. Beyond this primary function, users can utilize BloodHound's powerful query language to validate simpler security assessment scenarios tested by various other tools (e.g., “Which users have non-expiring passwords?”).

To assist in these broader security assessment capabilities, BloodHound queries have been mapped to common security assessment tools, demonstrating overlap in capabilities.

This approach enables different security teams to leverage BloodHound's comprehensive attack path data for multiple kinds of risk validation, whether they're conducting red team assessments, blue team analysis, or compliance audits.

The BloodHound-centric mapping data is available at [security-assessment-mapping.json](/docs/security-assessmet-mapping.json)

## Assessment Coverage Overview

The following show which other security tools the mapping supports and the number BloodHound queries in the BloodHound Query Library that correspond to controls performed by the tools.

| Security Tool | Total Controls | Mapped Controls | Coverage |
|---------------|-------------------|---------------|----------|
| [Netwrix PingCastle](https://www.pingcastle.com/PingCastleFiles/ad_hc_rules_list.html) | 186 | 105 | 56% |
| [Microsoft Defender for Identity: Security Posture Assessment](https://learn.microsoft.com/en-us/defender-for-identity/security-assessment) | 45 | 35 | 78% |
| [Tenable Nessus: Active Directory Starter Scan](https://www.tenable.com/blog/new-in-nessus-find-and-fix-these-10-active-directory-misconfigurations) | 10 | 10 | 100% |

## Mapping Structure
Each mapping includes a type that describes the relationship:
- `exact` - Query identifies the same risk with same scope
- `partial` - Query covers the core risk but with different approach/scope
- `superset` - Query covers everything the other tool does plus additional risk analysis
- `combination` - Single query maps to multiple controls that together equal its functionality

Each BloodHound query entry includes its GUID and an array of tool mappings. Tool mappings specify the security tool, specific control details, mapping type, and any relevant notes about scope differences.

For example, the below mapping excerpt shows the BloodHound query [Tier Zero computers with passwords older than the default maximum password age](../queries/Tier%20Zero%20computers%20with%20passwords%20older%20than%20the%20default%20maximum%20password%20age.yml) maps to one PingCastle control and one MDI, while also supsesetting them - increasing risk coverage by expanding the scope to Tier Zero.

```json
{
    "bloodhound_query": {
        "guid": "b6d6d0bf-130e-4719-996b-adc29bba36e9",
        "name": "Tier Zero computers with passwords older than the default maximum password age"
    },
    "maps_to": [
        {
            "source": "PingCastle",
            "controls": [
                {
                    "mapping_scope": "superset",
                    "mapping_scope_detail": "Expanded scope to Tier Zero",
                    "id": "S-PwdLastSet-DC",
                    "name": "[M]Check if all DC are using regular password change practices"
                }
            ]
        },
        {
            "source": "MDI",
            "controls": [
                {
                    "mapping_scope": "superset",
                    "mapping_scope_detail": "Expanded scope to Tier Zero",
                    "id": "Change Domain Controller computer account old password",
                    "name": "Change Domain Controller computer account old password"
                }
            ]
        }
    ]
}
```

> [!IMPORTANT]
> These mappings are provided "as is" with [Limitation of Liability](/LICENSE). While every effort has been made to ensure their accuracy, they have been created based on public documentation. Please contribute to the project if you identify any inaccuracies by opening an Issue or submitting a Pull Request. It is best practice to use multiple tools to ensure comprehensive risk coverage and accuracy.
