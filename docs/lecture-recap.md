##### 2026-05-22
##### ⬆️[[Incubating]]

# AI in Software Development with Claude Code — Lecture Recap, 2026-05-22

**Instructor:** Dr. Josh Lambert (FactSet / University of South Alabama)
**Setting:** Guest lecture, student cohort preparing for a digital-health hackathon
**Materials:** GitHub repo shared with all attendees (slides, synthetic dataset, walkthrough docs)

---

## Framing

This lecture was a live, hands-on tour of Claude Code — one of the leading AI-powered coding tools — aimed at students with little or no software engineering background. Josh's core argument: the bottleneck between your ideas and working software has been dramatically lowered. You no longer need to know how to code to build real, functional applications. What you *do* need is domain expertise, clear thinking about what you want, and a willingness to treat the AI like a collaborator rather than a search engine. The demo used a synthetic healthcare dataset (a fictional remote patient monitoring pilot) and ended with a fully functional interactive web dashboard — all without writing a single line of code by hand.

---

## Topics Covered

### 1. Who Josh Is (and why that matters for context)

- Manages several AI teams at FactSet, a financial data provider (hedge funds, banks, quant finance). His teams build AI solutions around graph deep learning, semantic layers, and knowledge systems.
- Visiting professor at the University of South Alabama teaching PhD-level ML and AI for business analytics.
- PhD from UCF (2020) in security studies — his dissertation used machine learning to predict political violence at local scales (civil-military change, regime change, violence against minority groups). More recently publishing in applied economics.
- Point: he's not a software engineer by training. He came at this from a domain-expert side, which is relevant to how he thinks about these tools.

### 2. The Shift in Software Development

- For decades, if you wanted an app built, you either paid an engineer or waited in a queue at work. The engineer was the bottleneck between ideas and execution.
- Transformer-based architectures (the neural net design behind ChatGPT, Claude, Gemini, etc.) have fundamentally changed this. Anyone can now be a productive software developer.
- What changed specifically: these models can read files on your computer, create new files, compile and run code, install dependencies, and fix their own errors. You're not writing code — you're *describing what you want* and staying in the loop to check results.
- The remaining gap: LLMs can't read your mind. You get out what you put in. "I want a dashboard" is not a prompt. "Here's the data, here's what a chief innovation officer needs to know before a board meeting, here are the three questions that matter most" — that's a prompt.

### 3. Context Is Everything

- LLMs need context the way a new hire needs onboarding. The more domain-specific information you give it, the better it performs.
- Your domain expertise is the thing that makes this powerful. You're the one who knows what questions to ask. The AI is the one who knows how to answer them at scale.
- Current professional practice is heavily about *context optimization* — figuring out how to fit the right information into the model's context window to get the best output.
- Don't trust blindly. Hallucinations happen, just like people make mistakes. Build in checkpoints.

### 4. The Demo: Sentinel Health RPM Pilot (Synthetic Healthcare Dataset)

The scenario: you're a chief innovation officer. You've got four weeks to decide whether to scale or sunset a remote patient monitoring program. The data is in a CSV (250 patients, 6 clinic sites, 26 variables). Your questions:

- Are ER visits and hospitalizations actually down compared to last year?
- Which clinic sites are performing? Which aren't?
- Is the ROI there?

Josh walked through the following steps live in Claude Code:

**Step 1 — Get oriented**
Prompt Claude Code to read the CSV and give a plain-language summary of what's in it. This seeds the model with context before you start asking real questions. Result: 250 patients, enrollment dates 2025–2026, clinical outcome variables (A1C for diabetes, systolic BP for hypertension, etc.), six clinic sites.

**Step 2 — Compute headline numbers**
Ask for the six key metrics Maya (hypothetical analyst) would put on a one-page memo: total enrolled, currently active, overall ER reduction, etc. Claude Code wrote and ran Python to calculate these. You don't need to understand the code. The output flagged something interesting: the ER reduction figure of -34% sounds great, but the post-enrollment period covers only a fraction of 12 months while the pre-period is a full 12 months — a comparison problem worth surfacing.

