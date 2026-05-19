# PLAN — École des Mines Lecture

> The model. Read top-to-bottom. Every other file is downstream of this one.

## The ask (operator-stated, revised 2026-05-19)

- ~60-min guest session at École des Mines, Friday 2026-05-22
- Invited by [[elise]] for the cohort she's leading on the Fulbright exchange
- **Audience: Texas healthcare administrators**, traveling with Elise. **Non-engineers, mostly never written code.** Intro level.
- Topic: using Claude Code (and AI coding tools generally) to **make software that helps you with your actual work**
- Deliverables:
  1. **Marp slides** with a quick Josh intro + main content
  2. **Streamlit dashboard** over data Elise provides — built end-to-end via Claude Code, used as the worked example
  3. ~~PAX bonus~~ → **moved to appendix only** (see "Scope cuts" below)

## The audience (revised)

- Texas-based healthcare administrators on an Elise-led France trip
- Non-engineering, mostly non-coding background
- They run clinics, manage budgets, look at reports, sit in meetings
- They've used Excel, maybe Power BI; many have used ChatGPT
- **What's interesting to them:** *"Can I make my own tools without hiring a developer?"*
- **What's NOT interesting to them:** terminal commands, agentic-CLI taxonomy, sub-agents, MCP servers, PAX schemas
- English is the working language; speak slowly, no jargon, no acronyms without unpacking
- They came on a trip with their professor — they're warm, not hostile, and curious

## Thesis (one sentence, revised)

> If you can describe the thing you wish existed, you can now make it — and here is what that looks like in practice for someone running a clinic.

## The arc (60 min, revised for non-coders)

| Min | Block | What | Why |
|---|---|---|---|
| 0–3 | Open + meta | Hi, thanks Elise, who I am in 30 seconds. One-time disclosure: "these slides, the app you're about to see, were made by AI on my laptop in under three hours." | Hook, then move on |
| 3–8 | The pain | "How many of you have ever wanted a report that didn't exist, and either lived without it or waited weeks for IT?" → land that this is *the* problem AI coding tools solve. | Make it about them, not the tool |
| 8–15 | What's actually changing | Plain-English version of "AI can now read, write, and run code on your computer." Stick figure / diagram metaphors, no terminal jargon. Compare to "having a junior analyst sitting next to you" — they understand that frame. | Build the mental model |
| 15–25 | The demo dataset | Pull up Elise's data. Frame the question we'll answer ("Can we see X by Y for our patients?"). Show what it looks like in Excel-like view. | Anchor in their world |
| 25–45 | **Live build** (~20 min) | Drive Claude Code, but **don't show the terminal much** — show the *dashboard updating*. Each loop: "I asked it to add this. Here's what changed. Let's look." Two reps max. Have a slide between them showing what was asked. | Show, don't lecture |
| 45–52 | What this means for *your* clinic | Concrete examples relevant to healthcare admin: scheduling optimizer, no-show predictor, simple cost dashboard, one-off survey analyzer. "Here's the kind of thing you could build in a weekend." | Translate to their life |
| 52–58 | Honest limits + how to start | Where AI helps, where it doesn't. **Cost reality** (~$20/mo subscription). **Where data should and shouldn't go** (HIPAA awareness). One concrete next step ("install Claude Desktop and ask it to make you a one-page summary of a spreadsheet you have"). | Buy credibility |
| 58–60 | Q&A bridge | One slide of contact + repo URL, then questions | Open the room |

## Scope cuts (decided 2026-05-19 after audience pivot)

- **PAX section CUT from main arc** — was a 7-minute research-aside; off-thesis for healthcare admins who have never coded. Kept as appendix slides + repo content for the bonus-points framing of the original ask. If a student asks "what else can you make?" the appendix can come up.
- **No comparison table** between Copilot / Cursor / Claude Code — they don't know any of those. Just say "AI coding tools."
- **Minimal terminal exposure.** Show outcomes (the dashboard updating) more than process (text scrolling). When the terminal is visible, narrate what it's doing in plain English.
- **No "skills, hooks, sub-agents" slide** — internal taxonomy that doesn't help them. Cut.
- **No "the loop" mental-model slide** — too abstract. Replaced with the "junior analyst sitting next to you" metaphor.
- **No code on slides** beyond at most one "here's what a prompt looks like" example. Code on screen = audience disengages.
- **No prompt-engineering content.** They can learn that later if they want.

