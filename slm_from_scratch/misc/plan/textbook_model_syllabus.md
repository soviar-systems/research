# [Textbook Model Syllabus] Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transition the syllabus from a simple list to a "Textbook Model" structured artifact (Executive Roadmap $\rightarrow$ Detailed Curriculum $\rightarrow$ ALO Specifications) to eliminate the "Conciseness Trap" and provide a repeatable template for future courses.

**Architecture:** We shift the `syllabus.md` from a general document to a structured data asset. The Mentor will no longer "synthesize" a roadmap but will "mirror" the pre-formatted "Detailed Curriculum" section. This decouples the internal calibration (using the whole syllabus) from the external presentation (mirroring the roadmap section).

**Tech Stack:** Markdown, JSON (System Prompt).

---

### Task 1: Create the Syllabus Blueprint

**Files:**
- Create: `mentor/syllabus_template.md`

- [ ] **Step 1: Write the template structure**
Define a template that enforces three distinct sections:
1. `# Executive Roadmap` (Table: Phase | Primary Goal | Estimated Time)
2. `# Detailed Curriculum` (Exhaustive list: Phase $\rightarrow$ Stage $\rightarrow$ ALO)
3. `# ALO Specifications` (Mapping: ALO ID $\rightarrow$ Required Proof of Mastery)

- [ ] **Step 2: Commit**
```bash
git add mentor/syllabus_template.md
git commit -m "docs: create syllabus_template.md for Textbook Model"
```

### Task 2: Refactor the Master Syllabus

**Files:**
- Modify: `mentor/syllabus.md`

- [ ] **Step 1: Implement "Executive Roadmap"**
Extract the "Goal" and "Estimated Time" for each of the 5 Phases into a high-level table at the top of the document.

- [ ] **Step 2: Implement "Detailed Curriculum"**
Move the existing Phase/Stage/ALO structure into this section. Ensure it is a flat, exhaustive list without summary.

- [ ] **Step 3: Implement "ALO Specifications"**
For every ALO (1.1 through 5.5), define the "Skeptical Mastery" criteria.
Example: `ALO 1.1: Proof = Correct implementation of linear sum in NumPy + explanation of weight geometry.`

- [ ] **Step 4: Commit**
```bash
git add mentor/syllabus.md
git commit -m "refactor: migrate syllabus.md to Textbook Model structure"
```

### Task 3: Align Mentor System Prompt

**Files:**
- Modify: `mentor/system_prompt.json`

- [ ] **Step 1: Update `first_session` Protocol Step 3**
Change "Syllabus Synchronization Audit" to explicitly command: "Retrieve the '# Detailed Curriculum' section from `syllabus.md` and report it verbatim."

- [ ] **Step 2: Update `syllabus_source_of_truth` rule**
Explicitly distinguish between internal calibration (using the whole file) and external presentation (mirroring the Detailed Curriculum section).

- [ ] **Step 3: Commit**
```bash
git add mentor/system_prompt.json
git commit -m "prompt: align system prompt with Textbook Model syllabus structure"
```

### Task 4: Update Project Documentation

**Files:**
- Modify: `ReadMe.md`
- Modify: `AGENTS.md`

- [ ] **Step 1: Update `ReadMe.md`**
Update the "Pedagogical Framework" to include the "Textbook Model" and "Architectural Decoupling" principles. Update the Roadmap table to refer to the `syllabus.md`'s Executive Roadmap.

- [ ] **Step 2: Update `AGENTS.md`**
Update the description of `syllabus.md` from "The Map" to "The Textbook Source of Truth (Executive Roadmap, Detailed Curriculum, and ALO Specifications)."

- [ ] **Step 3: Commit**
```bash
git add ReadMe.md AGENTS.md
git commit -m "docs: update ReadMe and AGENTS to reflect Textbook Model"
```

### Task 5: Real-World Verification

**Files:**
- Test: Deployment to production environment

- [ ] **Step 1: Deploy updated assets**
Deploy the updated `syllabus.md` and `system_prompt.json` to the real, clean environment (web-chat) where files are provided via RAG.

- [ ] **Step 2: Execute "First Session"**
Trigger the first session protocol and verify that the mentor retrieves and reports the `# Detailed Curriculum` section verbatim, without any summarization or omission.

- [ ] **Step 3: Verify "Skeptical Mastery" Gating**
Verify that the mentor correctly accesses the `# ALO Specifications` section to demand the specific proof of mastery for an ALO before allowing progression.

- [ ] **Step 4: Final Validation**
Confirm that the "Conciseness Trap" is eliminated in the real-world RAG environment.

---

**Plan complete and saved to `misc/plan/textbook_model_syllabus.md`. Two execution options:**

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
