[CmdletBinding()]param([int]$Port=5050)
$ErrorActionPreference="Stop"
Set-Location $PSScriptRoot
if(-not(Test-Path .venv)){python -m venv .venv}
$py=".venv\Scripts\python.exe"
& $py -m pip install -r requirements.txt
Start-Process "http://127.0.0.1:$Port"
& $py -m waitress --listen="127.0.0.1:$Port" app:app
