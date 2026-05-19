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

> These slides, and the working app you'll see in 20 minutes, were made by AI **on my laptop, in under three hours**.

I'll only mention this once. I'm telling you so you know what's possible — not to brag about the slides.

---

# Who I am (30 seconds)

- VP, Data Solutions AI at FactSet — I build AI teams that ship real things
- Visiting Professor at the University of South Alabama — I teach PhD students how to use ML and Python
- PhD in Security Studies; background in research before industry
- I love this stuff because it lets people build what they need, when they need it

**Online if you want:** [jelambert.com](https://jelambert.com) · [linkedin.com/in/joshuaelambert](https://www.linkedin.com/in/joshuaelambert/)

---

<!-- _class: session-marker -->
# The problem this solves

---

# A question

> Has there ever been a report, a dashboard, a tool you wished existed at your clinic — and either you lived without it, or you waited weeks for IT to build it?

(Show of hands.)

---

# That is the gap

For decades, if you wanted custom software, you had to:

- **Hire a developer** (expensive, slow)
- **Wait for IT** (slow, often deprioritized)
- **Live without it** (most common outcome)

The result: thousands of small, useful tools never got built. Decisions were made with worse information.

---

<div class="big">

That is what's changing.

</div>

---

<!-- _class: session-marker -->
# What's actually new

---

# Think of it like this

**Old way** — you tell a developer what you want. They go away. They come back later with a thing. You iterate.

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
- **Be trusted blindly.** You verify. You always verify.
- **Touch data it shouldn't touch.** *(More on HIPAA in 10 minutes.)*

This is a **tool**, not a replacement for thinking.

---

<!-- _class: session-marker -->
# The demo: Elise's data

---

# The question we'll answer

<!-- Fill in once Elise's dataset is wired -->

**Dataset:** *(brief description — Elise's data)*

**The question:** *(framed in a way an administrator would actually ask)*

**What we'll build:** a small interactive dashboard that lets you slice, filter, and chart this data — built live, in front of you.

---

# Right now — here's the starting point

*(Switch to live dashboard on screen.)*

What you see: a basic dashboard with this data already loaded.
What's missing: the specific things **you** want to see.

That's where we go next.

---

<!-- _class: session-marker -->
# Live build (~20 minutes)

---

# Three things we could add — pick one

1. **A chart showing visits over time** — "When are we busy?"
2. **Color-coding by patient age group** — "Who are we seeing?"
3. **A headline number showing average visit cost** — "What does it cost us?"

(Audience picks. If silence, we do #1.)

---

# Here's what I'm going to do

1. I type the request in plain English
2. The AI reads the existing app
3. It writes the change
4. It runs it
5. We look at the result together
6. If it's wrong, we say so, and it tries again

**Watch the dashboard, not the terminal.** The terminal is just receipts.

---

<!-- live demo happens off-deck — these slides are bumpers -->

# What you just saw

- **Plain English in, working software out**
- **Total time: a few minutes** for something that would have been a Jira ticket
- The result is **a thing you can keep, share, run again**, not a one-off chat answer

Now imagine doing this for a problem at your clinic.

---

<!-- _class: session-marker -->
# What this means for your work

---

# Things you could build in a weekend

- **A no-show predictor** — flag patients likely to miss next week's appointments
- **A scheduling fairness check** — are appointment slots distributed evenly across providers?
- **A one-off survey analyzer** — paste in 200 responses, get themes back
- **A cost-per-visit dashboard** — by category, by provider, by month
- **A staff hour tracker** — read the timecard CSV, flag anomalies
- **A billing audit helper** — find claims that look unusual
- **A patient-letter drafter** — write the first draft, you edit

Every one of these has been built by a non-engineer in a weekend.

---

# The honest cost

| Tool | Cost | When to use |
|---|---|---|
| **ChatGPT / Claude (chat)** | $0–$20/mo | Quick questions, drafting, explanations |
| **Claude Code / Cursor** | $20/mo + usage | Building actual software |
| **Heavy use (API direct)** | $50–$300/mo | Daily power use |

For comparison: hiring one developer for one week ≈ **$5,000+**.
A year of Claude ≈ **$240**.

The economics aren't close.

---

# The HIPAA conversation

**Do not paste patient identifiers into a public chatbot.** ChatGPT/Claude consumer subscriptions are not HIPAA-compliant by default.

**Safer paths:**
- Run the AI tool **on your own laptop** with **de-identified data** (this is what we did today)
- Use **enterprise tiers** with signed BAAs (Anthropic and OpenAI both offer them)
- Talk to your **compliance officer before** putting any PHI near these tools

**Rule of thumb:** if it would be a problem to email it to your friend, it's a problem to put it in a chatbot.

---

# How to start Monday morning

1. **Install Claude Desktop** (free) at [claude.ai/download](https://claude.ai/download)
2. **Pick one boring task** — a report you make every month, a spreadsheet you clean up by hand
3. **Ask it:** *"Help me automate this. Here's an example of what I do today."*
4. Spend 30 minutes. See how far it gets.

That's the whole first step. Not a course. Not a certification. Thirty minutes.

---

# What I want you to leave with

1. **You can now make software without being a software engineer.** This is new. It's real.
2. **Start with one small, real thing.** Not a moonshot.
3. **Be careful with patient data.** HIPAA hasn't gone away.
4. **The skill that matters isn't typing prompts.** It's knowing what's worth building.

That last one is what you already have.

---

<!-- _class: session-marker -->
# Questions?

---

# Contact + further reading

- [jelambert.com](https://jelambert.com)
- [linkedin.com/in/joshuaelambert](https://www.linkedin.com/in/joshuaelambert/)
- [joshlambert.substack.com](https://joshlambert.substack.com) — I write about this
- Email: JoshuaE.Lambert@gmail.com

**The deck and the app you saw:** *(repo URL — share after the talk if asked)*

Merci à [[elise|Elise]] pour l'invitation. Thank you all for your attention.

---

<!-- _class: lead -->
# Appendix
## (For the curious — not part of the talk)

---

# Bonus: from app to portable knowledge

The dashboard we built today answers **today's question**.

There's a research direction — a thing called a **PAX** (*Portable Analytical eXpertise*) — that packages the *domain itself* so the next person can re-run the same analysis on different data and get a comparable answer.

It's how "I built this once" becomes "anyone can run this anywhere."

Not part of the core talk. Ask me afterward if you're curious. Repo has the structure.

---

# Bonus: how this is actually built

- **Claude Code** — the AI coding tool I used
- **Streamlit** — the simplest way to make a Python web dashboard
- **Marp** — the slide format these slides are written in (yes, also AI-built)
- **Git** — version control; tracks every change

You don't need to learn any of these to *use* what AI builds for you. But if you want to peek under the hood, those are the names to google.
