# Live-demo script (minute 25 → 45)

> Goal: show Claude Code extending the dashboard end-to-end. ~20 minutes of stage time. Three reps of the loop: ask → plan → act → verify.

## Pre-stage (do before walking on)

1. Terminal open, full-screen, font size cranked (≥18pt). Prompt clean.
2. Dashboard already running in a separate browser tab — `localhost:8501`.
3. `cd dashboard` already done.
4. Claude Code launched, sitting at empty prompt.
5. Phone on tether, wifi off as primary.
6. Three fallback recordings open in QuickTime, paused at frame 0:
   - `docs/fallback-recordings/01-filter.mov`
   - `docs/fallback-recordings/02-trend.mov`
   - `docs/fallback-recordings/03-crosstab.mov`

## The three asks (pick one — let audience choose)

### A. "Add a filter by category to the sidebar"
- Easiest. Three-line change in `components/filters.py`.
- Run-time risk: low. Default fallback.

### B. "Chart the trend of <metric> over time, broken down by category"
- Medium. Touches `components/charts.py`; needs a `color=` kwarg + grouping.
- Most visually interesting result.

### C. "Add a third tab with a crosstab of category × region"
- Hardest. Touches `app.py` (new layout) + new component.
- Best showcase if everything's going well.

## Patter (≈ what I'm saying while it runs)

**Opening line:**
> "I want you to see what I see when I work this way. I'm going to ask Claude Code to extend this dashboard, in front of you, against the same code you can see on screen."

**While Claude reads:**
> "Notice it's reading first. It doesn't write before it knows what's there. This sounds obvious, but watch it — it's pulling in `app.py`, then the loader, then the component. That's the same pass *I* would make if I were doing this by hand."

**While Claude edits:**
> "Now it edits. Each change is a diff. Nothing is opaque. If you're skeptical of AI tools — and you should be — this is what to demand of them: that you can see exactly what changed."

**While Claude runs:**
> "Now it's running it. It just discovered the same thing I would have if I'd tested manually. Notice it's about to fix it without me telling it."

**Wrap:**
> "Total elapsed time: ~6 minutes for an end-to-end feature. The point isn't the feature. The point is the *workflow*. This is what I mean by 'building with Claude Code' — you stay in the loop, you stay in control, but the mechanical work moves off your plate."

## If it fails (decision tree)

| Symptom | Action |
|---|---|
| Claude Code times out / no response in 15s | Cut to fallback video; "let's look at one I prepared" |
| Claude Code edits but the app doesn't run | Show the error in terminal; if fixable in <2 min, fix it live. If not → fallback video |
| Network drops entirely | "Demo gods are angry today" → play fallback video. Same talking points still work |
| Wrong file edited | Show the diff; revert with `git checkout`; explain why this is the safety net of working in a repo |

## Don't do

- Don't make this about **prompting**. Treat the prompt as ordinary instruction.
- Don't apologize for what the model can't do. Show it doing what it *can*.
- Don't read the screen aloud. Audience can read.
- Don't oversell. The strongest move is letting them see *normal* work happen fast.
