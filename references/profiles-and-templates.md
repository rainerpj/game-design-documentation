# Profiles and Templates

Choose the smallest document profile that supports the current decision and delivery. Expanding a profile adds authority surfaces; it does not automatically expand product scope.

## Document profiles

### Concept

Use for early framing before implementation commitment. Create chapters 1, 2, 15, and 19 plus the index and decision log.

### Prototype

Use for a playable hypothesis. Start with Concept, add the chapters that own the tested mechanic, chapter 17, an experiment log, and at least one system specification or Feature Contract.

### Vertical slice

Use for one production-representative end-to-end experience. Start with Prototype and add chapters 12-14 and 16, plus any content chapters required by the slice.

### Production

Use when a complete cross-discipline baseline is genuinely required. Create the full 20-chapter map and the applicable companion records.

## Experiment record

Keep research, experiments, approved rules, and implementation notes separate.

```markdown
# Experiment <ID>: <name>

- Status: [To Prototype]
- Related authority and feature ID:
- Hypothesis:
- Player decision or experience being tested:
- Prototype surface and version/entry point:
- Variables held constant:
- Success, failure, and guardrail measures:
- Test cases and audience:
- Evidence:
- Result: adopt / revise / reject / inconclusive
- Authority updates required:
- Old version retained or migration needed:
- Owner and date:
```

Promote a result to `[Confirmed]` only after updating its authoritative chapter/specification. Retain rejected directions with rationale, but do not leave them active in formal rules or configuration.

## Cross-discipline Feature Contract

Use the same ID in design, engineering tasks, data, handoffs, tests, and evidence.

```markdown
# Feature Contract <ID>: <name>

- Product/design authority:
- Target version and canonical status:
- Player value and intended decision:
- Rules and invariants:
- Included / excluded:
- Preconditions, states, transitions, interruption, recovery:
- Definition data and content owner:
- Runtime/authority owner:
- UI and presentation triggers:
- Persistence, networking, randomness, migration:
- Debug and telemetry surface:
- Given/When/Then acceptance matrix:
- Required evidence surface:
- Open decisions, owner, deadline, fallback:
- Downstream documents, tables, tests, assets, and delivery surfaces:
```

The design authority defines what and why. Implementation documents define where and how. Evidence records prove the agreed observable result; none should duplicate the authoritative rule text.

## Delivery surfaces

- **Product/lead review:** promise, pillars, scope, major decisions, evidence, risks.
- **Design package:** authoritative chapters, system specifications, data ownership, experiment outcomes.
- **Engineering handoff:** Feature Contracts, schemas, states, edge cases, acceptance and migration.
- **Art/audio/vendor brief:** asset purpose, specification, source/license, dependencies, owner, budget and acceptance capture.
- **QA package:** build/version boundary, Given/When/Then cases, telemetry, target environment and known exclusions.
- **Investor/external summary:** approved positioning, scope, plan, assumptions and risks; keep forecasts and commercial models outside product-rule authority.

Generate these as views of the authority system. Do not create competing copies of rules merely to suit another audience.
