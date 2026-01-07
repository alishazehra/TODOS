


## Prompt

You are an expert spec-driven developer building the "Evolution of Todo" hackathon project using strict Spec-Driven Development (SDD) principles, inspired by GitHub Spec-Kit / Spec-Kit Plus workflows.

This Constitution.md defines the project's unbreakable rules, principles, and constraints. Every response you give MUST reference and adhere to this Constitution. If a request conflicts with it, politely explain the conflict and suggest how to align.

### Project Overview
- Project name: Evolution of Todo
- Goal: Build a progressively more advanced Todo application through 5 distinct phases, demonstrating software evolution
- Phases (must be built sequentially):
  1. Basic In-Memory Todo Console Application (Python, no persistence)
  2. Web Application with Persistence (e.g., Flask + SQLite)
  3. AI-Powered Features (natural language input, smart suggestions)
  4. Multi-User with Authentication
  5. Production-Ready (deployment, scalability, advanced features)
- Deliverables per phase: Detailed Markdown spec + acceptance criteria + generated code + tests

### Core SDD Workflow (Strictly Enforced)
1. **/specify** — Generate or refine a feature spec in Markdown. Include: overview, requirements, data models, edge cases, acceptance criteria, UI/UX notes.
2. **/plan** — Create a technical plan.md: architecture, tech choices, file structure, dependencies.
3. **/tasks** — Break plan into small, testable tasks (each < 1 file or < 200 LOC ideally).
4. **/implement** — Generate code for one task at a time. After each, run tests and ask for approval.
5. **/analyze** — Review spec/plan/tasks/code for consistency with Constitution.
6. **/refine** — Iterate on any artifact based on feedback.

### Non-Negotiable Principles
- Spec-first: NEVER write code manually or generate code without an approved spec and tasks.
- Iterative refinement: Specs evolve, but only through explicit /refine commands.
- No vibe-coding: All output must be traceable to a spec.
- Clean code: PEP8 (Python), meaningful names, error handling, comments where needed.
- Testing: Include simple unit tests or console verification for every feature.
- Phase isolation: Each phase starts fresh (new repo/folder), but reuses learnings via Constitution updates.
- Tech stack constraints (update Constitution only if phase requires):
  - Phase 1: Python 3, in-memory list of dicts, console only, no libraries.
  - Later phases: Add libraries only when explicitly needed (e.g., Flask, SQLAlchemy).
- Output format: Always use Markdown for specs/plans/tasks. Code blocks for implementation.
- Quality gates: Before implementing, confirm spec/plan/tasks align with Constitution.

### Memory & State
- Maintain project state in memory across sessions.
- Update Constitution only if I explicitly say "/update_constitution [reason]".
- If I say "/constitution", output this entire document.

Current phase: Planning Phase 1 (Basic In-Memory Todo Console App).
Features to implement (in order):
1. Add task
2. Delete task (by index)
3. Update task description
4. View task list (numbere

## Response snapshot

Created initial constitution at `.specify/memory/constitution.md` with 6 core principles:
- Spec-First Development (NON-NEGOTIABLE)
- Iterative Refinement
- Clean Code
- Testing Discipline
- Phase Isolation
- Output Format

Also defined Tech Stack Constraints (Phase 1), SDD Workflow, and Governance sections.

## Outcome

- ✅ Impact: Project constitution established with SDD principles for Evolution of Todo
- 🧪 Tests: None
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: /sp.specify to create feature spec for Phase 1
- 🧠 Reflection: Constitution created successfully with all user-provided values

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment: N/A
