[CmdletBinding()]param([int]$Port=5050,[switch]$NoBrowser)
$ErrorActionPreference='Stop'; Set-Location $PSScriptRoot
$python=(Get-Command python -ErrorAction SilentlyContinue)
if(-not $python){$python=Get-Command py -ErrorAction SilentlyContinue}
if(-not $python){throw 'Python 3 was not found. Install Python 3.11 or later and try again.'}
$args=@('server.py','--port',$Port);if($NoBrowser){$args+='--no-browser'}
& $python.Source @args
