# Data directory

Drop Elise's dataset here. The loader auto-detects:

- `*.csv`
- `*.xlsx`
- `*.parquet`

If no real file is present, the dashboard falls back to a deterministic
synthetic dataset shaped like digital-health visit records, so the demo
always runs.

**Do not commit raw data** — `.gitignore` excludes it by default.
