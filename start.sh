#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
command -v python3 >/dev/null 2>&1 || { echo "Python 3 is required." >&2; exit 1; }
exec python3 server.py "$@"
