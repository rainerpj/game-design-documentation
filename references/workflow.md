# Authoring, Review, and Delivery Workflow

## 1. Discovery gate

Inventory existing documents and determine:

- product owner and approvers;
- current build/prototype evidence;
- target platform, audience, mode and session;
- team, budget, schedule and outsourcing facts actually supplied;
- authoritative documents versus drafts, research, notes and obsolete versions;
- contradictions and missing decisions.

Output a short baseline and contradiction list before large-scale rewriting.

Keep research findings, product decisions, prototype experiments, implementation notes, and acceptance evidence as separate authority layers.

## 2. Product gate

Complete chapters 1, 2, 15 and 19 first. A viable baseline states:

- player promise and three to five pillars;
- core loop and progression boundary;
- MVP inclusions and exclusions;
- measurable prototype/vertical-slice/MVP exit criteria;
- assumptions, risks, owners and decision deadlines.

Do not expand content production until these chapters agree.

## 3. Rules gate

Complete chapters 4-11. For each system answer:

- what the player observes and decides;
- input, preconditions, rules, states and outputs;
- ownership and interaction with other systems;
- failure, resource exhaustion, duplicate triggers, full inventory, save/load and disconnect behavior;
- presentation and accessibility signals;
- MVP depth and explicit deferrals;
- measurable acceptance criteria.

When the rule is still experience-dependent, create an experiment record with a hypothesis, observable measure, guardrails, retained comparison version, and adoption rule. Do not present the prototype direction as confirmed merely because it is playable.

## 4. Implementation gate

Complete chapters 12-17 and system specifications. Before implementation:

- dependencies have owners and states;
- minimum test content can be configured;
- presentation triggers are defined;
- normal, failure and boundary test cases exist;
- authority, persistence, randomness and migration boundaries are explicit;
- performance budgets have target hardware/scenes or are marked as decisions, not invented.

## 5. Production gate

Before batch content production:

- a prototype proves the core experience;
- one complete content example passes cross-discipline review;
- schema is frozen or has a migration plan;
- asset specifications, naming, ownership and acceptance are explicit;
- capacity and outsourcing assumptions are documented;
- measured performance and content cost replace estimates.

## 6. Change process

When a decision changes:

1. Re-read live files.
2. Update the authoritative source.
3. Find downstream references, tables, tests, risks, saves and assets.
4. Remove stale `[To Decide]` or `[To Prototype]` language.
5. Record rationale, impact, migration and approval.
6. Re-run consistency checks.

For a Feature Contract change, trace the same ID through chapters, specifications, schemas, configuration, implementation tasks, tests, assets, saves/migrations, risks, and requested delivery surfaces. Preserve an old playable version when it is still comparison or acceptance evidence.

## 7. Consistency audit

Check that:

- chapters 1, 2 and 15 promise the same product;
- controls agree across chapters 2, 4, 5 and 12;
- resources agree across chapters 5, 7, 8 and 9;
- world/run flow agrees across chapters 2, 10 and 11;
- content counts agree across chapters 6-8, 10, 13 and 15;
- technical constraints support rules in chapters 4-11;
- milestones and tests cover every MVP feature;
- risk and decision entries are not stale;
- tables, prose and tests do not own conflicting values.
- experiments promoted to `[Confirmed]` have updated their authoritative rule, while rejected directions are absent from active UI, configuration, tests, and delivery bundles;
- Feature Contract IDs resolve to one design authority and the expected implementation, data, acceptance, and evidence surfaces.

## 8. Delivery audit

- Maintain an index with recommended reading paths by discipline.
- Keep formal chapters separate from standards, research and obsolete drafts.
- Use stable, descriptive filenames and a visible version/date.
- Verify links and referenced artifacts.
- For PDF: include cover, contents, bookmarks, page numbers and source/version note; render every page and inspect tables, clipping, fonts and chapter transitions.
