# Live-demo script (minute 25 → 45)

> Goal: show a working dashboard *change in front of them* in response to a plain-English request. Audience is healthcare administrators with no coding background — **keep them watching the dashboard, not the terminal.**

## Pre-stage

1. Two windows visible:
   - **Left half: the dashboard** (browser, full visible).
   - **Right half: Claude Code terminal** (smaller; they don't read it).
2. Font on terminal cranked (≥18pt) for the moments it matters.
3. Dashboard already running on Elise's real data at `localhost:8501`.
4. Phone on tether; wifi off as primary.
5. Three fallback recordings open in QuickTime, paused.

## The three asks (audience picks)

### A. "Add a chart showing visits over time"
- Default if audience is silent.
- Result is a **clearly visible new chart**. High legibility.
- Risk: low.

### B. "Color the existing chart by patient age group"
- Result: existing chart adds colored segments.
- Visually obvious, slightly more complex than A.

### C. "Add a number at the top showing average visit cost"
- A single KPI tile appears.
- Smallest visual change, but most "huh, that was easy."

All three are tuned so a non-coder sees an obvious result.

## Patter (what to say while it runs)

**Opening line, after audience picks:**
> "Watch the dashboard, not the terminal. The terminal is just receipts — it tells me what's happening underneath. The thing that matters is what changes on your screen."

**While Claude reads files:**
> "Right now it's reading the app — looking at what's already there, the same way you'd glance at a recipe before you start cooking. Notice it's not just guessing. It's checking."

**While Claude edits:**
> "Now it's writing the change. Every word is something I could read if I wanted to. Nothing is hidden. If you don't trust an AI tool — and you shouldn't trust one blindly — this is the part where you would check its work."

**While Claude runs:**
> "And now it's running it. The dashboard is going to reload in a second. If the AI made a mistake, it'll see the error itself and try to fix it. Just like you would."

**When the result appears:**
> "There. That's the change you asked for. Total time, maybe four minutes. Imagine that's the no-show report you've been meaning to build for two years."

## If it fails

| Symptom | Action |
|---|---|
| Claude Code stalls 15+ seconds | Cut to fallback video. "Let's look at one I prepared earlier — the point is the same." Don't apologize. |
| Edits but app errors out | Show the error briefly: *"see, it caught its own mistake."* If fixable in <90 seconds, fix live. Otherwise switch to fallback. |
| Network drops | Switch to tether. If that fails: fallback video. *"Welcome to live demos."* — gets a laugh. |
| Wrong file edited | Show `git checkout` — explain that **every change is undoable**, this is the safety net. Reinforces a key talking point. |

## Don't do

- Don't make this about **the model** or **prompting**. Make it about the **outcome**.
- Don't read terminal output aloud — they will tune out.
- Don't apologize for things the AI can't do — show what it *can*.
- Don't mention "tokens," "MCP," "agentic," "skills," "sub-agents," "CLI." These words turn off non-engineers in seconds.
- Don't oversell. Let the change-on-screen do the talking.

## Two reps max

Originally planned 3 reps. The plan is now **2 reps** and reclaim the time for the "what could you build" + "HIPAA" content, which is what this audience actually needs.