## What we ADD because of the audience

- A **"problems worth solving in a clinic"** slide listing 5–7 things AI coding could help with (scheduling, no-shows, surveys, one-off reports, simple staff dashboards, billing audits). Concrete, healthcare-specific.
- A **cost slide.** "Claude is ~$20/mo for the consumer subscription, more for heavy use." Numbers earn trust.
- A **HIPAA / data-residency slide.** "Don't paste patient data into a public chatbot. Here's what's safe and what's not." This is the slide that earns the room for healthcare admins specifically.
- A **"how to start Monday morning"** slide with 3 concrete steps no programmer required.

## Live-demo plan (the riskiest 20 minutes)

**Pre-stage:** Dashboard already runs on Elise's real data. Three canned asks. Audience picks (theater of agency).

Three asks, tuned for non-coders:

1. **"Add a chart that shows visits by month."** — easiest, most legible
2. **"Color the chart by patient age group."** — small extension; visually obvious
3. **"Add a number at the top showing the average visit cost."** — a single KPI; understandable result

All three produce a *visible change in the dashboard* that a non-coder can see and judge. Avoid asks where the result is invisible.

**Fallback ladder:**
1. **Plan A** — Claude Code drives live, end-to-end
2. **Plan B** — If it stalls, switch to a pre-recorded screen capture
3. **Plan C** — Show the diff + the working result; no model call

## Pre-Friday timeline

| Day | Goal | Concrete |
|---|---|---|
| **Mon 5/19** | Scaffold + audience pivot | Done. Repo, slides skeleton, dashboard on synthetic data, plan |
| **Tue 5/20** | Elise data + dashboard for healthcare admins | Receive dataset; wire real loader; choose the two charts + KPI tuned to what an admin would actually look at; refine intro slides |
| **Wed 5/21** | Slide pass + recordings | Final slide narrative; record 3 fallback demo videos; HIPAA + cost slides locked |
| **Thu 5/22 morning** | Dry run | Full 60-min run with timer; rehearse the "junior analyst" metaphor until it lands |
| **Fri 5/22** | Lecture | Show up rested |

## Risk register (revised)

| Risk | P | Impact | Mitigation |
|---|---|---|---|
| Audience tunes out at first terminal screen | H | High | Minimize terminal time; frame everything in dashboard outcomes |
| Jargon slipping in (CLI, agentic, MCP, etc.) | M | High | Glossary check on every slide; have Elise pre-read |
| Demo stalls live | M | High | 3 pre-recorded fallback videos |
| HIPAA / data-privacy question I can't answer | M | M | Pre-prepare the "safe vs not safe" answer; defer specifics to compliance lawyer |
| "Will this take my job?" question | M | M | Honest framing: replaces tasks, not roles; raises floor for non-coders |
| Live model call fails (network, API) | M | H | Tether on iPhone; fallback videos |
| Going over time | M | M | Cut from minute 45–52 if needed |
| Slides too dense / too technical | M | H | One idea per slide; pictures > text; Elise pre-reads |

## Definition of done — Friday morning

- [ ] `slides/presentation.pdf` ≤ 25 slides, no overflow, audience-tested wording
- [ ] `dashboard/` runs cold on Elise's real data, two charts + KPI row tuned to what a healthcare admin would care about
- [ ] 3 fallback demo videos in `docs/fallback-recordings/`
- [ ] One full timed dry-run completed Thursday
- [ ] PDF backup on USB; phone tether tested
- [ ] Elise has pre-read the slides for jargon density

## Open questions (for operator)

- **Q1:** What's in Elise's dataset? Schema, row count, **is it patient data? real or de-identified?** This matters for what we show on screen.
- **Q2:** Lecture language is English, yes? (Texas admins → almost certainly yes)
- **Q3:** Projector / room setup at École des Mines
- **Q4:** Can students follow along on laptops? (Probably not relevant — they're not coding along)
- **Q5:** Should the slides quietly include a "for Elise's grad students" pointer to the more technical content, in case any of them attend?

## What "the model" means

The user used the word **"model"** loosely — not an ML model. He means *the plan*. This document is the plan. If a build choice in another file diverges from this plan, **update this file first**, then propagate.
