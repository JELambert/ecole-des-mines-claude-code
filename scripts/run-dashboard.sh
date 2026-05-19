#!/usr/bin/env bash
# Launch the Streamlit demo dashboard. uv handles deps.
set -euo pipefail
cd "$(dirname "$0")/../dashboard"
uv sync
uv run streamlit run app.py