**Step 3 — Break down by clinic site**
"Show me ER reduction and hospitalization reduction broken out by clinic site." Claude wrote more Python, ran it, returned a table. Westgate Clinic showed 0% change, which stood out.

**Step 4 — Economics**
Asked for cost-benefit / ROI analysis. Result: -14% ROI — the program saved $218K but cost $252K to run. Three sites are profitable; three are losing money.

**Step 5 — Collect everything into a report**
"Make a results folder, collect all the analysis in there, generate a formatted PDF." Claude created the folder, wrote a markdown report, converted to PDF, and handled its own dependency failures (no LaTeX? figured it out without being asked).

**Step 6 — Build an interactive dashboard**
The demo culminated with building a multi-page Streamlit web app. Josh asked for graphs, filters, download buttons, counterfactual analysis via a spawned research agent, and a plan before execution (plan mode). The result was a functional app with:
- Enrollment status overview
- ER/hospitalization reduction by clinic
- Cost-benefit / ROI page
- Clinical outcomes page (filterable)
- Download buttons for graphs (PNG) and tables (CSV)

All of this without writing any code. Claude installed Streamlit itself when it found it missing.

### 5. Plan Mode

- Shift-Tab in Claude Code toggles "plan mode."
- In plan mode, the model produces a detailed plan (file structure, pages, data flows) *before* doing any coding. You review it, suggest edits, and then approve.
- Works the same way for humans: thinking before doing produces better results. Worth using on anything non-trivial.
- After approval, you can say "auto-approve all Python" so it doesn't pause to ask permission for each code block.

### 6. Multi-Agent Orchestration

- Most people think of AI as a one-to-one interaction: you ask, it answers. That's the floor, not the ceiling.
- You can "spawn" additional agents. In the demo, Josh spawned a research agent that explored the dataset independently and surfaced counterfactuals and questions no one had asked yet. The main agent and research agent talked to each other.
- No hard limit on agents. Josh routinely runs 10–20 agents on a single task, across multiple terminal windows/tabs, each potentially running 10–20 sub-agents. "At any given time, there could be 200 LLMs working for me."
- More agents = more tokens used = more cost. But often better final output.
- The skill that's emerging as most valuable in software engineering is not coding a single file — it's *orchestrating agents across many domains simultaneously*, managing their direction, and synthesizing their outputs.

### 7. Model Selection and Costs

Three major CLI providers:
| Provider | CLI Name |
|---|---|
| Anthropic | Claude Code |
| OpenAI | Codex |
| Google | Google CLI |

All have roughly similar capability for most tasks. Josh's preference is Claude for general productivity, but:
- Google's image generation ("Imagen" — he called it "Nano Banana" in passing, probably Imagen 3) is better than Claude's (which has none for photorealistic images) or ChatGPT's.
- Python and SQL are the sweet spots for all of them — heavily represented in training data. Obscure languages (e.g., Lisp) will be noticeably worse.
- Open-source models are also available and can be layered in for cost control.

Subscription costs (approximate at time of lecture):
- Minimum: ~$20/month. At this tier, you'll burn through tokens quickly on a capable model.
- ~$100/month: hard to exhaust unless you're running many agents across many tabs.
- API billing: pay per token. During the demo, the displayed token cost was ~$0.02, but Josh mentioned his work account had run up ~$450 in token cost on a single day — not his actual bill since it's bundled into a subscription.

### 8. Interfaces: CLI vs. Desktop App

- CLI (command line / terminal): closer to the operations, fewer abstraction layers, Josh's preference.
- Desktop GUI apps: all three providers have them. More approachable if the terminal is intimidating. Also have folder access and similar capability.
- Pick whichever lets you actually get things done.

### 9. MCPs and What Josh's Team Actually Builds

