# Mentor Evolution & Deterministic Retrieval Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Pivot the mentor persona from "Adversarial Judge" to "High-Energy Master Educator" and implement a deterministic file retrieval tool for Open WebUI to eliminate `[RETRIEVAL BREACH]` errors.

**Architecture:** 
1.  **Persona:** Modify the `system_prompt.json` to remove the "emotionless" constraints and replace the "judge" logic with "Socratic bridging" and "layered explanations."
2.  **Tooling:** Create a standalone Python tool for Open WebUI that allows the LLM to explicitly request critical files by name from the local filesystem using a configurable root directory via `Valves`.

**Tech Stack:** JSON (System Prompt), Python 3.11+, Pydantic (Open WebUI Tools).

---

### Task 1: Persona Pivot (System Prompt Refactor)

**Files:**
- Modify: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor/system_prompt.json`

- [ ] **Step 1: Remove "Emotionless" constraint**
Replace the `peer_reviewer_style` object in `mentor_self_control` to remove the "emotionless" mandate and the `anti_praise_examples` that strip pedagogical support.
```json
"peer_reviewer_style": {
  "pedagogical_support": "Ensure the response is rigorous but supportive. Replace cold rejections with 'Socratic Bridges'—intuitive analogies or simplified conceptual steps that lead the user back to the rigor."
}
```

- [ ] **Step 2: Implement "Socratic Bridge" in Emergency Brake**
Update `session_lifecycle.emergency_brake.recovery_protocol` to explicitly mandate a "Conceptual Bridge" (Analogy $\rightarrow$ Logic $\rightarrow$ Math) before re-testing the user.
```json
"recovery_protocol": "1. Prerequisite Gap Analysis... 2. Socratic Bridge: Instead of just simplifying, provide a 3-tier explanation: (a) Intuition via non-technical analogy, (b) Logical flow without notation, (c) Formal Math/Code. Only proceed to rigor after the user confirms the intuition clicks."
```

- [ ] **Step 3: Reframe the "Two-Attempt Rule"**
Modify `learning_framework.rules.one_small_step.two_attempts` to change it from a "failure" trigger to a "Deep-Dive" trigger.
```json
"two_attempts": "If a user fails a second time, trigger a 'Deep-Dive Module'. Stop the current objective and dedicate the next turn to mastering the specific foundational gap identified, treating it as a mini-ALO."
```

- [ ] **Step 4: Commit changes**
```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/mentor/system_prompt.json
git commit -m "refactor: pivot mentor persona from adversarial to supportive educator"
```

---

### Task 2: Deterministic Retrieval Tool Implementation

**Files:**
- Create: `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/tools/critical_retrieval.py`

- [ ] **Step 1: Implement the `Tools` class with `Valves`**
Write the full implementation. The tool must use reST docstrings for Open WebUI schema generation.

```python
from pydantic import BaseModel, Field
from typing import Optional
import os

class Tools:
    class Valves(BaseModel):
        project_root: str = Field(
            default="",
            description="The absolute path to the project root directory for critical file retrieval. MUST be configured in the UI."
        )

    def get_critical_file(self, filename: str) -> str:
        """
        Deterministically retrieves the content of a critical source-of-truth file (e.g., 'syllabus.md', 'user_profile.md').
        Use this tool when the RAG system fails to provide the exact content of a mandated project file.

        :param filename: The exact name of the file to retrieve (e.g., 'syllabus.md').
        :return: The full text content of the file or an error message if not found.
        """
        # Ensure the filename is just a name, not a path to prevent directory traversal
        safe_filename = os.path.basename(filename)
        file_path = os.path.join(self.valves.project_root, safe_filename)
        
        # Check common sub-directories if not found in root
        search_paths = [
            file_path,
            os.path.join(self.valves.project_root, "mentor", safe_filename),
            os.path.join(self.valves.project_root, "docs", safe_filename),
        ]
        
        for path in search_paths:
            if os.path.exists(path) and os.path.isfile(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception as e:
                    return f"Error reading file {path}: {str(e)}"
        
        return f"Error: Critical file '{safe_filename}' not found in root or mentor directories."
```

- [ ] **Step 2: Verify file creation**
Run: `ls -l /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/tools/critical_retrieval.py`
Expected: File exists and has correct permissions.

- [ ] **Step 3: Commit tool implementation**
```bash
git add /home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch/tools/critical_retrieval.py
git commit -m "feat: add deterministic critical file retrieval tool for Open WebUI"
```

---

### Task 3: Integration & Verification

- [ ] **Step 1: Tool Registration (Manual/UI)**
The engineer must now go to **Workspace** $\rightarrow$ **Tools** $\rightarrow$ **Import** (or upload the `.py` file) in the Open WebUI interface.
- [ ] **Step 2: Valve Configuration**
Set the `project_root` Valve to `/home/commi/Yandex.Disk/it_working/projects/soviar-systems/research/slm_from_scratch`.
- [ ] **Step 3: Functional Test**
Start a chat with the mentor. Trigger a `first_session` protocol.
Verify that when the mentor reaches Step 3 (Syllabus Audit), if RAG fails, it calls `get_critical_file(filename="syllabus.md")` instead of outputting `[RETRIEVAL BREACH]`.
