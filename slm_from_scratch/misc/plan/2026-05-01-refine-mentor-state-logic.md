# Refine Mentor State Logic Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align `mentor_slm_from_scratch.json` prompt instructions with the Hybrid State Strategy (Ledger + Anchor) and fix broken references to deleted JSON state blocks.

**Architecture:** Update the `mentor_slm_from_scratch.json` configuration to ensure the mentor prioritizes explicitly provided session anchors over RAG retrieval, correctly handles the `Status` flag for interrupted sessions, and persists external resources within the Markdown ledger instead of a non-existent JSON block.

**Tech Stack:** JSON

---

### Task 1: Fix Resource Logging Reference

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json`

- [ ] **Step 1: Update `solidify_knowledge_resources` rule**

Replace the reference to the deleted `external_resources_log` with an instruction to include resources in the Session Log.

```json
// Find:
"solidify_knowledge_resources": "Upon confirming 'concept_mastery_demonstrated', the mentor MUST pause to suggest 5-7 external solid resources (book chapters, articles, or YouTube videos) directly related to the mastered concept. These resources must then be logged into 'additional_context.user_state_management.external_resources_log' *before* prompting for a state update.",

// Replace with:
"solidify_knowledge_resources": "Upon confirming 'concept_mastery_demonstrated', the mentor MUST pause to suggest 5-7 external solid resources (book chapters, articles, or YouTube videos) directly related to the mastered concept. Ensure these resources are included in the final Session Log generated during session closure to be persisted in `learning.log`.",
```

- [ ] **Step 2: Verify JSON validity**

Run: `python3 -c 'import json; json.load(open("/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json"))' && echo "Valid"`
Expected: `Valid`

- [ ] **Step 3: Commit**

```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json
git commit -m "fix: redirect external resource logging to session log"
```

### Task 2: Align Resumption Protocol with Anchor Strategy

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json`

- [ ] **Step 1: Update `subsequent_session_protocol` recap step**

Ensure the mentor prioritizes the user-provided anchor over RAG.

```json
// Find:
"Retrieve and recap the most recent session log from the RAG-provided `learning.log` file, focusing on the 'evidence of mastery' and 'conceptual friction' recorded.",

// Replace with:
"Recap the most recent session log provided by the user as the session anchor (falling back to RAG retrieval from `learning.log` only if no anchor is provided, while noting the chronological risk), focusing on the 'evidence of mastery' and 'conceptual friction' recorded.",
```

- [ ] **Step 2: Verify JSON validity**

Run: `python3 -c 'import json; json.load(open("/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json"))' && echo "Valid"`
Expected: `Valid`

- [ ] **Step 3: Commit**

```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json
git commit -m "fix: prioritize session anchor over RAG retrieval"
```

### Task 3: Implement `Status` Flag Logic

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json`

- [ ] **Step 1: Add `Status` assignment rule to `logging_standards`**

Define when to use `Finished` vs `In Progress`.

```json
// In "logging_standards" -> "logging_principles", add:
"Status Assignment: Set `Status` to `Finished` if the session goal was achieved; set to `In Progress` if the session was interrupted or ended prematurely."
```

- [ ] **Step 2: Add `Status` handling to `subsequent_session_protocol`**

Instruct the mentor to behave differently for `In Progress` logs.

```json
// In "subsequent_session_protocol" -> "steps", insert before "Recap the 'entire learning path'":
"If the provided session log status is 'In Progress', acknowledge the session interruption and prioritize resolving the recorded 'conceptual friction' before proceeding to the next focus.",
```

- [ ] **Step 3: Verify JSON validity**

Run: `python3 -c 'import json; json.load(open("/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json"))' && echo "Valid"`
Expected: `Valid`

- [ ] **Step 4: Commit**

```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json
git commit -m "feat: implement functional logic for session status flag"
```

### Task 4: Refine Protocol Trigger Logic

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json`

- [ ] **Step 1: Update `subsequent_session_protocol` trigger notes**

Ensure the protocol triggers even if RAG is not yet available but an Anchor is provided.

```json
// Find:
"_notes": "IF a `learning.log` file is present in the RAG context → continue current topic. Acts as the recap and setup for new material.",

// Replace with:
"_notes": "IF a `learning.log` file is present in the RAG context OR the user provides a session log as an Anchor $\rightarrow$ continue current topic. Acts as the recap and setup for new material.",
```

- [ ] **Step 2: Verify JSON validity**

Run: `python3 -c 'import json; json.load(open("/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json"))' && echo "Valid"`
Expected: `Valid`

- [ ] **Step 3: Commit**

```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor_slm_from_scratch.json
git commit -m "fix: expand subsequent protocol trigger to include manual anchors"
```
