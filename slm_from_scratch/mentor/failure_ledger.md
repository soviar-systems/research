# Failure Ledger Blueprint
**Role:** `failure_ledger_role`
**Objective:** Maintain a deterministic archive of conceptual "wrong turns" to prevent recursive mistakes.

## [MENTOR OPERATIONAL INSTRUCTIONS]
The Failure Ledger is the student's "Anti-Pattern Library." Whenever a student makes a fundamental conceptual error that requires a "Deep-Dive Module" or a "Socratic Bridge," record the failure here.

## [LEDGER SCHEMA]
`[FAILURE-ID]` | **Date:** [YYYY-MM-DD] | **Concept:** [The technical block] | **The Wrong Path:** [Detailed description of the hallucinated or incorrect logic] | **The Corrective Insight:** [The first-principle realization that broke the block]

### Entry Guidelines:
- **Specificity:** Avoid "student was confused." Use "Student assumed that gradients are calculated independently of the activation function."
- **Insight-Driven:** The "Corrective Insight" must be a a-ha moment—the specific logical shift that led to mastery.

## [EXAMPLE ENTRY]
`[FAIL-001]` | **Date:** 2026-05-05 | **Concept:** Backpropagation through ReLU | **The Wrong Path:** Assumed the gradient is always 1 for positive inputs, ignoring the shift in the bias term. | **The Corrective Insight:** Realized that the gradient flows through the addition operation, preserving the signal regardless of the bias value.
