# 01 · Analyze the data with Claude Code

> A guided tour of how to explore `data/sentinel_health_pilot.csv` by **talking to Claude Code in plain English.** No coding required. Each section gives you a prompt you can copy verbatim, plus what you should expect Claude to do in response.

## Before you start

1. Open a terminal in the folder that holds this repo (`EcoleDesMines/`).
2. Run `claude` to start Claude Code (or open Claude Code in your IDE).
3. The dataset lives at `data/sentinel_health_pilot.csv` — 250 rows, 26 columns, synthetic patients from the Sentinel Health pilot. The full data dictionary is in `docs/sentinel_health_brief.md` and `docs/dataset-deep-dive.md`.

You don't need to read those first. Claude will read them for you.

## Step 1 — Orient yourself

**Prompt:**
> Read `data/sentinel_health_pilot.csv` and `docs/sentinel_health_brief.md`. Then in plain English tell me: what is this dataset, who collected it, how many rows, what columns, and what questions it is designed to answer. Don't write any code yet.

**What you should see:** a short summary of the Sentinel Health pilot, the five board questions, and the columns grouped by meaning (engagement, clinical, utilization, cost). If Claude jumps into Python, stop it and ask for English first.

## Step 2 — Get the headline numbers

**Prompt:**
> Compute the six headline numbers Maya would put on a one-page board memo: total patients enrolled, % currently active, overall ER reduction vs. the year before, overall hospitalization reduction, average patient satisfaction, and total program cost to date. Show your math. Use the direction-of-improvement rules from `docs/dataset-deep-dive.md`.

**What you should see:** a small table of six numbers, plus the calculation Claude did. Sanity-check them against your gut. If something looks wrong, say so — Claude will rework it.

## Step 3 — Break the headlines apart

Pick one of these and ask:

**By clinic site:**
> Show me ER reduction and hospitalization reduction broken out by `clinic_site`. Rank the six sites best to worst. Highlight any site that's an outlier in either direction.

**By condition:**
> Group patients by `primary_condition` and show me which condition shows the biggest improvement and which shows the smallest. Use both ER reduction and clinical-metric improvement.

**By engagement:**
> Split patients into engagement quartiles by `avg_weekly_readings`. For each quartile show average ER reduction. Is there a clear engagement-to-outcome relationship?

**What you should see:** a small ranked table for each cut, and a one-sentence read of what the cut reveals.

## Step 4 — Push on a finding

When something interesting surfaces, push:

> You said Lakeshore is the best-performing site. Is that because Lakeshore enrolled sicker patients (more room to improve), or because Lakeshore's care team is actually better? Look at baseline risk and engagement by site and tell me which explanation is more consistent with the data.

**What you should see:** Claude actually looks. It might say "the data doesn't let us distinguish — both explanations fit." That is the right answer when it's the right answer. The goal is to surface limits, not to get a confident answer.

## Step 5 — The economics question

> Does the program pay for itself? Use the standard US per-event costs (ER ≈ $1,400, hospitalization ≈ $13,000) and the `total_cost_to_date_usd` column. Compute estimated savings, then net value (savings − cost). Show me overall and by clinic site. Then tell me what assumptions you made and which ones are weakest.

**What you should see:** a per-patient and total-program net-value number, plus a clear note that the per-event costs are assumptions, not MeridianCare's contracted rates.

## Step 6 — Ask the question you actually have

The prompts above are scaffolding. Once Claude knows the dataset, ask whatever you'd actually want to know:

- *"Are older patients engaging less than younger patients?"*
- *"Which patients dropped out, and is there a pattern?"*
- *"If I had to cut two clinics, which two would I cut and why?"*
- *"What's the single most important chart for the board?"*

The pattern is always the same: describe what you want to know, in your own words. Don't translate it into "code-speak." Claude does that part.

## Step 7 — Save what you learned

When you've found something worth keeping:

> Append a one-paragraph summary of what we just found to `docs/findings.md` — create the file if it doesn't exist. Cite the columns you used and the rows the finding is based on.

**What you should see:** a new `docs/findings.md` (or appended to existing). This builds your audit trail. Six months later you'll forget how you got the number; the file won't.

## Habits that pay off

- **Make Claude read first, code second.** If it jumps to code before reading the dictionary, stop it.
- **Sanity-check every number.** Pick one row by hand, do the math yourself, confirm Claude got it right.
- **Ask "what's the weakest assumption?" after every result.** The honest answer is usually more useful than the number.
- **Don't ask leading questions.** *"Show me that engagement causes outcomes"* will get you a confident wrong answer. *"Does engagement correlate with outcomes, and can we distinguish correlation from causation here?"* will get you the truth.

## What's next

Once you've explored the data and know what you'd want to show on a single screen — KPIs, charts, filters — move to [`02-build-the-dashboard.md`](02-build-the-dashboard.md).
