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
- Create: `../../../mentor_generator/templates/mentor_core/manifest.json`

- [ ] **Step 1: Create Manifest File**
  Create a JSON file mapping authorized critical assets to their purpose. 
  
  ⚠️ **CRITICAL NOTE:** The following list is a **Proposed Taxonomy**. It must be carefully reviewed and discussed to ensure all necessary mentor artifacts are covered without introducing security risks. **Do not treat this as a final specification until architectural sign-off.**

  ```json
  {
    "core": {
      "syllabus.md": "Full course map, including prerequisites, roadmap, and ALO specs.",
      "user_profile.md": "User identity, professional goals, and hardware constraints (Evolvable).",
      "mentor_failures.md": "Distilled ledger of past mistakes to avoid."
    },
    "progress": {
      "learning.log": "Append-only ledger of mastered ALOs and proof of reasoning.",
      "course_history": "Raw history of all learning sessions."
    },
    "mastery": {
      "ALOS/phase_1.md": "Deterministic verification criteria for Phase 1.",
      "ALOS/phase_2.md": "Deterministic verification criteria for Phase 2.",
      "ALOS/phase_3.md": "Deterministic verification criteria for Phase 3."
    },
    "verification": {
      "submissions/": "Authorized directory for student code submissions and exercise artifacts."
    }
  }
  ```
  *Note: For the tool implementation, the manifest will be flattened or traversed to validate the requested filename.*

### Task 2: The Communication Protocol (The Law)

**Files:**
- Modify: `../../slm_from_scratch/mentor/system_prompt.json`

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
- Modify: `../../tools/mentor_critical_retrieval.py`

- [ ] **Step 1: Implement Runtime Manifest Loading**
  Update the tool to load `manifest.json` from the Blueprint Unit (`mentor_generator/templates/mentor_core/`) at runtime. Implement a minimal hardcoded fallback list in case the file is missing or corrupted.

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
