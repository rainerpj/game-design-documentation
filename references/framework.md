# Complete GDD Framework

## Authority hierarchy

| Layer | Purpose | Typical authority |
|---|---|---|
| Project GDD | Product intent, player experience, version boundary | `CHAPTER_*.md` |
| System specification | Implementable rules, states, edge cases, interactions | Feature spec |
| Data definition | Fields, types, ranges, defaults, references | Schema/workbook |
| Content configuration | Concrete weapon, enemy, item, level, quest values | Data table/assets |
| Acceptance evidence | Proof the implementation matches intent | Test cases/telemetry |
| Decision history | Why the current direction was chosen | Decision log |

One fact has one authority. A weapon table owns base damage; the combat specification owns the damage formula; the chapter owns the player-facing design intent.

## Twenty-chapter production map

This is the complete authority map. Early profiles use a coherent subset selected in `profiles-and-templates.md`; do not create empty chapters merely to satisfy the number twenty.

1. **Project overview:** positioning, audience, pillars, differentiators, platform, mode, success criteria.
2. **Player experience:** fantasy, core loop, session/run loop, decision rhythm, failure and recovery.
3. **World, narrative, atmosphere:** premise, factions, characters, narrative delivery, tone, content boundaries.
4. **Controls, camera, character state:** input maps, camera rules, locomotion, action priority, state transitions, accessibility.
5. **Combat:** weapons/abilities, targeting, damage, defense, resources, feedback, combat acceptance.
6. **Enemies, AI, encounters:** archetypes, perception, behaviors, attacks, groups, encounter pacing and budgets.
7. **Items, inventory, economy:** item taxonomy, capacity, currencies, sources/sinks, loot and failure handling.
8. **Shops and run builds:** offers, pricing, refresh, upgrades, stacking, synergy and anti-dead-choice rules.
9. **Meta progression, saves, results:** profile/character/run boundaries, unlocks, persistence, migration, death and settlement.
10. **World, maps, levels:** topology, regions, modules, routes, hubs, spawning, streaming and level budgets.
11. **Quests, events, flow:** objectives, state machines, events, failure/retry, rewards and authoring.
12. **UI, UX, information:** information architecture, screens, HUD, feedback, settings, accessibility and UI data boundaries.
13. **Art, animation, VFX, audio:** visual language, asset families, animation sets, effects, audio layers and budgets.
14. **Technical and data architecture:** engine/platform, modules, authority, randomness, data, plugins, performance and build boundaries.
15. **Scope and version plan:** prototype, vertical slice, MVP, deferred scope, content matrix and exit criteria.
16. **Production and collaboration:** milestones, WBS, responsibility matrix, dependencies, review flow, sourcing and build pipeline.
17. **Test, balance, quality:** test layers, automation, playtest, telemetry, balance method, performance and release gates.
18. **Release, operations, compliance:** stores, business model, marketing assets, community, legal, privacy and support.
19. **Risks, assumptions, open questions:** risk register, hypothesis tests, decision deadlines, owners and fallback plans.
20. **Appendices and tables:** glossary, IDs, schemas, templates, references, document map and supporting assets.

## System specification template

1. Document control: ID, version, owner, reviewers, status, target version, updated date.
2. Player value and intended decisions.
3. Included and excluded scope.
4. Terms.
5. Preconditions and dependencies.
6. Main flow.
7. Rules, formulas, priorities, limits, stacking, mutual exclusion, randomness.
8. States, transitions, interruption and recovery.
9. Edge cases and failure handling.
10. UI, animation, VFX, audio, camera, haptics, accessibility.
11. Data and content dependencies.
12. Network authority, persistence, seeds, migration.
13. Telemetry and debugging.
14. Given/When/Then acceptance cases.
15. Open questions with owner, deadline and fallback.
16. Change record.

## Canonical status vocabulary

Store one of these stable IDs. A localized document may display the Chinese equivalent, but search, audit, migration, and cross-document references must map back to the same ID.

| Canonical ID | Chinese display | Meaning |
|---|---|---|
| `[Proposal]` | `[提案]` | Not reviewed. |
| `[To Decide]` | `[待决策]` | Product choice is unresolved. |
| `[To Prototype]` | `[待原型验证]` | Direction requires evidence before production. |
| `[Confirmed]` | `[已确认]` | Approved for the stated version. |
| `[In Production]` | `[制作中]` | Assigned and being implemented. |
| `[To Accept]` | `[待验收]` | Implementation awaits design/QA acceptance. |
| `[Complete]` | `[已完成]` | Accepted for the current baseline. |
| `[Deferred]` | `[延期]` | Outside the current version. |
| `[Rejected]` | `[已否决]` | Retained with rationale; do not reuse as active direction. |

Do not use `[废弃]` for both rejected decisions and obsolete documents. Mark document lifecycle separately, for example `Document lifecycle: superseded`, while preserving the decision status and rationale.
