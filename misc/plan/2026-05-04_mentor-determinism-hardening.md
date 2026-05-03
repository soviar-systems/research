# Mentor Determinism Hardening Plan (Revised)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Eliminate phantom file requests by aligning the Mentor's "Law" and the Tool's "Reality" through a shared Asset Manifest.

**Tech Stack:** JSON, Python.

---

### Task 1: Concise Asset Manifest (The Law)

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor/system_prompt.json`

- [ ] **Step 1: Implement Asset Manifest & Version Increment**
  1. Increment `metadata.version` in `system_prompt.json` from `3.8.6` to `3.9.0`.
  2. Add `asset_manifest` under `learning_framework` $\rightarrow$ `rules`. Use a simple mapping to avoid pollution.
  
  ```json
  "asset_manifest": {
    "syllabus.md": "Full course map, including prerequisites, roadmap, and ALO specs.",
    "user_profile.md": "User identity, professional goals, and hardware constraints.",
    "learning.log": "Append-only ledger of mastered ALOs and proof of reasoning."
  },
  "manifest_constraint": "Request ONLY files listed in the asset_manifest. Any other file request is a protocol failure."
  ```

- [ ] **Step 2: Remove Redundancies**
  Clean up the `syllabus_source_of_truth` rule by removing the explicit "do not request prerequisites.md" reminders. The manifest now handles this.

- [ ] **Step 3: Commit**
  `git commit -m "fix(mentor): replace negative constraints with concise asset manifest"`

### Task 2: Manifest-Driven Guardrails (The Tool)

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/tools/mentor_critical_retrieval.py`

- [ ] **Step 1: Sync Authorized Assets**
  Add a constant `AUTHORIZED_FILES` that mirrors the `asset_manifest` from the system prompt.
  
  ```python
  AUTHORIZED_FILES = ["syllabus.md", "user_profile.md", "learning.log"]
  ```

- [ ] **Step 2: Implement "Loop-Back" Error Logic**
  Update `get_mentor_critical_file`. If the requested `filename` is not in `AUTHORIZED_FILES`, return a response that points the mentor back to the manifest.
  
  ```python
  if filename not in AUTHORIZED_FILES:
      return {
          "content": f"Reason: File '{filename}' is not an authorized critical asset. Action: Use one of the following authorized files: {', '.join(AUTHORIZED_FILES)}."
      }
  ```

- [ ] **Step 3: Commit**
  `git commit -m "feat(tools): implement manifest-driven error handling to correct mentor behavior"`

### Task 3: End-to-End Verification

- [ ] **Step 1: Test "Phantom" Request**
  Trigger a request for `prerequisites.md`. Verify the tool returns the list of `AUTHORIZED_FILES` and that the Mentor subsequently requests `syllabus.md`.

- [ ] **Step 2: Final Commit**
  `git commit -m "test: verify manifest-driven loop-back for retrieval failures"`
