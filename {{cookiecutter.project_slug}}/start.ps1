<#
start.ps1

Environment Variables
---------------------

# Valid set: ("Machine", "User")
# $Scope = "Machine"
[Environment]::SetEnvironmentVariable($Variable, $Value, $Scope)

# Scope: Process
Set-Item "env:\$Variable" "$Value"
#>

# Path
Set-Item "env:\PATH" "C:\tools\UnxUtils\bin;C:\tools\UnxUtils\usr\local\wbin;C:\cygwin64\bin;{{cookiecutter.houdini_install_path}};$env:PATH"

# Houdini Path
Set-Item "env:\HOUDINI_PATH" "$((INSTALL));&"

# Python Path
Set-Item "env:\PYTHONPATH" "{{cookiecutter.houdini_install_path}}\python27\lib\site-packages-ui-forced\PySide2;$env:PYTHONPATH"
Set-Item "env:\PYTHONPATH" "$((INSTALL))\python;$env:PYTHONPATH"

# Aliases
if (Test-Path ".\aliases.psm1") { Import-Module ".\aliases.psm1" }

# Python environment
conda activate cookiecutter