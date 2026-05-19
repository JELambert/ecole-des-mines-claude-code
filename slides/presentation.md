---
marp: true
theme: default
paginate: true
header: 'Making Software Without Being a Software Engineer'
footer: 'Joshua E. Lambert · École des Mines · 2026-05-22'
style: |
  section {
    background-color: #ffffff;
    color: #1f2937;
    font-size: 30px;
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
  }
  h1 { color: #1e3a8a; font-size: 50px; }
  h2 { color: #3b82f6; font-size: 38px; }
  strong { color: #1e40af; }
  blockquote { border-left: 4px solid #3b82f6; padding-left: 16px; color: #475569; }
  .lead h1 { font-size: 62px; }
  .small { font-size: 22px; color: #64748b; }
  .big { font-size: 48px; text-align: center; padding-top: 40px; color: #1e3a8a; }
  .session-marker {
    background-color: #1e3a8a; color: white; padding: 20px;
    text-align: center; font-size: 2em;
  }
---

<!-- _class: lead -->
# Making Software Without Being a Software Engineer

## What AI coding tools mean for people who run things

**Joshua E. Lambert, PhD**
École des Mines de Saint-Étienne · 2026-05-22

<span class="small">A guest session with Prof. Elise Lambert's cohort</span>

---

# Quick note before we start

> These slides, and the working dashboard you'll see in 20 minutes, were made by AI **on my laptop, in under three hours**.

I'll only mention it once. I'm telling you so you know what's possible — not to brag.

---

# Who I am (30 seconds)

- **VP, Data Solutions AI at FactSet** — I build AI teams that ship real software
- **Visiting Professor, University of South Alabama** — I teach PhD students how to use ML and Python
- PhD in Security Studies; ML/NLP researcher before industry
- I'm here because Elise asked, and because I think this stuff actually matters for people running things

[jelambert.com](https://jelambert.com) · [linkedin.com/in/joshuaelambert](https://www.linkedin.com/in/joshuaelambert/)

---

<!-- _class: session-marker -->
# The problem this solves

---

# A question

> Has there ever been a report, a dashboard, or a tool you wished existed at your clinic — and either you lived without it, or you waited weeks for IT to build it?

(Show of hands.)

---

# That is the gap

For decades, if you wanted custom software, you had to:

- **Hire a developer** — expensive, slow, hard to direct
- **Wait for IT** — slow, often deprioritized
- **Live without it** — most common outcome

Result: thousands of small, useful tools never got built. Decisions made with worse information.

---

<div class="big">

That is what's changing.

</div>

---

<!-- _class: session-marker -->
# What's actually new

---

# Think of it like this

**Old way** — you tell a developer what you want. They go away. They come back later. You iterate slowly.

**New way** — you tell the AI what you want. It builds it **while you watch**. You see it work. You ask for changes. It changes it.

It's like having a **junior analyst sitting next to you** who can read, write, and run code — and never gets tired, never goes to lunch, never costs $90,000 a year.

---

# What it can do (plain language)

- **Read** the files on your computer (spreadsheets, documents, data)
- **Write** new files (apps, reports, charts)
- **Run** the things it writes — and show you what they do
- **Fix** what it gets wrong, when you point it out

You don't write code. You **describe what you want**, and you **check the result**.

---

# What it cannot do (be honest)

- **Read your mind.** You still have to be specific.
- **Replace knowing what's worth building.** That's still your job.
- **Be trusted blindly.** You verify. Always.
- **Touch data it shouldn't touch.** *(More on HIPAA in 10 minutes.)*

This is a **tool**, not a replacement for thinking.

---

<!-- _class: session-marker -->
# The demo: meet Maya Chen

---

# The scenario

**Maya Chen** — Chief Innovation Officer at **MeridianCare Health Network**
4 hospitals · 18 clinics · Pacific Northwest

Nine months ago Maya launched **Sentinel Health** — a **Remote Patient Monitoring** pilot:

- **250 patients** across 6 partner clinics
- Chronic conditions: **Diabetes · Hypertension · CHF · COPD**
- Bluetooth devices · symptom app · weekly virtual check-ins
- **~$1,800 per patient per year**

---

# Maya's problem

The board meets in **4 weeks**. They will decide:

- **Scale system-wide** (~12,000 eligible patients), or
- **Sunset the program.**

She needs to answer five questions. Today.

---

# The five questions

1. **Outcomes** — Are ER visits and hospitalizations actually down vs. the year before?
2. **Segmentation** — Which patient groups benefit most?
3. **Engagement** — Is engagement strong enough? Does it correlate with outcomes?
4. **Sites** — Which of the 6 clinics are working? Which aren't?
5. **Economics** — Does $1,800/patient/year pay for itself?

The dashboard we'll build answers all five.

---

# Here's the data she has

A spreadsheet. **250 rows. 26 columns.**

- Patient demographics (age, condition, baseline risk)
- Devices and engagement (readings, app logins, check-ins)
- Clinical metrics (A1C, blood pressure, weight, SpO2)
- Utilization (ER visits, hospitalizations — before & during)
- Cost (monthly, total to date)
- Patient satisfaction (1–5)

(For privacy, every patient in this dataset is **synthetic** — Elise generated it. No real patient data.)

---

# Right now — the starting point

*(Switch to live dashboard.)*

What you see: the headline numbers — ER reduction, hospitalization reduction, satisfaction, total cost — and a slice of the data.

What's missing: the specific things **you** would want to drill into.

---

<!-- _class: session-marker -->
# Live build (~20 minutes)

---

# Three things we could add — you pick

1. **A chart of ER visits over time, by clinic site** — "Are some sites improving faster than others?"
2. **Color the engagement scatter by patient age band** — "Are older patients engaging differently?"
3. **A headline number showing average net value per patient** — "Is this paying off, per patient?"

(Audience picks. Silence → default to #1.)

---

# Here's what I'm going to do

1. I type the request in plain English
2. The AI reads the existing dashboard
3. It writes the change
4. It runs it
5. We look at the result together
6. If it's wrong, we say so, and it tries again

**Watch the dashboard, not the terminal.** The terminal is just receipts.

---

# What you just saw

- **Plain English in, working software out**
- **Total time: a few minutes** for something that would have been a Jira ticket
- The result is **a thing you can keep, share, and run again** — not a one-off chat answer

Now imagine doing this for a problem at your clinic.

---

<!-- _class: session-marker -->
# What this means for your work

---

# Things you could build in a weekend

- **A no-show predictor** — flag patients likely to miss next week
- **A scheduling fairness check** — are slots distributed evenly across providers?
- **A one-off survey analyzer** — paste 200 responses, get themes back
- **A cost-per-visit dashboard** — by category, by provider, by month
- **A staff hour tracker** — read the timecard CSV, flag anomalies
- **A billing audit helper** — find claims that look unusual
- **A patient-letter drafter** — write the first draft, you edit

Every one of these has been built by a non-engineer in a weekend.

---

# Like Maya's dashboard — but for you

The dashboard you just watched get built **costs less to build than one consultant lunch**.

It answers questions a board will pay six figures to answer correctly.

The constraint is no longer "can we build it" — it's "**do we know what to ask for?**"

---

# The honest cost

| Tool | Cost | When to use |
|---|---|---|
| **ChatGPT / Claude (chat)** | $0–$20/mo | Quick questions, drafting, explanations |
| **Claude Code / Cursor** | $20/mo + usage | Building actual software |
| **Heavy use (API direct)** | $50–$300/mo | Daily power user |

For comparison: hiring one developer for one week ≈ **$5,000+**.
A year of Claude ≈ **$240**.

The economics aren't close.

---

# The HIPAA conversation

**Do not paste patient identifiers into a public chatbot.** Consumer ChatGPT and Claude are **not HIPAA-compliant** by default.

**Safer paths:**
- Run the AI tool **on your own laptop** with **de-identified or synthetic data** (this is what we did today)
- Use **enterprise tiers** with signed BAAs (Anthropic and OpenAI both offer them)
- Talk to your **compliance officer before** putting any PHI near these tools

**Rule of thumb:** if it would be a problem to email it to your friend, it's a problem to put it in a chatbot.

---

# Maya's dashboard was synthetic on purpose

The Sentinel data you saw isn't real. Elise generated it for this lecture.

That's deliberate. **Demonstrate the workflow on fake data; rebuild on the real thing inside your organization's environment.**

This is the pattern: prototype publicly, deploy privately.

---

# How to start Monday morning

1. **Install Claude Desktop** (free) at [claude.ai/download](https://claude.ai/download)
2. **Pick one boring task** — a report you make every month, a spreadsheet you clean up by hand
3. **Ask it:** *"Help me automate this. Here's an example of what I do today."*
4. Spend 30 minutes. See how far it gets.

That's the whole first step. Not a course. Not a certification. **Thirty minutes.**

---

# What I want you to leave with

1. **You can now make software without being a software engineer.** This is new. It's real.
2. **Start with one small, real thing.** Not a moonshot.
3. **Be careful with patient data.** HIPAA hasn't gone away.
4. **The skill that matters isn't typing prompts.** It's knowing what's worth building — and that's what you already have.

---

<!-- _class: session-marker -->
# Questions?

---

# Contact + further reading

- [jelambert.com](https://jelambert.com)
- [linkedin.com/in/joshuaelambert](https://www.linkedin.com/in/joshuaelambert/)
- [joshlambert.substack.com](https://joshlambert.substack.com) — I write about this
- Email: JoshuaE.Lambert@gmail.com

**The deck and the dashboard you saw** are in a repo I'll share after the talk.

Merci à **Elise** pour l'invitation. Thank you all for your attention.

---

<!-- _class: lead -->
# Appendix
## (For the curious — not part of the talk)

---

# Bonus: from app to portable knowledge

The dashboard answers **today's question** — Maya's question — about Sentinel Health.

A package format called **PAX** (*Portable Analytical eXpertise*) goes further: it wraps the *domain itself* — the concepts, the findings, the data, and the analysis playbook — so the next health system can run the same analysis on their own data and get a comparable answer.

The repo includes a PAX skeleton for the Sentinel domain. Ask afterward if curious.

---

# Bonus: how this is actually built

- **Claude Code** — the AI coding tool I used
- **Streamlit** — simplest way to make an interactive Python dashboard
- **Plotly** — the charts
- **Pandas** — the data layer
- **Marp** — these slides
- **Git** — version control; every change is undoable

You don't need to learn any of these to *use* what AI builds for you. Those are the names to google later.
