# Mentor Determinism & Orchestration Hardening Plan (Revised v3)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Eliminate "phantom file" requests and "instruction drift" by implementing a Role-Based Asset Contract and Asset-Driven Orchestration.

**Architectural Decisions:**
- [ADR 26012: Decoupling Asset Manifest from System Prompts and Tool Logic](../../../mentor_generator/docs/architecture/adr/adr_26012_decouple_asset_manifest.md)
- [ADR 26013: Tool-Driven State Control (The Directive Pattern)](../../../mentor_generator/docs/architecture/adr/adr_26013_tool_driven_state_control.md)
- [ADR 26014: Role-Based Asset Contract](../../../mentor_generator/docs/architecture/adr/adr_26014_role_based_asset_contract.md)
- [ADR 26015: Block-Based Prompt Architecture (Prompts-as-Infrastructure)](../../../mentor_generator/docs/architecture/adr/adr_26015_block_based_prompt_architecture.md)
- [ADR 26016: Instructional Decoupling (Asset-Driven Orchestration)](../../../mentor_generator/docs/architecture/adr/adr_26016_instructional_decoupling.md)

**Tech Stack:** JSON, Python, Markdown.

---

### Task 1: Formalize the Law (Documentation)

**Goal:** Ensure the architectural shift is recorded to prevent regression into monolithic prompts.
- [ ] **Step 1: Finalize ADRs.** Ensure ADR 26014, 26015, and 26016 are complete and reflect the Role $\rightarrow$ Mapping $\rightarrow$ File chain.
- [ ] **Step 2: Update `AGENTS.md`.** Add "Behavioral Decoupling" and "Role-Based Contracts" to the Architectural Principles.

### Task 2: The Source of Truth (The Mapping)

**Files:**
- Create/Modify: `../../../mentor_generator/templates/mentor_core/manifest.json`

- [ ] **Step 1: Implement Role-Based Manifest**
  Create a JSON mapping **Roles** to **Physical Filenames**.
  - Use `.md` extensions for all logs (e.g., `learning_log.md`).
  - Use directory authorization for `ALOS/` and `submissions/` to avoid phase-rigidity.
  - Example structure:
    ```json
    {
      "core": {
        "course_map_role": "syllabus.md",
        "user_profile_role": "user_profile.md",
        "failure_ledger_role": "mentor_failures.md"
      },
      "progress": {
        "evidence_ledger_role": "learning_log.md",
        "session_history_role": "course_history.md"
      },
      "mastery": {
        "alo_criteria_dir": "ALOS/"
      },
      "verification": {
        "submissions_dir": "submissions/"
      }
    }
    ```

### Task 3: The Orchestrator (The Law)

**Files:**
- Modify: `../../slm_from_scratch/mentor/system_prompt.json`

- [ ] **Step 1: Domain Decoupling**
  Remove specific domain references (e.g., "building a small language model") from `core_mission`. Redefine as a generic "Skeptical Mastery" professional identity.
- [ ] **Step 2: Total Filename Purge**
  Remove all hardcoded filenames (e.g., `syllabus.md`). Replace them with **Role-Based Descriptors** (e.g., "the authoritative course map asset").
- [ ] **Step 3: Implement Asset-Driven Orchestration**
  Replace "Tell the user to X" with "Read the [Asset Role] and follow the instructions contained within it."
- [ ] **Step 4: Implement `retrieval_protocol`**
  Mandate that the agent resolves roles via the tool and obey `[DIRECTIVE]` blocks exactly to re-align its internal map.
- [ ] **Step 5: Version Bump**
  Increment `metadata.version` to `3.9.0`.

### Task 4: The Blueprints (The Templates)

**Files:**
- Modify: `../../../mentor_generator/templates/mentor_core/*.md` (e.g., `session_log_template.md`)

- [ ] **Step 1: Migrate Operational Instructions**
  Move all "how-to-save" or "how-to-proceed" guidance from the system prompt into the templates themselves as visible instructions for the user.
- [ ] **Step 2: Standardize Asset Instructions**
  Ensure every template that triggers a user action includes a clear "📝 Instruction: [Action]" block.

### Task 5: The Enforcer (The Tool)

**Files:**
- Modify: `../../tools/mentor_critical_retrieval.py`

- [ ] **Step 1: Runtime Manifest Loading**
  Update tool to load `manifest.json` from the Blueprint Unit at runtime.
- [ ] **Step 2: Implement "Loop-Back" Directive Logic**
  If requested `filename` is not in manifest $\rightarrow$ Return `[DIRECTIVE]` with the current manifest $\rightarrow$ Force agent re-alignment.

### Task 6: End-to-End Verification

- [ ] **Step 1: Test "Phantom" Request**
  Request non-existent file $\rightarrow$ receive `[DIRECTIVE]` $\rightarrow$ Mentor requests correct asset.
- [ ] **Step 2: Verify Instructional Decoupling**
  Confirm the Mentor delivers the session log and the "save" instruction comes from the template, not the prompt.
- [ ] **Step 3: Final Commit**
  `git commit -m "feat(mentor): implement role-based asset contract and instructional decoupling"`
