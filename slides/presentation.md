---
marp: true
theme: default
paginate: true
header: 'École des Mines — Building with Claude Code'
footer: 'Joshua E. Lambert · 2026-05-22 · jelambert.com'
style: |
  section {
    background-color: #ffffff;
    color: #1f2937;
    font-size: 28px;
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
  }
  h1 { color: #1e3a8a; font-size: 48px; }
  h2 { color: #3b82f6; font-size: 36px; }
  strong { color: #1e40af; }
  code { font-size: 22px; background: #f1f5f9; padding: 1px 6px; border-radius: 3px; }
  pre code { font-size: 20px; }
  table { font-size: 22px; }
  blockquote { border-left: 4px solid #3b82f6; padding-left: 16px; color: #475569; }
  .lead h1 { font-size: 60px; }
  .session-marker {
    background-color: #1e3a8a; color: white; padding: 20px;
    text-align: center; font-size: 2em;
  }
  .small { font-size: 20px; color: #64748b; }
---

<!-- _class: lead -->
# Building with Claude Code

## A one-hour guest lecture

**Joshua E. Lambert, PhD**
École des Mines de Saint-Étienne · 2026-05-22

<span class="small">Invited by Prof. Elise Lambert · grad-student cohort</span>

---

# Meta-disclosure

> These slides were written with Claude Code.
> So was the dashboard you'll see at minute 25.
> So was the PAX package you'll see at minute 45.
>
> Total build time: **under three hours**, including this disclosure.

The **medium is the message**. Hold me to it.

---

# Who I am

**Joshua E. Lambert, PhD**
VP, Data Solutions AI · FactSet Research Systems (S&P 500)
Global Scholar & Visiting Professor · University of South Alabama

Building & scaling AI teams in regulated industries: production knowledge graphs, NLP, GenAI. Cross-domain — financial services, defense, international development.

**Teaching:** BA798 (ML & AI for Business Analytics), BUS751 (Python for Business Analytics) — PhD-level.

**Online:**
- 🌐 [jelambert.com](https://jelambert.com)
- 💼 [linkedin.com/in/joshuaelambert](https://www.linkedin.com/in/joshuaelambert/)
- ✍️ [joshlambert.substack.com](https://joshlambert.substack.com)
- 💻 [github.com/JELambert](https://github.com/JELambert)

---

# Background (one slide, then we move on)

- **PhD**, Security Studies, University of Central Florida
- **MA**, Political Science, University of New Orleans
- **BA**, Political Science, Auburn University

8 peer-reviewed journals · 2 book chapters · policy reports
Research has spanned political psychology, conflict forecasting, fisheries security, NLP applications, AI governance.

Today I want to show you a **tool**, not a CV.

---

<!-- _class: session-marker -->
# Part 1 — What is Claude Code?

---

# Claude Code is not autocomplete

| | Autocomplete (Copilot, Cursor tab) | Chat (ChatGPT in a browser) | **Agentic CLI (Claude Code)** |
|---|---|---|---|
| Lives in | Your editor | A browser tab | **Your terminal, in your repo** |
| Context | Open file ± nearby | What you paste | **The whole project, your tools, your shell** |
| Action | Suggests next token | Suggests text | **Reads, writes, runs, retries** |
| Memory | None | Per-conversation | **Files, hooks, skills, persistent** |

The shift: from *suggesting code* to **doing the work** alongside you.

---

# The loop (mental model)

```
┌──────────────┐
│  You speak   │  natural language, your repo as context
└──────┬───────┘
       ▼
┌──────────────┐
│  Plan        │  tool calls drafted, dependencies traced
└──────┬───────┘
       ▼
┌──────────────┐
│  Act         │  Read / Edit / Write / Bash — in your tree
└──────┬───────┘
       ▼
┌──────────────┐
│  Verify      │  tests, linters, runs the thing
└──────┬───────┘
       ▼
┌──────────────┐
│  Report      │  diff summary, what changed, what's next
└──────────────┘
```

Each step is **observable**. You see every file touched.

---

# Three primitives that change everything

**Skills** — reusable workflows (e.g. `/cite` ingests a paper end-to-end; `/intake` processes voice memos)

**Hooks** — shell commands that fire on events (`SessionStart` injects today's context; `PreToolUse` blocks dangerous ops)

**Sub-agents** — Claude can spawn isolated workers (research, code review, parallel exploration) and synthesize

Together: you're not prompting a chatbot. You're **directing a system**.

---

# A real session, anatomized

```text
$ claude
> add a category filter to the dashboard and chart trends per category

⏺ Reading dashboard/app.py …
⏺ Reading dashboard/data/loader.py …
⏺ Edit dashboard/app.py (+18 −2)
⏺ Edit dashboard/components/filters.py (new, 24 lines)
⏺ Bash: uv run streamlit run app.py --check
   ✓ runs, no errors
⏺ Task: write a test for the new filter
   ✓ 3 assertions pass

Done. New filter in the sidebar; trend chart respects it. Committed.
```

Watch this happen in 6 minutes at minute 25.

---

<!-- _class: session-marker -->
# Part 2 — The dataset & the question

---

# The data (Elise's contribution)

<!-- Fill in once dataset arrives -->

**Source:** *(provided by Prof. Lambert)*
**Shape:** *(rows × cols — TBD)*
**Domain:** *(TBD — digital health / informatics likely)*
**The question we'll answer:** *(TBD)*

> Why real data matters here: the demo is only convincing if the dashboard solves a problem you actually have.

---

# The dashboard (target state)

A Streamlit app with:

- **KPI strip** at the top (3–5 headline numbers)
- **Filters** in the sidebar (date range, category, segment)
- **Two charts** — one trend, one breakdown
- **Drill-down table** at the bottom

Built end-to-end through Claude Code. The git history *is* the lecture notes.

---

<!-- _class: session-marker -->
# Part 3 — Live demo (~20 min)

---

# What I'll do live

1. Open the repo in Claude Code
2. Show the current dashboard running
3. **You pick** one of three extensions:
   - Add a new filter
   - Add a metric trend
   - Add a cross-tab tab
4. Drive Claude Code to implement it
5. Run it · fix what breaks · commit

If the network fails: I have three recordings ready. The point survives.

---

<!-- placeholder slide kept short — actual live action happens off-deck -->

# What you'll notice

- Claude Code **asks before doing risky things** (deleting files, force-push)
- It **reads before it writes**
- It runs the test/server itself; you see real output, not promises
- The diff is reviewable; nothing is opaque

---

<!-- _class: session-marker -->
# Part 4 — Bonus: PAX

---

# From app to portable knowledge

A **PAX** (*Portable Analytical eXpertise*) is a package format that bundles:

- The **concepts** in a domain (constructs)
- The **knowledge** about it (findings, with structured statistics)
- The **raw data** behind the findings
- A **playbook** — a reproducible analysis workflow

It's an open spec — see [pax-market.com](https://pax-market.com).

---

# Why this matters

Your dashboard answers *today's* question.
A PAX captures the **domain itself** so the next person can:

- Re-derive the findings from the raw data
- Compare across studies on the same constructs
- Run the playbook on new data and get a comparable answer

It's the difference between **shipping an answer** and **shipping a method**.

---

# What the PAX looks like

```
pax/
├── pax.yaml                          # manifest
├── knowledge/
│   ├── domain.json                   # the field
│   ├── constructs.json               # variables, with formal definitions
│   ├── sources.json                  # where claims came from
│   └── findings.json                 # claims, with effect sizes + p-values
└── playbooks/
    └── quick_start.yaml              # reproducible analysis
```

Built — like the dashboard — with Claude Code.

---

<!-- _class: session-marker -->
# Part 5 — What this changes

---

# Where Claude Code lands well

- **Scaffolding** — new repos, boilerplate, "make me a starting point"
- **Mechanical refactors** — rename, split, restructure
- **Glue code** — wiring APIs, dashboards, ETL
- **Tests** — writing them, fixing them, expanding coverage
- **Docs** — README, comments, ADRs
- **Exploring unfamiliar code** — "explain this module"

---

# Where it doesn't (yet)

- **Original research** — it can speed up the surrounding work, not the insight
- **Decisions involving real stakes** — security, money, irreversible ops
- **Domains it has no context for** — your private codebase still requires your judgment
- **Replacing the human who understands the problem** — you stay in the loop

The skill that compounds isn't *prompting*. It's **deciding what to build**.

---

# How your students could start

1. Install: `npm install -g @anthropic-ai/claude-code`
2. Open a small project; run `claude`
3. Pick **one** boring task you've been putting off; let Claude Code do it
4. Read the diff. Don't accept blindly.
5. Build a habit: every week, one task you'd have dreaded — let the tool drive
6. After two weeks, write your first **skill** (a reusable workflow)

The fluency comes from reps on real tasks, not from tutorials.

---

# References & repo

- This deck + code: `github.com/JELambert/ecole-des-mines-2026` *(public after the talk)*
- Claude Code docs: [docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code/overview)
- PAX spec: [pax-market.com](https://pax-market.com)
- My write-ups: [joshlambert.substack.com](https://joshlambert.substack.com)

**Contact:** JoshuaE.Lambert@gmail.com · [jelambert.com](https://jelambert.com)

---

<!-- _class: lead -->
# Questions?

Merci à Elise pour l'invitation.
Merci à vous pour votre attention.
