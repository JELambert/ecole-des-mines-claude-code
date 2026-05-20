# 02 · Build the dashboard with Claude Code

> One long prompt that gets you from "CSV on disk" to "interactive dashboard in a browser." You can paste it as-is, or adapt the bracketed parts to your own data.

## Before you start

- You've done the data exploration in [`01-analyze-the-data.md`](01-analyze-the-data.md) — you know roughly what numbers and charts you want to see.
- Claude Code is running in this folder.
- You have a Python environment manager installed. `uv` is the friendliest (one-line install: `curl -LsSf https://astral.sh/uv/install.sh | sh`). If you don't, ask Claude to install it for you.

## The build prompt

Copy this whole thing and paste it into Claude Code. Edit the bracketed sections to match what you want.

---

> I want you to build a Streamlit dashboard in this repo that visualizes `data/sentinel_health_pilot.csv` for an audience of healthcare administrators (the Maya Chen / Sentinel Health scenario in `docs/sentinel_health_brief.md`).
>
> **Read first, build second.** Before writing any code, read:
> - `data/sentinel_health_pilot.csv` (head + dtypes)
> - `docs/sentinel_health_brief.md` (the scenario + data dictionary)
> - `docs/dataset-deep-dive.md` (the derived columns and direction-of-improvement rules)
>
> Then summarize back to me, in two sentences, what the dashboard needs to show.
>
> **Project layout I want:**
> - `dashboard/app.py` — the Streamlit entry point
> - `dashboard/data/loader.py` — load + enrich the CSV (compute derived columns; honor the direction-of-improvement rules)
> - `dashboard/components/kpis.py` — the headline number tiles
> - `dashboard/components/charts.py` — one render function per chart
> - `dashboard/components/filters.py` — sidebar filters
> - `dashboard/pyproject.toml` — managed with `uv`; deps: streamlit, pandas, plotly
> - `dashboard/README.md` — one-paragraph "how to run"
>
> **Sections the dashboard needs, top to bottom:**
> 1. **KPI strip** — six tiles: total enrolled, % active, overall ER reduction %, hospitalization reduction %, average satisfaction (1–5), total program cost to date.
> 2. **Outcomes panel** — side-by-side bar charts of ER visits and hospitalizations, pre vs. during, broken out by `primary_condition`.
> 3. **Site performance** — ranked table of the 6 clinic sites across engagement and outcome metrics. Make the best and worst sites visually obvious (color or sort).
> 4. **Engagement vs. outcomes** — scatter: `avg_weekly_readings` on X, `er_reduction` on Y, dot size = `baseline_risk_score`, dot color = `primary_condition`.
> 5. **Segment cuts** — small-multiples or grouped bars showing outcomes by age band, by condition, by baseline-risk tier.
> 6. **Cost-benefit** — estimated savings (ER reduction × $1,400 + hosp reduction × $13,000) vs. `total_cost_to_date_usd`. Show net value. **Clearly label the per-event costs as assumptions.**
>
> **Sidebar filters that filter everything above:** clinic site, primary condition, status, age band, risk tier.
>
> **Constraints:**
> - Use synthetic / direction-correct math from `docs/dataset-deep-dive.md`. Don't naively subtract baseline from latest for clinical metrics — SpO2 improves *upward*.
> - Cache the loader with `@st.cache_data` so filters are fast.
> - No external auth, no database, no deployment config. Just a local dashboard I can run with `uv run streamlit run app.py`.
> - Keep the visual language calm and clinical — generous whitespace, muted color palette, large readable numbers on the KPI tiles. No emoji.
>
> **When you're done:**
> - Show me the file tree you created.
> - Run the dashboard once to confirm it starts without errors.
> - Tell me what to type to launch it myself.

---

## How to drive it

1. Paste the prompt. Let Claude read.
2. **Stop and check after the two-sentence summary.** If Claude misunderstood the scenario, correct it before any code gets written. Cheap to fix here, expensive later.
3. Let Claude scaffold the files. It will probably run the dashboard at the end and either hand you the URL or report an error.
4. If there's an error, paste the error back and say *"fix it."* Don't try to debug it yourself.
5. Open `http://localhost:8501` in your browser. Click around. Use the sidebar filters. Make sure every KPI and chart responds.

## What "done" looks like

- Six KPI tiles at the top with readable numbers.
- Each section answers exactly one of Maya's board questions.
- Filters work on every chart.
- The cost-benefit panel has a visible "this is an assumption" caveat.
- You can hand the URL to a non-technical colleague and they can use it.

## If you want something different

The prompt above is opinionated — six sections, Streamlit, Plotly. Swap any of it:

- **Want a static report instead of an interactive app?** Replace "Streamlit dashboard" with "single-page HTML report using Plotly figures and a few paragraphs of narrative."
- **Want a different tool?** Substitute *Dash*, *Gradio*, or *Panel*. Claude knows them all.
- **Want fewer sections?** Cut sections 4–6 in the prompt and ask just for KPIs + outcomes + sites.
- **Want different visuals?** Replace any chart description with what you want. Claude will do exactly what you ask, so **be specific**: "horizontal bar chart sorted descending, with the bar for the worst site colored red."

## Common first-pass problems and how to ask for fixes

| Symptom | What to say |
|---|---|
| Numbers don't match your hand-check from `01-analyze-the-data.md` | *"The overall ER reduction you're showing is X but I calculated Y. Show me the math you used and fix it."* |
| Charts are tiny / overflow / wrong colors | *"Make the chart wider, use the muted palette, and stack the bars vertically."* |
| Filter doesn't update a chart | *"The status filter isn't propagating to the engagement-vs-outcomes scatter. Make every chart respect every filter."* |
| KPI tiles wrap weirdly | *"Use `st.columns(6)` and shrink the label font so each tile fits on one line."* |
| App is slow | *"Wrap the loader in `@st.cache_data` and tell me what's slow."* |

The trick is to **describe the bug like you'd describe it to a colleague over Slack.** No code, no jargon. Claude will translate.

## What's next

Once it runs and the numbers are right, the dashboard is a *starting point*, not a finished product. Move to [`03-update-the-dashboard.md`](03-update-the-dashboard.md) for how to ask for changes after the fact.
