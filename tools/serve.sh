#!/usr/bin/env bash
# Build the site with the production config and serve it on http://localhost:8000.
#
# Usage:
#   tools/serve.sh

set -euo pipefail

cd "$(dirname "$0")/.."

python3 -m pelican -t theme -s publishconf.py
cd output
python3 -m http.server
