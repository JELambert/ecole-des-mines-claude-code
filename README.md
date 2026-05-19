# École des Mines — Claude Code Guest Lecture

Friday 2026-05-22 · ~60 min · Saint-Étienne · invited by [[elise]] for her grad-student cohort.

## What this repo is

A self-contained build for a one-hour live lecture that **uses itself as the demo**. The talk is *about* developing with Claude Code, and every artifact here was built with Claude Code on a deadline — so the repo doubles as the worked example.

```
slides/        Marp markdown deck → PDF/HTML
dashboard/     Streamlit app over Elise's dataset (the live demo)
pax/           Praxis PAX package wrapping the dataset's domain (bonus arc)
docs/          Timeline, demo script, talking notes, risk register
scripts/       Build helpers (slides → PDF, dashboard launch)
PLAN.md        The model — read this first
```

## Read order

1. `PLAN.md` — end-to-end plan: timeline to Friday, hour arc, scope cuts, risk register
2. `docs/timeline.md` — day-by-day execution checklist
3. `docs/demo-script.md` — moment-by-moment live demo script
4. `slides/presentation.md` — the actual deck (Marp markdown)

## Run the deck

```bash
cd slides
marp presentation.md -o presentation.pdf
# or live preview:
marp -s .
```

Install: `npm i -g @marp-team/marp-cli`.

## Run the dashboard

```bash
cd dashboard
uv sync
uv run streamlit run app.py
```

Runs out of the box on **synthetic data**. Drop Elise's real file into `dashboard/data/` and the loader auto-picks it up.

## Run the PAX (bonus)

```bash
cd pax
# validate against the PAX v4 spec
python -m praxis_cli validate .   # if installed
```

See `pax/README.md` for the full play.

## Status

| Artifact | Status | Notes |
|---|---|---|
| Plan | ✅ scaffold | Refined Mon 5/19; revisit Wed |
| Slides | 🟡 scaffold | ~25 slide skeleton; intro slides ready |
| Dashboard | 🟡 scaffold | Synthetic-data version runnable; awaits Elise's data |
| PAX | 🟡 scaffold | Manifest + stubs; populate once domain is known |
| Rehearsal | ⏳ Thu | Full dry-run with timer |

## Contact

Josh Lambert · JoshuaE.Lambert@gmail.com · https://jelambert.com
