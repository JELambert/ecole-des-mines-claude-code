# PLAN — École des Mines Lecture

> The model. Read top-to-bottom. Every other file in this repo is downstream of this one.

## The ask (operator-stated)

- 1-hour guest lecture at École des Mines, Friday 2026-05-22
- Invited by Elise (his wife) for her grad-student cohort
- Topic: **using Claude Code** to build something real
- Deliverables:
  1. **Marp markdown slides** with a Josh intro (website, LinkedIn, CV, background)
  2. A **Streamlit dashboard** over data Elise provides — built end-to-end via Claude Code
  3. **Bonus:** wrap the dashboard's domain as a **PAX** (Praxis package) using the v4 creation guide
- Everything dev is done through Claude Code (this is also the message)

## The audience (informed inference)

- French graduate students at École des Mines (engineering / data science / digital health context — Elise teaches digital-health informatics)
- Mixed English fluency; slow down, no idioms, no fast switching
- Likely curious about AI coding tools but with European skepticism on hype — **demo > rhetoric**
- Probably some have used Copilot / ChatGPT; few have lived inside an agentic CLI
- Hour-long, single-session — no Q&A bumper, no prerequisites assumed

## Thesis (one sentence)

> Claude Code is a CLI-native AI agent that lets a single person build, ship, and iterate on a real, working application **on the same scale of time as the conversation you'd have describing it** — and here is the thing I made on that timeline, including these slides.

## The arc (60 min, with slack)

| Min | Block | What | Why |
|---|---|---|---|
| 0–3 | Open | Title slide + thank Elise + meta-disclosure: "these slides were built with Claude Code in <2 hours" | Earn attention; the medium is the message |
| 3–8 | Who I am | One slide: title, website, LinkedIn, CV, background, courses I teach. Quick. | Credibility, then move on |
| 8–18 | What Claude Code is | What an agentic CLI is vs. autocomplete; how it differs from chat; hooks, skills, subagents; the loop. **Live `claude --help`-style screen** | Set the conceptual frame |
| 18–25 | The dataset & the question | Show Elise's data; pose the question the dashboard answers; frame it as a real working problem | Anchor the demo |
| 25–45 | **Live demo** (~20 min) | Drive Claude Code in front of them: extend the dashboard with one feature they pick; show planning, edits, run, fix. Have **2 fallback recordings** if the live fails | The hour's center of gravity |
| 45–52 | The PAX bonus | Show the PAX wrapping the same domain; explain why structured knowledge + raw data + playbooks matter | Stretch frame: from app to portable knowledge |
| 52–58 | What this changes | Honest framing: where Claude Code lands well, where it doesn't; what to study; how Elise's students could start | Land the value |
| 58–60 | Q&A bridge | One slide of references, contact, repo URL, then questions | Open the room |

## Scope cuts (decided up front)

- **Do not** teach prompt-engineering theory. Not the topic. Show, don't lecture.
- **Do not** demo the harness / sub-agents in the live unless asked. Mention them in the deck.
- **Do not** build the dashboard live from zero. The skeleton is pre-built; the demo is **extending** it.
- **Do not** demo PAX install/run end-to-end. Show the structure + the *why*. Live install is too much variance.
- **Do not** show MCP server config. Mention by name; defer to repo links.

## Live-demo plan (the riskiest 20 minutes)

**Pre-stage:** Dashboard already runs locally on synthetic data. Real data (Elise's) is loaded into `dashboard/data/`. Three pre-tested ask candidates, any of which works:

1. "Add a filter by category X to the dashboard"
2. "Compute and chart the trend of metric Y over time"
3. "Cross-tabulate column A vs B and add it as a tab"

Let the audience pick (theater of agency). If the audience is mute, default to #1.

**Fallback ladder:**
1. **Plan A** — Claude Code drives it live, end-to-end
2. **Plan B** — Live drive partway, then play a pre-recorded screen if it stalls (recording made Wed)
3. **Plan C** — Walk through the *diff* of a previous session's transcript + show the result running. No live model call at all.

**Network:** assume École des Mines wifi is unreliable. Tether off iPhone. Have a backup PDF of the deck on the laptop.

## Pre-Friday timeline

| Day | Goal | Concrete |
|---|---|---|
| **Mon 5/19** | Scaffold | Repo, slides skeleton, dashboard skeleton on synthetic data, PAX skeleton, this plan |
| **Tue 5/20** | Elise data + dashboard | Receive dataset; wire real loader; build 2 charts + 1 KPI row; verify it runs on her laptop's environment |
| **Wed 5/21** | PAX + slide pass + recordings | Populate PAX with real domain content; finalize slide narrative; record 3 fallback demo videos |
| **Thu 5/22 morning** | Dry run | Full 60-min run with timer; tighten cuts; print PDF backup |
| **Fri 5/22** | Lecture | Show up rested |

## Risk register

| Risk | P | Impact | Mitigation |
|---|---|---|---|
| Elise's dataset arrives late | M | High — demo loses anchor | Synthetic dataset already built; can demo on synthetic + verbally bridge |
| Live model call fails (network, API, rate limit) | M | High | 3 pre-recorded fallback videos; can switch in <30s |
| Audience English too weak for nuance | M | M | Speak slowly; pause for translations; slides are mostly visual; have Elise translate Q's |
| Tooling breaks on stage (Marp, Streamlit, uv) | L | M | All commands committed in `scripts/`; tested Thu |
| Demo goes overtime | M | M | Hard timer at 45 min; PAX section is the cuttable buffer |
| Slides too dense | L | L | One-idea-per-slide enforced; verify Thu in dry run |
| PAX section confuses audience | M | M | Position as "research aside"; not the core thesis |

## Definition of done — Friday morning

- [ ] `slides/presentation.pdf` renders cleanly, ≤30 slides, no overflow warnings
- [ ] `dashboard/` runs from cold checkout with `uv sync && uv run streamlit run app.py` on Elise's real data
- [ ] 3 fallback demo videos in `docs/fallback-recordings/`
- [ ] PAX validates if `praxis-cli` available; otherwise structure is reviewable manually
- [ ] One full timed dry-run completed Thursday with stopwatch
- [ ] Phone tether tested at École des Mines wifi
- [ ] Print PDF backup of deck + USB stick

## What "the model" means

The user used the word **"model"** loosely — not an ML model. He means *the plan*. This document is the plan. Every other file follows from it. If a build choice in another file diverges from this plan, **update this file first**, then propagate.

## Open questions (for operator)

These are written but not blocking — Josh will surface answers naturally as the week goes on.

- **Q1:** What's actually in Elise's dataset? Schema, row count, sensitivity classification (anonymized? PII?)
- **Q2:** Will it be in English or French? If French, header translations needed for the live demo (audience won't see the bar charts' titles changing across languages)
- **Q3:** Is the lecture in English or French? (Elise's grad-student cohort context suggests English; confirm)
- **Q4:** Projector resolution? Marp slides should target 16:9; verify Thursday
- **Q5:** Can students follow along on laptops? If yes, share the GitHub repo URL on slide 2 so they can pull during the talk

These do not block scaffold work. Resolve them this week.
