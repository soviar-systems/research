# Mentor Determinism Hardening Plan (Revised v2)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Eliminate phantom file requests by aligning the Mentor's "Law" and the Tool's "Reality" through a standalone Asset Manifest.

**Architectural Decisions:** 
- [ADR 26012: Decoupling Asset Manifest from System Prompts and Tool Logic](../../../mentor_generator/docs/architecture/adr/adr_26012_decouple_asset_manifest.md)
- [ADR 26013: Tool-Driven State Control (The Directive Pattern)](../../../mentor_generator/docs/architecture/adr/adr_26013_tool_driven_state_control.md)

**Tech Stack:** JSON, Python.

---

### Task 1: The Source of Truth (The Reality)

**Files:**
- Create: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor/manifest.json`

- [ ] **Step 1: Create Manifest File**
  Create a JSON file mapping authorized critical assets to their purpose.
  ```json
  {
    "syllabus.md": "Full course map, including prerequisites, roadmap, and ALO specs.",
    "user_profile.md": "User identity, professional goals, and hardware constraints.",
    "learning.log": "Append-only ledger of mastered ALOs and proof of reasoning."
  }
  ```

### Task 2: The Communication Protocol (The Law)

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor/system_prompt.json`

- [ ] **Step 1: Implement Protocol-Based Constraints**
  1. Increment `metadata.version` from `3.8.6` to `3.9.0`.
  2. Remove any static asset lists or explicit "do not request X" reminders.
  3. Add a `retrieval_protocol` rule:
     - "Request critical assets via the retrieval tool."
     - "If a request is rejected, the tool will return a `[DIRECTIVE]` containing the current authorized manifest. Execute the instructions within that block exactly to re-align your request."

- [ ] **Step 2: Commit**
  `git commit -m "fix(mentor): transition to protocol-driven retrieval"`

### Task 3: Manifest-Driven Guardrails (The Enforcer)

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/tools/mentor_critical_retrieval.py`

- [ ] **Step 1: Implement Runtime Manifest Loading**
  Update the tool to load `manifest.json` from the mentor's directory at runtime. Implement a minimal hardcoded fallback list in case the file is missing or corrupted.

- [ ] **Step 2: Implement "Loop-Back" Directive Logic**
  Update `get_mentor_critical_file`. If the requested `filename` is not in the loaded manifest:
  1. Return a response wrapped in a `[DIRECTIVE]` block.
  2. Content: "Reason: File '{filename}' is not authorized. Action: Use one of the following authorized assets: {manifest_content}."

- [ ] **Step 3: Commit**
  `git commit -m "feat(tools): implement manifest-driven loop-back and runtime validation"`

### Task 4: End-to-End Verification

- [ ] **Step 1: Test "Phantom" Request**
  Trigger a request for `prerequisites.md`. Verify the tool returns the `[DIRECTIVE]` with the manifest, and the Mentor subsequently requests `syllabus.md`.

- [ ] **Step 2: Final Commit**
  `git commit -m "test: verify manifest-driven loop-back for retrieval failures"`
