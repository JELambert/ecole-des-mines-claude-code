#!/usr/bin/env bash
# Build the Marp deck to PDF. Requires marp-cli (`npm i -g @marp-team/marp-cli`).
set -euo pipefail
cd "$(dirname "$0")/.."
marp slides/presentation.md -o slides/presentation.pdf --allow-local-files
echo "Wrote slides/presentation.pdf"
