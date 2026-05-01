# Learning Log Maintenance Guide

The `learning.log` (The Ledger) is the permanent, append-only record of your progress through the "Building a Small LLM from First Principles" course. It is the most critical component for maintaining pedagogical continuity and preventing "instruction drift" in the mentor LLM.

## 1. Purpose
Unlike a traditional notebook, the `learning.log` serves as:
- **Evidence of Mastery**: A record of the reasoning/code that passed the "Skeptical Gate."
- **The Session Anchor**: A way to instantly restore the mentor's state at the start of a new session.
- **Friction Map**: A history of where you struggled, allowing the mentor to adjust analogies and pacing.

## 2. Initialization
If `mentor/learning.log` does not exist, create it with the following header:

```markdown
# Learning Log: Building a Small LLM from First Principles
**User Profile:** [Link to user_profile.md]
**Syllabus:** [Link to syllabus.md]

---
## Session Log: [Date] | [Initial ALO]
(First session entry goes here)
```

## 3. The Maintenance Workflow

### Step A: The Anchor (Session Start)
To prevent the mentor from losing track of your progress or repeating explanations:
1. Open `mentor/learning.log`.
2. Copy the **most recent session entry** (everything from the last `## Session Log` header to the end of the file).
3. Paste it into your chat with the mentor as the "Anchor."
   - *Prompt example:* "Here is the anchor from my last session: [Paste Log]. Let's begin the next ALO."

### Step B: The Mastery Gate (Session End)
A session ends only when the mentor verifies you have mastered the current Atomic Learning Objective (ALO). 

### Step C: The Append (Post-Session)
1. The mentor will generate a structured summary based on `mentor/templates/session_log_template.md`.
2. **Manually append** this summary to the bottom of `mentor/learning.log`.
3. Ensure a horizontal rule (`---`) or a clear header (`## Session Log: [Date]`) separates sessions.

## 4. Summary of the "Trinity of State" Interaction

| Component | Role | Interaction |
|-----------|------|-------------|
| **System Prompt** | The Law | Static; defines skeptical rules. |
| **User Profile** | The Context | Stable; defines hardware/goals. |
| **Learning Log** | The Evidence | Dynamic; appended after every session. |

## 5. Troubleshooting
- **Log becoming too large?** The mentor uses RAG or the "Anchor" strategy. You only need to provide the *most recent* entry as the anchor, not the entire file.
- **Missed a log?** If a session ended without a log, manually summarize the key breakthrough and the ALO mastered before starting the next session.
