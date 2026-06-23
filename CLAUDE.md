# CLAUDE.md

Context file for working on this repo in future sessions.

## What this repo is

Training material for **"AI Application Development: Build Your First Mini AI Agent with Microsoft Foundry"** (BKC internal course). See `README.md` and `COURSE_OUTLINE.md` for the full outline.

Current structure:
- `docs/00-09` — lecture content (Foundry concept, API key/token, prompt engineering, setup, security, + bonus: advanced prompting, multi-turn, function calling)
- `workshops/lab-01` to `lab-07` — hands-on labs with `starter.py` / `solution.py` (Lab 6-7 are bonus/advanced: multi-turn chatbot, function calling)
- `slides/course-slides.md` — Marp slide deck for the full-day technical course (Track B below)
- `sample-data/` — supplier issues & IT tickets (non-confidential mock data)

This existing course (Lab 1-7 + slides) is the **technical / "Track B"** path: VS Code + Python + Azure OpenAI SDK, aimed at people comfortable writing/running code.

---

## Planned: "Track A" — AI course for non-IT staff

### Why a separate track

Most people interested in this training are **not IT** — they work in Purchasing, QA, HR, Finance, Admin, etc. The existing Track B (raw Python + API calls) is too technical as an entry point for them. They only get a Foundry API key during the training session itself (no ongoing ChatGPT/Copilot access afterward, as of now).

### Decided direction (from discussion)

- **Not** a fully no-code Streamlit-only experience — the user wants participants to write *some* code, but it should be mostly **copy-paste**.
- Approach: **"Fill-in-the-blank with ready-made prompts"**
  - One pre-built, complete script `mini_agent.py` (boilerplate: API client, JSON parsing, pretty print — fully working, nothing to debug)
  - Participants edit only two variables by copy-pasting:
    - `PROMPT_TEMPLATE` — picked from a printed/slide "Prompt Gallery" (5 ready-made templates: Supplier Issue Analyzer, IT Ticket Classifier, Document Completeness Checker, Email Draft Generator, Meeting Notes → Action Plan)
    - `INPUT_TEXT` — their own (non-confidential) real-work text
  - Run `python mini_agent.py` → see formatted result immediately
- This mirrors/simplifies the existing Lab 5 "Mini Challenge" but removes the open-ended prompt-design burden — prompts are provided ready-made.

### Not yet built (still brainstorming / not prioritized)

Deliverables identified but **not started**:
1. `mini_agent.py` — the boilerplate script described above
2. "Prompt Gallery" handout — the 5 ready-made prompt templates, copy-paste formatted
3. New slide deck / agenda for Track A (lighter than Track B — skip deep API Key/Endpoint mechanics)

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
- Department-specific sample input data (HR, Finance, Admin — not just Supplier/IT) so the exercises feel relevant to each audience

**Take-home value**
- "Prompt Cheat Sheet" — 1-page reference (Role/Task/Rules/Output formula + the 5 gallery prompts) participants can keep and reuse with ChatGPT/Copilot after the course
- "AI Toolbox Map" — 1-pager showing which AI tools BKC staff actually have access to and when to use which
- "Action Card" — each participant commits to one real recurring task they'll try AI on within a week

### Next step when resuming this work

Ask the user to prioritize which of the above activities to include, then build in this order:
1. `mini_agent.py` + Prompt Gallery (core hands-on)
2. Track A agenda/slide deck
3. Selected bonus activities (cheat sheet, toolbox map, etc.)
