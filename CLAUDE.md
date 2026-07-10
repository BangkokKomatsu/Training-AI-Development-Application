# CLAUDE.md

Context file for working on this repo in future sessions.

## What this repo is

Training material for **"AI Application Development: Build Your First Mini AI Agent with Microsoft Foundry"** (BKC internal course). See `README.md` and `COURSE_OUTLINE.md` for the full outline.

Current structure:
- `docs/00-09` — lecture content (Foundry concept, API key/token, prompt engineering, setup, security, + bonus: advanced prompting, multi-turn, function calling)
- `workshops/lab-01` to `lab-07` — hands-on labs with `starter.py` / `solution.py` (Lab 6-7 are bonus/advanced: multi-turn chatbot, function calling)
- `workshops/colab/bkc_ai_workshop.ipynb` — **Track A** single Colab notebook (Setup + Lab 1-4 + Mini Challenge), pre-filled cells with one `# ✏️` edit point each
- `slides/course-slides.md` — Marp deck for the technical **Track B** (VS Code + local Python)
- `slides/course-slides-colab.md` — Marp deck for **Track A** (Colab-led, non-IT-friendly)
- `sample-data/` — factory issues (non-confidential mock data)

The Lab 1-7 `.py` files + `course-slides.md` are the **technical / "Track B"** path: VS Code + Python + Azure OpenAI SDK, aimed at people comfortable writing/running code.

**Model note (verified 2026-07):** BKC's deployment is **`gpt-5-mini`**, which on Azure OpenAI **rejects `temperature` and `max_tokens`** (use `max_completion_tokens` or omit; omit `temperature`). The Track A materials already account for this — precision is taught via prompt + JSON mode, not Temperature. The Track B `.py` labs and `course-slides.md` may still reference `temperature`/`max_tokens` and need the same fix if run on gpt-5-mini.

---

## Planned: "Track A" — AI course for non-IT staff

### Why a separate track

Most people interested in this training are **not IT** — they work in Purchasing, QA, HR, Finance, Admin, etc. The existing Track B (raw Python + API calls) is too technical as an entry point for them. They only get a Foundry API key during the training session itself (no ongoing ChatGPT/Copilot access afterward, as of now).

### Decided direction — BUILT (confirmed 2026-07-10)

Concrete audience for the next run: **~50 people, ~5 IT / ~45 non-IT**, 10:00–16:00.

Delivery decisions (locked):
- **Google Colab is the primary runtime** (browser, zero local install) — kills ~80% of setup failures for non-IT. Local `.py`/Streamlit kept as an option for the ~5 IT people = **dual-track**.
- **Fill-in-the-blank:** cells pre-filled, learners just press Run and edit ONE marked spot per lab (`# ✏️`, usually the prompt or input). They do NOT write code from scratch.
- **Teaching flow (user's preference):** explain concept on slides → walk through Colab code → run together, in short cycles per topic. NOT git-following, NOT live-coding from scratch.
- **Lab 3 (Streamlit) and Lab 4 (Excel/try-except) are demo-led** for non-IT; protect deep hands-on for Lab 1, 2, and the Mini Challenge (where the transferable prompt skill lands).
- Ops: **3 TAs** roam + hand-raise; ~5 IT participants seeded as table buddies. **One shared API key** for all 50 → don't run all at once (avoid 429), request higher TPM, Thai try-except messages, rotate key after.

Built deliverables:
1. `workshops/colab/bkc_ai_workshop.ipynb` — the fill-in-the-blank Colab notebook (replaces the earlier `mini_agent.py` idea)
2. `slides/course-slides-colab.md` — Track A Marp deck (includes Prompt Cheat Sheet + "Round 2 > Round 1" prompt-refinement slide)

### Still open / not built
- "Prompt Gallery" as a separate printed handout of 5 ready-made templates (the notebook has inline templates instead — build the handout only if the user wants a paper takeaway)
- Facilitator run-sheet (minute-by-minute instructor script) — offered, not yet built
- Department-specific sample data beyond the factory examples

### Additional activity ideas discussed (pick & choose, not all needed)

**Engagement / icebreaker**
- "Be the AI" pair exercise — one person writes a prompt on paper, the other follows it literally (no computer) — teaches why prompt wording matters
- "Before/After Prompt" live demo — same input, vague prompt vs well-designed prompt, side by side

**Critical thinking / security (ties into `docs/06-security-checklist.md`)**
- "Spot the Hallucination" — show a confident-but-wrong AI output, have participants find the error
- "Can I paste this into AI?" quiz — real-ish examples (price, resume, defect photo) → yes/no + why

**Skill-building**
- "Round 2 is better than Round 1" — iterative prompting / refining via follow-up chat turns instead of rewriting the whole prompt (useful skill that transfers to ChatGPT/Copilot)
- Translation / tone-adjustment exercise for emails to overseas suppliers (high relevance for Procurement)

**Department relevance**
- Department-specific sample input data (Maintenance, QA, Production, HR, Admin) so the exercises feel relevant to each audience

**Take-home value**
- "Prompt Cheat Sheet" — 1-page reference (Role/Task/Rules/Output formula + the 5 gallery prompts) participants can keep and reuse with ChatGPT/Copilot after the course
- "AI Toolbox Map" — 1-pager showing which AI tools BKC staff actually have access to and when to use which
- "Action Card" — each participant commits to one real recurring task they'll try AI on within a week

### Next step when resuming this work

Core Track A hands-on + slides are DONE (see "Built deliverables" above). Remaining options, if the user wants them:
1. Facilitator run-sheet (minute-by-minute instructor script) — the natural next step
2. "Prompt Gallery" paper handout + "AI Toolbox Map" / "Action Card" take-home pieces
3. Selected bonus activities (icebreaker "Be the AI", "Spot the Hallucination", department-specific sample data)
4. Verify the Colab notebook end-to-end against BKC's real gpt-5-mini deployment before the session
