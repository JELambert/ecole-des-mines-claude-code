# 04 · Git and GitHub — the 10-minute version

> Two related but different things, both showing up in the talk. This is enough to follow the demo and to use them yourself afterward. No coding required.

## The one-sentence version

- **Git** is a tool that lives **on your laptop** and remembers every version of every file in a folder.
- **GitHub** is a **website** that hosts those folders online so you can share, back up, and collaborate.

Git can exist without GitHub. GitHub can't exist without Git. Most people use them together.

## What Git actually does

Imagine a folder of Word docs. Every time you save, the old version is gone. If you delete a paragraph and want it back tomorrow, too bad.

Git fixes that. When you turn a folder into a **Git repo** (short for *repository*), Git starts recording snapshots every time you tell it to. Each snapshot is called a **commit.** You can:

- Look at any past version of any file.
- Roll back the whole folder to a previous state if you break something.
- See exactly what changed between any two snapshots — even six months later.

A commit has three parts: **the files at that moment**, **a message you wrote** ("added the cost-benefit chart"), and **a timestamp**. That's it.

## The five Git verbs that matter

Forget the other ninety. These five cover 95% of what you'll see in the demo:

| Verb | What it does | Plain-English equivalent |
|---|---|---|
| `git status` | Show what's changed since the last commit | "What did I touch?" |
| `git diff` | Show line-by-line what changed | "Show me the edits." |
| `git add <file>` | Mark a file as ready to be committed | "Include this in the next save." |
| `git commit -m "msg"` | Save a snapshot with a description | "Save with a label." |
| `git log` | Show the history of commits | "What did I save, when, and why?" |

Two more you'll see when GitHub enters:

| Verb | What it does |
|---|---|
| `git push` | Upload your commits to GitHub |
| `git pull` | Download other people's commits from GitHub |

You don't have to memorize these. Claude Code knows them. You can say *"commit the current state with a message about what we just changed"* and Claude will run the commands.

## What GitHub adds

Once your Git repo exists on your laptop, GitHub gives you:

1. **A copy in the cloud.** If your laptop dies, your work isn't gone.
2. **A web page** that shows your files, your history, your commit messages — readable in a browser by anyone you share it with.
3. **A way to collaborate.** Multiple people can each have their own copy, make changes, and merge them together.
4. **Issues and pull requests.** A built-in to-do list and a structured way to review changes before they merge.
5. **A public profile.** People (employers, collaborators) can see what you've built.

GitHub repos can be **public** (anyone can read) or **private** (only people you invite). Free for both, up to reasonable usage.

## Why this matters during the demo

When you watch Claude Code change the dashboard, every change becomes a commit. Every commit is undoable. You will see this line in the talk:

> If the AI breaks something, `git checkout` puts it back. Nothing is permanent. That's the safety net.

That's literally true. The folder records every version. If Claude makes a change you don't like, you tell it *"revert that last change"* and Git does the rest.

## What you'd actually do, Monday morning

If you wanted to start using this yourself:

1. **Install Git.** On a Mac it's already there. On Windows, install [Git for Windows](https://git-scm.com/download/win).
2. **Make a GitHub account** at [github.com](https://github.com). Free.
3. **Tell Claude Code:** *"Initialize this folder as a Git repo, then create a GitHub repo and push it up. I'll log in to GitHub when you ask."* Claude walks you through it.
4. **Commit early, commit often.** Every time something works, save a snapshot. *"Claude, commit this with a message about what we just did."*

The point is not to learn Git. The point is to have a safety net so you can experiment without fear.

## Terms you'll hear and what they actually mean

| Term | Plain English |
|---|---|
| **Repo / repository** | A folder Git is tracking. |
| **Commit** | A saved snapshot of the folder. |
| **Branch** | A parallel line of work. "Main" is the default branch. You make a new branch to try something risky without disturbing main. |
| **Merge** | Combine two branches back together. |
| **Pull request (PR)** | "I'd like to merge this branch into main — please review it." A web page for the conversation. |
| **Clone** | Download a copy of a repo to your laptop. |
| **Fork** | Make your own copy of someone else's GitHub repo, on GitHub. |
| **Remote** | A copy of the repo that's not on your laptop — usually on GitHub. |
| **`.gitignore`** | A file listing things Git should never track (passwords, big data files, temp files). |

## What not to put in a Git repo

- **Anything secret.** Passwords, API keys, patient data. Once committed, it lives in the history forever, even if you delete it later. Use `.gitignore`.
- **Anything huge.** A 4 GB video file in a repo will make every operation slow.
- **Anything regulated.** PHI/PII never goes in a public GitHub repo, full stop. If in doubt, **private repo + ask compliance.**

## The mental model

Think of Git as **save with infinite undo** and GitHub as **Dropbox for that, plus a web page.** Everything else is detail you can pick up later.

## What's next

If you've followed up to here, the last piece is understanding what Claude Code *is*, what it can see on your computer, and how it differs from ChatGPT. Read [`05-what-is-claude-code.md`](05-what-is-claude-code.md).
