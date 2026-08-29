# Game Design Documentation

A Codex skill for establishing and maintaining a traceable game design document system. It turns scattered design notes into an authority-based GDD structure without forcing every project to start with a full production document set.

## What it provides

- Four scalable documentation profiles: concept, prototype, vertical slice, and production.
- A chapter authority hierarchy with one authoritative source for each product rule.
- Boundaries between design prose, tunable data, implementation notes, and delivery artifacts.
- Feature Contracts, decision logs, risk registers, experiment records, and acceptance criteria.
- Review and delivery gates for coherent Markdown or PDF design packages.
- A scaffold script for creating the smallest adequate document system for a new project.

## Install

Clone the repository into the Codex skills directory:

```bash
git clone https://github.com/rainerpj/game-design-documentation.git "${CODEX_HOME:-$HOME/.codex}/skills/game-design-documentation"
```

Restart or reload Codex after installation. The skill supports automatic discovery and can also be invoked explicitly as `$game-design-documentation`.

This is currently a private repository, so cloning requires a GitHub account with repository access.

## Quick start

Ask Codex to establish, restructure, audit, or export a game design document system. For a new project, the bundled scaffold can create a profile-appropriate starting structure:

```bash
python scripts/scaffold_gdd.py <project-root> --title "My Game" --profile prototype
```

Available profiles are `concept`, `prototype`, `vertical-slice`, and `production`. Add `--language en` for English output.

## Repository structure

```text
game-design-documentation/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- framework.md
|   |-- workflow.md
|   |-- role-standards.md
|   `-- profiles-and-templates.md
`-- scripts/
    `-- scaffold_gdd.py
```

`SKILL.md` is the entry point. The files under `references/` define the documentation framework, workflow gates, discipline ownership, profiles, and reusable templates.

## Scope

This repository contains the reusable Codex skill only. It does not contain a specific game's GDD, production data, source code, assets, or exported delivery documents. Generated documents are written to the project root explicitly supplied by the user.

