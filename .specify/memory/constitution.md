<!--
Sync Impact Report
==================
Version change: N/A → 1.0.0 (initial creation)
Modified principles: None (all new)
Added sections: 6 principles, 3 main sections, Governance
Removed sections: None
Templates requiring updates: ✅ All templates align with constitution
Follow-up TODOs: None
-->

# Evolution of Todo Constitution

## Core Principles

### I. Spec-First Development (NON-NEGOTIABLE)

Every feature MUST begin with an approved specification. NO code may be written without:
- A complete feature spec in Markdown (`specs/<feature>/spec.md`)
- An implementation plan (`specs/<feature>/plan.md`)
- A task breakdown (`specs/<feature>/tasks.md`)

All output MUST be traceable to a spec requirement. "Vibe-coding" is prohibited.

### II. Iterative Refinement

Specifications evolve through explicit refinement commands only:
- `/sp.refine` for spec modifications
- `/sp.plan` for architectural updates
- `/sp.tasks` for task adjustments

Implicit changes during implementation are not permitted. Any deviation requires a new refinement command.

### III. Clean Code

All code MUST adhere to quality standards:
- **Python**: PEP 8 compliance
- **Meaningful naming**: Variables, functions, and classes clearly convey intent
- **Error handling**: Graceful degradation with informative messages
- **Comments**: Explain WHY, not WHAT; document non-obvious logic

### IV. Testing Discipline

Every feature MUST include verification:
- Unit tests for core logic
- Integration tests for feature workflows
- Console verification for CLI-only applications

Tests MUST be written before implementation (Red-Green-Refactor).

### V. Phase Isolation

Each phase of the "Evolution of Todo" project is self-contained:
- Fresh repository/folder structure per phase
- Learnings propagate via Constitution updates
- Dependencies only added when phase requires them
- No backward compatibility requirements between phases

### VI. Output Format

All documentation MUST use Markdown:
- Specifications: `specs/<feature>/spec.md`
- Plans: `specs/<feature>/plan.md`
- Tasks: `specs/<feature>/tasks.md`
- Code: Proper syntax highlighting in fenced blocks

## Tech Stack Constraints

Phase 1 technology choices (subsequent phases may deviate):
- **Language**: Python 3.x
- **Storage**: In-memory list of dictionaries (no persistence)
- **Interface**: Console/CLI only
- **Dependencies**: Standard library only (no external packages)

Libraries MAY be added in later phases when explicitly required by feature specifications.

## SDD Workflow (Strictly Enforced)

1. **/sp.specify** — Generate feature spec with: overview, requirements, data models, edge cases, acceptance criteria, UI/UX notes
2. **/sp.plan** — Create technical architecture: tech choices, file structure, dependencies, interfaces
3. **/sp.tasks** — Break plan into testable tasks (each < 200 LOC, single file ideally)
4. **/sp.implement** — Generate code task-by-task; run tests after each; seek approval before continuing
5. **/sp.analyze** — Review all artifacts for constitution consistency
6. **/sp.refine** — Iterate on artifacts based on feedback

## Governance

This Constitution supersedes all other development practices. Amendments require:
1. Documentation of proposed change
2. Review and approval
3. Migration plan for affected artifacts

All PRs and reviews MUST verify compliance with these principles. Complexity MUST be justified.

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
