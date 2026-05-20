# 05 · What Claude Code actually is

> The mental model behind the demo. Written for someone who's used ChatGPT in a browser and is wondering how this is different.

## In one paragraph

**Claude Code is Claude — the AI made by Anthropic — running on your laptop, with permission to read your files, write new ones, and run commands on your computer.** A browser chatbot can only talk to you. Claude Code can actually *do* things: open a CSV, write a Python script, run it, see the output, and iterate. You watch it work in a terminal window. It asks before doing anything risky.

## How it's different from ChatGPT (or Claude.ai)

| | Browser chatbot | Claude Code |
|---|---|---|
| Where it runs | Anthropic's / OpenAI's servers | Your laptop |
| What it can see | Only what you paste | Files in the folder you started it from |
| What it can do | Write text back to you | Read, write, edit, run files; install software; use git; talk to the web |
| Who has your data | Whichever company you use | The model sees only what it touches; nothing else leaves your machine unless you let it |
| When you'd use it | Quick questions, drafting, brainstorming | Actually building or changing something on your computer |

You **still need a chatbot** for most quick questions. Claude Code is for when you want the AI to *do* something concrete — modify a spreadsheet, build a dashboard, generate a report from data, refactor a file.

## The mental model: a junior analyst at your desk

Imagine you hired a sharp, fast junior analyst. They sit next to you. You say:

> "Open the patient pilot CSV. Tell me how ER visits compare to last year, broken out by clinic."

They open the file. They poke around. They write a small script. They run it. They show you the answer. If you say *"now color the chart by age group"* they go back, change the script, and re-run it.

**That's Claude Code.** Same loop. Same iteration. The terminal is just where you watch them work.

## What it can see on your computer

By default Claude Code only sees the **folder you started it in.** Not your whole laptop. Not other folders. Not your photos.

- It can read files in that folder.
- It can write files into that folder.
- It can run commands — but on anything risky (installing software, deleting files, sending to the internet) **it asks first.** You approve or deny each one.

If you want to keep something out of its reach, keep it out of that folder. That's it.

## What it cannot do (be honest)

- **Read your mind.** Vague prompts get vague answers.
- **Always be right.** It hallucinates less than older models but still does. You verify. Always.
- **Replace knowing what's worth building.** That's still you.
- **Operate other apps for you.** It can't click around in Excel or Epic. It works with files and code.

## How it gets used

You type into a terminal window. The conversation looks like this:

> **You:** Read the patient data and summarize the columns.
> **Claude:** *[reads the CSV]* The dataset has 250 patients across 6 clinics, with engagement, clinical, and utilization columns. Here are the most important ones…
> **You:** Build a chart of ER visits by clinic.
> **Claude:** *[writes a Python script, runs it, opens the chart]* Here's the chart. Lakeshore is the clear leader; Westgate is flat.
> **You:** Save that as a PNG and put it in a folder called `reports`.
> **Claude:** *[creates the folder, saves the file]* Done. The file is at `reports/er_visits_by_clinic.png`.

You don't write code. You describe. It does.

## Cost

- The **Claude Pro subscription** is roughly **$20/month** (USD) — generous for normal use. Most people stay under the included limits.
- **Heavier use** (long sessions, big projects) uses up the included quota faster; you can upgrade to a higher-tier plan or pay per-use via the API.
- For a healthcare admin trying it out a few hours a week, $20/month is the right starting point.

Pricing changes; check [anthropic.com/pricing](https://anthropic.com/pricing) for current numbers.

## What's safe to give it, what isn't

| Safe | Be careful | Don't |
|---|---|---|
| Synthetic data | De-identified summaries | Real patient data, real PHI/PII |
| Public documents | Internal but non-sensitive docs | Anything covered by HIPAA, financial PII, secrets |
| Your own writing | Org-internal drafts | Material that breaks NDAs |
| Code, configs | Vendor proposals (check NDA) | Passwords, API keys, certificates |

When in doubt: **ask your compliance officer.** The right answer is org-specific.

**Practical rule of thumb:** if you'd be uncomfortable pasting it into a customer-facing email, don't paste it into a chatbot. If you must work with sensitive data, ask your IT team about Claude through Bedrock, Vertex, or a HIPAA-eligible Enterprise plan — those have data-handling guarantees consumer Claude doesn't.

## How to start, Monday morning

1. **Install Claude Code.** Instructions at [docs.claude.com/en/docs/claude-code](https://docs.claude.com/en/docs/claude-code). Five minutes.
2. **Pick a small, real task.** Not "build me an EHR." Something like: *"Look at this spreadsheet of last month's no-shows and tell me what patterns you see."*
3. **Make a new folder** (or `git init` an existing one) and start Claude Code from inside it.
4. **Have one conversation.** Notice when you say things clearly and it does what you want, vs. when you're vague and it guesses wrong.
5. **Iterate.** The 10th task is much easier than the 1st.

## Things to read after this

- The official docs: [docs.claude.com/en/docs/claude-code](https://docs.claude.com/en/docs/claude-code)
- Anthropic's overview of AI safety + responsible use: [anthropic.com](https://anthropic.com)
- A reasonable "what is a coding agent?" primer: search for *"Simon Willison Claude Code"* — he writes clearly about this for non-engineers
- This repo's own [`01-analyze-the-data.md`](01-analyze-the-data.md) and [`02-build-the-dashboard.md`](02-build-the-dashboard.md) — they ARE the practical Monday-morning starter you're looking for

## The thing to remember

Claude Code is **not magic**. It's a fast, patient, never-tired junior analyst who reads, writes, and runs code on your machine, **with your permission, at your direction.** The skill is the same skill you already have: knowing what you want, describing it clearly, and checking the result.
