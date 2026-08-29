---
name: game-design-documentation
description: Establish, restructure, maintain, audit, or export a complete game project design-document system. Use when Codex needs to create a reusable GDD framework, consolidate scattered design notes into authoritative chapters, define design ownership and data-table boundaries, track decisions and open questions, create a new project's planning-document skeleton, or prepare a coherent design package for review or PDF delivery.
---

# Game Design Documentation

Build a traceable design system, not a single oversized document.

## Start

1. Inspect the live workspace before assuming files, engine, genre, team, or version scope.
2. Read `references/framework.md` for the chapter map and authority hierarchy.
3. Read `references/workflow.md` for authoring, review, change, and delivery gates.
4. Read `references/role-standards.md` when system, combat, level, narrative, UI, art, audio, engineering, production, or QA ownership matters.
5. Read `references/profiles-and-templates.md` when choosing document depth, running gameplay experiments, creating a Feature Contract, or preparing a discipline-specific delivery surface.
6. If no document system exists, select the smallest adequate profile and run `scripts/scaffold_gdd.py <project-root> --title "<title>" --profile <concept|prototype|vertical-slice|production>`; use `--language en` for English output.

## Operating rules

- Treat the chapter files as the authoritative product/design baseline.
- Put rules and rationale in prose documents; put tunable values and content rows in data tables.
- Keep one authoritative source for each fact. Link to it rather than duplicating it.
- Use the canonical status IDs in `references/framework.md`; localized labels are display equivalents, not separate states.
- Remove stale uncertainty after a decision is made; update every affected chapter, table, and risk entry.
- Preserve the user's approved scope. Keep future compatibility as a boundary, not an automatic deliverable.
- State MVP inclusions and exclusions explicitly.
- Define internal versus outsourced ownership when production responsibility is in scope.
- Record assumptions when project inputs are missing; do not invent dates, budgets, staffing, platform commitments, or content counts.

## Workflow

1. Inventory existing documents, tables, diagrams, builds, and decision records.
2. Establish the product baseline: audience, fantasy, pillars, loop, platform, session, camera, input, mode, MVP, and exclusions.
3. Resolve contradictions and select one authoritative statement for each rule.
4. Create or update only the profile-appropriate chapters. Treat the 20-chapter structure as the complete production map, not a mandatory starting payload.
5. Add system specifications only when a feature can be implemented and accepted independently.
6. Define data schemas after the rules stabilize; keep concrete balancing values out of prose when a table is authoritative.
7. Add observable acceptance criteria and risks to every production-ready area.
8. For uncertain gameplay, record a hypothesis and evidence in the experiment log before promoting it to `[Confirmed]`.
9. Run the audits in `references/workflow.md`.
10. Export only the requested delivery surface. For PDF, use the PDF skill and render every page for visual QA.

## Deliverables

Prefer a versioned project index plus the smallest chapter set needed by the selected profile. Add only resources the project needs:

- `PROJECT_DESIGN_DOCUMENT_INDEX.md`
- profile-selected `CHAPTER_*.md` files; use all 20 only for a production-complete document system
- system specifications for independently implementable features
- configuration workbook or schemas
- decision log, risk register, test cases, and change log
- experiment log and Feature Contracts when hypotheses or cross-discipline implementation need traceability
- consolidated PDF when requested

Do not silently mix research memos, role standards, obsolete drafts, or implementation notes into the formal GDD. Reference them from the index under separate headings.