- MCP (Model Context Protocol) is essentially an API standard for giving LLMs access to external tools and data sources.
- Example: hook up an MCP for Gmail, and Claude can now read, draft, and send emails from that account (within whatever permissions you set).
- Josh's team at FactSet builds knowledge graphs over ontologies and taxonomies to give LLMs structured access to complex, distributed financial data. The problem: a natural language question like "give me lithium-ion battery sentiment from SEC filings for this sector" maps to dozens of tables across AWS, Google, Databricks — each with unique column names and entity IDs. The team builds systems that translate intent into structured queries.
- The leap from "one CSV today" to "ten thousand tables across three cloud providers" is where this kind of infrastructure becomes necessary.

### 10. Voice Input and Prompting Style

- Josh uses voice-to-text apps (specifically mentioned Handy and Hearty — both free, noted as working really well; also mentioned Whisper Flow as a paid option that's marginally better but not enough to bother with) to interact with LLMs.
- When you type, you compress — you try to say as much as possible in as few words as possible. That's bad for LLMs, which need to hear how you're thinking.
- "Even if you say 'I'm thinking about this, but never mind, actually I like this better' — that's good context. The model is hearing your reasoning process."
- Talking out loud to the LLM the way you'd talk through a problem with a colleague is one of the most effective prompting strategies.

### 11. Workflow Automation and AI as a Career Reality

Josh closed with a broader point:

- He has AI triage his email daily, manage his to-dos, transcribe all his meetings, and flag his top priorities after each call.
- The question isn't whether AI will change your industry — it will. The question is whether *you're* the one augmenting your workflow with it.
- "People that use AI are going to be the ones that succeed. People that aren't using AI in a lot of cases just aren't going to be able to keep up."
- This isn't "AI takes jobs." It's "people who use AI replace people who don't."

### 12. Security and "Clean System" Strategy

- Running autonomous agents on your main machine carries risk — privacy, security, accidental file changes.
- Many practitioners use a "clean system" — a dedicated machine (e.g., a Mac Mini) with nothing sensitive on it. If an agent goes rogue, worst case you reinstall the OS. No lost passwords, no exposed private data.
- This is why Mac Minis are selling — cheap, capable, disposable dev boxes.

---

## Q&A

**What does it cost to run all these tokens? It keeps going up at the bottom of the screen.**
Josh noted that the token cost counter at the bottom is a custom add-on he had built (not native to Claude Code), and it had a bug during the demo. On the substantive question: token cost depends on the model, whether you're using sub-agents, and your plan. On a subscription you get a pool of usage for a flat monthly fee. API billing is per-token. At the $100/month tier, it's difficult to run out unless you're running many concurrent agents across multiple sessions. His work account logged ~$450 in token cost on a single day — but that's against a bundled enterprise agreement, not an out-of-pocket charge.

**Is there a way to see all running agents in one place, or do you have to ask them to report back?**
Not really — at this stage the tooling doesn't aggregate running agents across windows. Each terminal tab has its own view of what's running. You'd have to check tabs individually. The providers do track total usage (you can see your monthly consumption percentage in the app), but live agent inventory across sessions isn't a solved problem yet.

**What file types can Claude Code create? Does "no image generator" limit the output?**
Claude can create essentially any file type. Common useful ones: Markdown, JSON, PDF (via conversion), HTML, Python scripts, SQL, CSV, PNG/JPEG (graphs generated via Python libraries like matplotlib). What it *can't* do is generate photorealistic images ("show me a cat on a tricycle"). For that, Google Imagen is better. But charts, diagrams, architecture diagrams, web designs — all available.

**What if I want the dashboard to stay live and update automatically when new data comes in?**
"Take exactly what you just asked and put it into Claude Code." Seriously — just describe the requirement. Claude will propose an architecture for connecting to a live database or real-time data source and you say yes. You don't need to design it yourself. Real-time data pipelines are a solved problem in code; you just need to tell it that's the goal.

**I'm a biologist and you said "never trust, always verify" — can we actually ask the AI to check itself, and have multiple models check each other?**
Yes, and this is a legitimate production strategy. Within a single session, you can ask Claude to explain how it coded something, review its own analysis, and flag errors — and it will sometimes catch its own mistakes. For higher-stakes applications, practitioners use a "harness" (a plan-evaluate-plan cycle) where the LLM loops back and pressure-tests its own output. The most rigorous approach: run Claude, OpenAI, and Google CLI against the same problem and have them challenge each other's answers. You get small but meaningful variations in reasoning, and the intersection is usually the most reliable output. Cost and time tradeoff, but it's worth it for anything high-stakes.

**Could Claude replace the AI chatbots that social media businesses use for customer service and automation?**
Probably for some use cases, not all. When LLMs first came out, a lot of companies built bespoke chatbots by wrapping an LLM with their own data. The major labs have grown fast enough to put some of those wrapper businesses out of business — their general-purpose models are simply better. But there will still be niches where specialized, fine-tuned, brand-specific products make sense. That said: we are seeing consolidation. The frontier labs have structural advantages that are hard to compete with.

**What about transcription apps — which one do you use?**
Handy and Hearty (both free, both good). Whisper Flow if you want to pay — marginally better, not enough to matter. The transcription quality on all of these has improved dramatically recently, which Josh attributed to... transformer-based architectures, unsurprisingly.

**Someone mentioned Fire.ai — do you use it?**
Familiar with it but hasn't really used it. (Questioner described it as something that helps filter the signal from the noise across the crowded AI tools landscape.)

**Can you tie it to synthetic data the way Julia described — use LLM-generated practice data to debug your model, then reserve the real 20% for final validation?**
Exactly right. Synthetic data generation is one of the best LLM use cases. You give it context about the distribution and domain ("I want a dataset that looks like it comes from a clinical trial, normally distributed, some variance across sites") and it generates something statistically plausible that you can work with before touching real data. De-risks the pipeline, lets you find bugs cheaply.

---

## Tools, Libraries, and Resources Mentioned

| Name                             | What it is                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Claude Code**                  | Anthropic's CLI for AI-assisted development. Primary tool of the demo.                                                                                             |
| **Codex**                        | OpenAI's equivalent CLI.                                                                                                                                           |
| **Google CLI**                   | Google's equivalent CLI.                                                                                                                                           |
| **Streamlit**                    | Python library for building interactive web dashboards. Very low barrier.                                                                                          |
| **Git / GitHub**                 | Version control + cloud hosting for code. Used to distribute the demo materials. `git clone <url>` to download a repo.                                             |
| **Python**                       | The programming language Claude Code ran for all calculations. You don't need to write it; the LLM does.                                                           |
| **MCP (Model Context Protocol)** | Standard for connecting LLMs to external tools and APIs (Gmail, databases, etc.).                                                                                  |
| **Markdown / JSON**              | File formats LLMs work with naturally — lightweight, open, well-represented in training data.                                                                      |
| **Handy**                        | Free voice-to-text app for macOS. Josh's preferred transcription tool.                                                                                             |
| **HEX**                          | Another free voice-to-text option. Also recommended.                                                                                                               |
| **Whisper Flow**                 | Paid voice-to-text. Marginally better than the free options; probably not worth it for most.                                                                       |
| **Imagen (Google)**              | Google's image generation model ("Nano Banana" mentioned in passing — likely Imagen 3). Better than ChatGPT's for photorealistic images; Claude has no equivalent. |
| **Claude Design**                | New Claude product for graphical/UI design work, mentioned briefly.                                                                                                |
| **Stack Overflow**               | Developer Q&A forum; heavily represented in LLM training data, which is why Python/SQL perform so well.                                                            |
| **LaTeX / WeasyPrint**           | PDF conversion dependencies. Claude handled installing them automatically when they were missing — mentioned as an example of offloading dependency management.    |
| **Mac Mini**                     | Mentioned as a popular "clean system" dev box — cheap, capable, disposable.                                                                                        |
| **Josh's Substack**              | Mentioned but not named — writes about AI and other topics. Connect for follow-up content.                                                                         |
| **FactSet**                      | Josh's employer; financial data platform serving hedge funds, investment firms, banks.                                                                             |

---

## Key Takeaways

- **You don't need to code to build software.** You need to describe what you want clearly, provide domain context, and stay in the loop to verify results. The LLM handles the code.
- **Context quality is your main input variable.** Short vague prompts produce mediocre output. Give the model your domain knowledge, your constraints, your questions, and your goals.
- **Never trust blindly.** LLMs hallucinate. Build in checkpoints, ask the model to explain its reasoning, have it check itself. Always verify outputs that will be used for real decisions.
- **Synthetic data is a first-class use case.** Before you touch real (messy, protected, incomplete) data, use an LLM to generate plausible synthetic data to test your pipeline.
- **Multi-agent orchestration is where the ceiling is.** One agent is a tool. Ten agents working in parallel under your direction is a force multiplier. Learning to orchestrate — not just prompt — is the skill that separates good from great.
- **Tedious work should not exist in your workflow.** Installing libraries, formatting reports, copy-pasting results, managing dependencies — these are agent tasks. If you're doing them yourself, you're leaving leverage on the table.
- **AI augments the people who use it.** The coming shift isn't "AI replaces jobs." It's "people who use AI replace people who don't." Start finding where it fits your workflow now, before the gap widens.

---

## Glossary

**CLI (Command Line Interface)** — Any application you run from a terminal window, by typing commands. Claude Code, Git, Python — all CLIs. Not as scary as it looks; the demo showed the full workflow.

**GUI (Graphical User Interface)** — The visual desktop apps you're more used to (buttons, menus, windows). Claude, ChatGPT, and Gemini all have GUI desktop apps as alternatives to their CLIs.

**LLM (Large Language Model)** — The underlying AI model type (GPT-4, Claude 3, Gemini, etc.). Built on transformer architecture; trained on massive amounts of text including code, research, and the internet.

**Transformer architecture** — The neural network design that powers modern LLMs. Introduced in the 2017 "Attention Is All You Need" paper; underlies essentially every major AI tool in use today.

**Token** — The unit LLMs process text in (roughly 3/4 of a word). Token usage determines API cost and model context limits.

**Context window** — How much text a model can "hold in memory" at once. Fitting the right information into the context window efficiently is a core engineering challenge.

**MCP (Model Context Protocol)** — A standard that lets LLMs connect to external tools, APIs, and databases. Think of it as giving the AI hands to reach into Gmail, Slack, SQL databases, etc.

**Plan mode** — A Claude Code setting (Shift-Tab) that forces the model to generate a step-by-step plan *before* doing any work. Review and edit the plan before execution begins.

**Synthetic data** — Data generated by an LLM to simulate a real dataset, with plausible distributions and structure but no real individuals. Useful for prototyping before real data is available or appropriate.

**Streamlit** — A Python library that turns data scripts into interactive web apps with minimal additional code. Very popular for dashboards and internal tools.

**ETL (Extract, Transform, Load)** — The data engineering process of pulling raw data from sources, cleaning/reshaping it, and loading it into a database or analysis tool. Mentioned as a painful step that synthetic data lets you skip in early prototyping.

**Hallucination** — When an LLM confidently states something that is factually incorrect. Not rare enough to ignore. Always verify important claims.

**Harness** — An evaluation loop where an LLM (or multiple LLMs) plans, executes, evaluates its own output, and repeats. Used to pressure-test results and catch errors automatically.

**Orchestration** — Managing multiple AI agents working in parallel on different parts of a task, directing them, resolving conflicts, and synthesizing their outputs. Described as the highest-leverage skill in modern AI-assisted software development.

**Knowledge graph / ontology** — Structured representations of relationships between entities (people, companies, concepts, financial instruments). Josh's team builds these to give LLMs the scaffolding needed to query complex databases accurately.
