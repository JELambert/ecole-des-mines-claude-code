# 03 · Update the dashboard with Claude Code

> Once the dashboard exists, you'll think of changes within five minutes of looking at it. This is a menu of prompts for the most common kinds of changes, plus the habits that keep updates from spiraling.

## The setup

- Dashboard built per [`02-build-the-dashboard.md`](02-build-the-dashboard.md), running at `http://localhost:8501`.
- Claude Code open in the same folder.
- Browser visible alongside the terminal — you want to see the change land.

Streamlit auto-reloads on file save. Most prompts below produce a visible change in 5–30 seconds.

## Pattern 1 — Add a chart

> Add a new chart to the dashboard: a horizontal bar chart showing **average medication adherence by clinic site**, sorted descending, with sites below 60% colored amber. Put it in the site-performance section, below the existing ranked table. Update `dashboard/components/charts.py` and wire it into `app.py`.

**Why this works:** it's specific about *what*, *where*, and *how to color it*. Vague prompts ("add an adherence chart somewhere") will produce something you didn't picture.

## Pattern 2 — Change an existing chart

> The engagement-vs-outcomes scatter is too crowded. Switch dot color from `primary_condition` to `status` (Active / Disengaged / Withdrew / Completed), and drop the dot-size encoding entirely.

**Why this works:** it tells Claude *what to keep* (the scatter) and *what to change* (color, size). Saying "fix the scatter" without specifics gets you a redesign you didn't ask for.

## Pattern 3 — Add a KPI tile

> Add a seventh KPI tile to the top strip: **average days enrolled**. Round to whole days. Match the visual style of the other six tiles.

## Pattern 4 — Add a filter

> Add a new sidebar filter: **age band**. The options should be "<55", "55–69", "70+", computed from the `age` column. Make sure it filters every chart and KPI, not just the segment-cut section.

## Pattern 5 — Fix a number

> The hospitalization reduction in the KPI strip is showing 0.13 instead of 13%. Format it as a percentage with one decimal, like "13.4%". Check the other KPI tiles for the same bug.

**Why this works:** the second sentence ("check the others") catches a class of bugs, not just one. Cheap to ask, expensive to debug later.

## Pattern 6 — Improve the look

> The dashboard feels noisy. Do these three things:
> 1. Set the Plotly theme to `plotly_white` everywhere.
> 2. Use a single accent color (a muted blue) for the primary bars and a muted grey for secondary bars.
> 3. Increase the font size of KPI numbers by 25%.

**Why this works:** three small concrete changes, not one vague "make it look better."

## Pattern 7 — Swap in different data

> I'm replacing `data/sentinel_health_pilot.csv` with `data/my_clinic_data.csv` — same column names, different patients. Make the loader read whichever file is present and tell me up front which one it found.

**Why this works:** real-world dashboards live longer than the first dataset. Building this in early saves rebuilding later.

## Pattern 8 — Add an export

> Add a "Download report" button at the bottom of the dashboard that exports the current filtered dataset to CSV, named with today's date.

## Pattern 9 — Add a narrative

> At the top of the dashboard, below the title, add a 2–3 sentence narrative summary that updates based on the current filters. Example: "Showing 47 patients across Lakeshore and Westgate clinics. ER visits down 41% vs. baseline. Best-performing condition: CHF."

## Pattern 10 — Roll back a change

If a change broke something:

> The chart you added in the last change is hiding the cost-benefit panel. Revert that last change and try a different layout — put the new chart in its own expander below the cost-benefit panel.

Or, harder reset:

> Use `git status` and `git diff` to show me what changed since the last commit. Then revert the changes to `dashboard/components/charts.py` only — keep everything else.

## Habits that keep updates clean

### Commit before every change

Before asking for a change, say:

> Commit the current state of the dashboard with a message like "working dashboard with site + cost panels" before we start.

That way you have a safe point to roll back to. See [`04-git-and-github.md`](04-git-and-github.md) for why this matters.

### One change at a time

Ten changes in one prompt = ten places Claude can misunderstand you. Two-or-three at a time is the sweet spot.

### Watch the dashboard, not the terminal

When Claude is editing, look at the browser tab. The moment the page reloads, see if the change matches what you pictured. If not, say so before Claude moves on to the next thing.

### Describe what you see, not what you think the cause is

✅ *"The bar for Lakeshore is missing from the outcomes chart."*
❌ *"The dataframe filtering is broken in `charts.py`."*

You're not the engineer. Claude is. Just describe the symptom.

### When something works, name it

> That last change looks right. Commit it with a message describing what we did.

That makes the next mistake easy to roll back to a known-good state.

## What's next

If git terminology is unfamiliar, [`04-git-and-github.md`](04-git-and-github.md) explains it. If you want to understand what Claude Code actually is — what it can and can't see, and how it differs from ChatGPT — read [`05-what-is-claude-code.md`](05-what-is-claude-code.md).
