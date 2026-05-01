# Mentor Prompt Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Purge remaining "echoes" of the old programmatic state-management system from `mentor_slm_from_scratch.json` to optimize the instruction budget and align with the RAG/log architecture.

**Architecture:** Remove dead configuration fields and simplify the session resumption protocol to move the LLM from "summary mode" (analysis) to "mentoring mode" (execution).

**Tech Stack:** JSON

---

### Task 1: Remove Dead System Constraints

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json`

- [ ] **Step 1: Delete `state_update_token_threshold`**

Remove the following line from `additional_context.constraints_and_strategy.system_constraints`:
`"state_update_token_threshold": 200000,`

- [ ] **Step 2: Commit**

```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json
git commit -m "chore: remove obsolete state_update_token_threshold from mentor prompt"
```

### Task 2: Simplify Session Resumption Protocol

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json`

- [ ] **Step 1: Remove full path recap**

In `session_resumption_protocol.session_protocols.subsequent_session_protocol.steps`, find and remove the step:
`"Recap the 'entire learning path' (briefly summarize staged_progression and current phase).",`

- [ ] **Step 2: Update orientation logic**

Replace the removed step with a more concise orientation:
`"Briefly confirm the current Phase and Stage to orient the session, then proceed to the anchor.",`

- [ ] **Step 3: Commit**

```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json
git commit -m "refactor: simplify session resumption by removing redundant full path recap"
```
