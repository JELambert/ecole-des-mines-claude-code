---
marp: true
theme: default
paginate: true
header: 'Describing Is the New Doing'
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
# Describing Is the New Doing

## Building your own software with Claude Code

**Joshua E. Lambert, PhD**
École des Mines de Saint-Étienne · 2026-05-22

<span class="small">A guest session with Dr. Elise Lambert's 2026 cohort</span>

---

# Who I am (30 seconds)

- **VP, Data Solutions AI at FactSet** — I build AI teams that ship real software
- **Visiting Professor, University of South Alabama** — I teach PhD students how to use ML and Python
- **PhD in Security Studies** (University of Central Florida); ML/NLP researcher before industry
- **Research domains I publish in** — political conflict, civil-military relations, NLP & conflict forecasting, applied economics, political psychology

[jelambert.com](https://jelambert.com) · [linkedin.com/in/joshuaelambert](https://www.linkedin.com/in/joshuaelambert/)

---

# A question

> Has there ever been a report, a dashboard, or a tool you wished existed — and either you lived without it, or you waited weeks for IT to build it?

---

# That is the gap

For decades, if you wanted custom software, you had to:

- **Hire a developer** — expensive, slow, hard to direct
- **Wait for IT** — slow, often deprioritized
- **Live without it** — most common outcome

Result: thousands of small, useful tools never got built. Decisions made with worse information.

---

# Paradigm shift

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

(Every patient in this dataset is **synthetic** — Elise generated it. No real patient data.)

---

# Now we switch to Claude Code

What you're about to see: **me building this dashboard, live, from scratch.**

- No slides for the next ~25 minutes
- I'll narrate as I go
- You'll see the **real terminal**, the **real prompts**, the **real edits**, and the **dashboard appearing piece by piece**
- It will not be perfect on the first try. That is the point.

When something looks unfamiliar, stop me. The vocabulary on the next slide should cover most of it.

---

# Vocabulary you'll see (1 of 2)

- **LLM** — *Large Language Model.* The AI behind the curtain. Reads text, writes text, makes decisions.
- **Claude** — the LLM I use. Made by Anthropic. (ChatGPT is OpenAI's; Gemini is Google's.)
- **Claude Code** — a tool that lets Claude read, write, and run files **on my laptop**, not just chat in a browser.
- **Terminal** — the black text window I type into. It's just another way to talk to your computer.

---

# Vocabulary you'll see (2 of 2)

- **Git repo** — a folder on my laptop that **tracks every change**, so I can undo anything.
- **GitHub** — a website where Git repos live online; lets you share + back up your code.
- **Streamlit** — the tool that turns Python data code into a web dashboard with almost no extra work.

Don't worry about memorizing these — they'll come up in context.

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

Merci à **Dr. Elise Lambert** et **Dr. Julia Fleck** pour l'invitation. Thank you all for your attention.

---

<!-- _class: lead -->
# Appendix
## (For the curious — not part of the talk)

---

# Bonus: from app to portable knowledge

The dashboard answers **today's question** — Maya's question — about Sentinel Health.

A package format called **PAX** (*Portable Analytical eXpertise*) goes further: it wraps the *domain itself* — the concepts, the findings, the data, and the analysis playbook — so the next health system can run the same analysis on their own data and get a comparable answer.

Ask afterward if curious.

---

# Bonus: how this is actually built

- **Claude Code** — the AI coding tool I used
- **Streamlit** — simplest way to make an interactive Python dashboard
- **Plotly** — the charts
- **Pandas** — the data layer
- **Marp** — these slides
- **Git** — version control; every change is undoable

You don't need to learn any of these to *use* what AI builds for you. Those are the names to google later.

---

# Bonus: what's in the shared repo

- **`data/`** — the synthetic Sentinel Health CSV
- **`slides/`** — this deck (Marp markdown)
- **`docs/`** — five guides:
  1. How to analyze the data with Claude Code
  2. How to build the dashboard (the prompt I used)
  3. How to update the dashboard
  4. Git & GitHub — the 10-minute version
  5. What Claude Code actually is

No dashboard code is shipped. You generate it yourself by pasting the prompt in guide #2.
