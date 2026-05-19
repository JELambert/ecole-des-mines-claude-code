# Dashboard

A Streamlit app built as the live demo for the École des Mines lecture.

## Run

```bash
cd dashboard
uv sync
uv run streamlit run app.py
```

## Data

Drop a `.csv`, `.xlsx`, or `.parquet` into `data/` and the loader picks it up automatically. If no real file is present, synthetic digital-health-shaped data is used so the dashboard always runs.

## Layout

```
app.py                 entry point — page config + composition
data/
  loader.py            real-file-or-synthetic loader
  README.md            where Elise's dataset goes
components/
  filters.py           sidebar filters (auto-adapts to columns)
  kpis.py              KPI strip
  charts.py            trend + breakdown
```

Components are intentionally tiny so the live-demo extension request ("add a category filter", "add a trend chart") is a one-file edit and Claude Code's diff is reviewable on stage.
