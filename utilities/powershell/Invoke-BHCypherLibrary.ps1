function Invoke-BHCypherLibrary {
    [CmdletBinding()]
    param (
        # Get single Cypher from YAML file
        [Parameter(ParameterSetName = 'Import')]
        [Parameter(ParameterSetName = 'Run')]
        [Parameter(Mandatory, ParameterSetName = 'SingleYAML')]
        [string]$YAMLFilePath,

        # Get all Cyphers from JSON
        [Parameter(ParameterSetName = 'Import')]
        [Parameter(ParameterSetName = 'Run')]
        [Parameter(Mandatory, ParameterSetName = 'AllJSON')]
        [switch]$AllFromJSON,
        [Parameter(ParameterSetName = 'AllJSON')]
        [string]$JSONPath = ".\Cypher.json",
        
        # Get all Cyphers from YAML
        [Parameter(ParameterSetName = 'Import')]
        [Parameter(ParameterSetName = 'Run')]
        [Parameter(Mandatory, ParameterSetName = 'AllYAML')]
        [switch]$AllFromYAML,
        [Parameter(ParameterSetName = 'AllYAML')]
        [string]$YAMLDirectoryPath = ".\Cypher",

        # Import
        [Parameter(Mandatory, ParameterSetName = 'Import')]
        [switch]$Import,

        # Run
        [Parameter(Mandatory, ParameterSetName = 'Run')]
        [switch]$Run
    )
    
    if ($YAMLFilePath) {
        if (-not (Get-Module powearshell-yaml)) {
            Write-Error "Missing module 'powershell-yaml'"
            return
        }

        $CypherArray = @()
        if ($YAMLFilePath.EndsWith('.yml') -or $YAMLFilePath.EndsWith('.yaml')) {
            $CypherArray += Get-Content $YAMLFilePath | ConvertFrom-Yaml
        } else {
            Write-Error "Filetype not .yml or .yaml"
            return
        }
    } elseif ($AllFromYAML) {
        if (-not (Get-Module powearshell-yaml)) {
            Write-Error "Missing module 'powershell-yaml'"
            return
        }

        $CypherArray = @()
        Get-ChildItem -Path $YAMLDirectoryPath -Recurse -Include *.yml,*.yaml | % {$CypherArray += Get-Content $_ | ConvertFrom-Yaml }
    } elseif ($AllFromJSON) {
        $CypherArray = Get-Content $JSONPath | ConvertFrom-Json
    }

    foreach ($Cypher in $CypherArray) {
        switch ($Cypher.Platform) {
            "Active Directory" {$Platform = "AD: "}
            "Azure" {$Platform = "AZ: "}
        }
        $Name = ($Platform + $Cypher.Category + ' // ' + $Cypher.Name)

        if ($Import) {
            New-BHPathQuersy -Name $Name -Description $Cypher.Description -Query $Cypher.Query
        } elseif ($Run) {
            Write-Host "# Running query: $Name" -ForegroundColor Yellow
            try {
                $o = Invoke-BHCypher -Query $Cypher.Query -Minimal
            } catch {
                Write-Host $_
            }
            #pause
        }
    }
}