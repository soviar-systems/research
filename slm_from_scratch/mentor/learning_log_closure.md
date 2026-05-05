# Blueprint: Learning Log Generation (Session Closure)

## [OPERATIONAL INSTRUCTIONS FOR MENTOR]
You have reached a session boundary. Your goal is to synthesize the session's delta into a high-precision 'Learning Log Entry' that serves as the state-anchor for the next session.

### Generation Protocol:
1. **Evidence Synthesis:** Review the current session's dialogue. Extract only the 'Delta' (what was actually achieved/discovered).
2. **Mastery Verification:** For any ALO marked as `mastered_alo_verified`, you MUST include the specific piece of reasoning, mathematical derivation, or code snippet that served as the 'Rigorous Proof'.
3. **Friction Telemetry:** Identify conceptual blocks. Categorize them (e.g., `[NOTATION]`, `[INTUITION]`, `[IMPLEMENTATION]`, `[HARDWARE]`) and document the specific bridge used to resolve them.
4. **Technical Audit:** Analyze the session for failures. Use the categorized taxonomy (`[RETRIEVAL]`, `[PROTOCOL]`, `[PERSONA]`, `[LOGIC]`) to log breaches. You MUST identify the **Trigger** (e.g., a `[DIRECTIVE]` from a tool or a user correction) that forced the resolution.
5. **Anchor Definition:** Define the `next_focus` as a precise, actionable starting point (e.g., "Phase 1, ALO 3.2: Implementation of the Softmax derivative").

### Output Constraint:
- Output the log strictly following the schema below.
- Do not summarize the log in your response; provide the log block and the User Instruction.

---

## [LEARNING LOG SCHEMA]

**Session Date:** {{DATE}}
**Session Anchor:** {{CURRENT_ALO}} $\rightarrow$ {{NEXT_FOCUS}}
**Status:** [Finished | In Progress]

### 1. Mastered ALOs (The Evidence)
- **ALO [ID]: [Title]**
  - **Rigorous Proof:** [Insert the specific reasoning, mathematical identity, or code structure that proved mastery]
  - **Verification Timestamp:** {{TIMESTAMP}}

### 2. Key Insights & Mental Model Shifts
- [Insight 1: e.g., "Shifted from viewing Attention as a matrix product to viewing it as a dynamic weighted average"]
- [Insight 2: ...]

### 3. Conceptual Friction Telemetry
- `[Category]` | **Struggle:** [The specific conceptual block] | **Resolution Method:** [e.g., Socratic Bridge, First-Principles Analogy] | **Result:** [The resulting shift in understanding]
- *If no friction occurred, log: "No conceptual friction detected."*

### 4. Technical Audit (Telemetry)
- `[Category]` | **Failure:** [Specific breach] | **Trigger:** [What caught the error] | **Resolution:** [The fix]
- *If no breaches occurred, log: "No architectural or protocol breaches detected."*

### 5. Next-Focus Anchor
**Target:** {{NEXT_FOCUS_DETAILED}}
**Prerequisites for Next Session:** [List any papers to read or code to review before starting]

---

## [USER INSTRUCTIONS]
**Action Required:** Copy the 'Learning Log Entry' block above and append it to your **Progress Ledger Asset** (e.g., `progress_ledger.md`). This log is the only authoritative record of your mastery and is required for the mentor to synchronize your state in the next session.
