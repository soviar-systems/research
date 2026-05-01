# QWEN.md - Building a Small LLM from First Principles

## Primary Source of Truth
**CRITICAL:** The `ReadMe.md` file is the primary source of truth for the project's vision, hardware constraints, and pedagogical framework. Before initiating any session or making architectural suggestions, the agent MUST read `ReadMe.md` to align with the "Skeptical Mastery" approach and the "Trinity of State" architecture.

## Directory Structure
-   `01_foundational_neurons_and_backprop/`: Materials and implementations for Phase 1.
-   `02_tokenizer/`: Materials and implementations for Phase 2 (including BPE tokenizer code).
-   `data/`: Storage for datasets used during training.
-   `templates/`: Blueprints for onboarding new students (e.g., `user_profile_template.md`, `session_log_template.md`).
-   `mentor_slm_from_scratch.json`: **The Mentor System Prompt**. Defines the persona, pedagogical rules (anti-praise, one-small-step), and course structure.
-   `user_profile.md`: **The Context**. Defines the user's goals, hardware constraints, and professional background.
-   `learning.log`: **The Ledger**. A permanent, append-only Markdown record of mastered concepts and session history, used by the mentor via RAG.
-   `syllabus.md`: **The Map**. Detailed list of Atomic Learning Objectives (ALOs) for the course.
-   `ReadMe.md` / `ReadMe.ipynb`: Course introduction and hardware requirements.

## Mentor & Learning Setup
The learning process is guided by a hand-crafted SLM mentor system prompt implemented in **Open WebUI** using the `gemma-4-31b-it` model.

### State Management: Hybrid Ledger/Anchor Strategy
To avoid the "Instruction-Scaling Tipping Point" and programmatic fragility, the project uses a human-centric state strategy:
-   **The Ledger (`learning.log`)**: All progress, mastered concepts, and "conceptual friction" are stored in a Markdown log file synchronized with the mentor's RAG. This is the permanent source of truth.
-   **The Anchor**: For 100% reliable session resumption, the user provides the most recent "Session Log" entry from `learning.log` as an explicit anchor at the start of each session. This prevents state drift and ensures precise chronological continuation.
-   **Session Closure**: At the end of each session, the mentor generates a structured log (via `session_log_template.md`) which the user manually appends to the ledger.

### RAG System
-   **Knowledge Base**: The mentor utilizes a RAG system containing books, articles, and lecture notes (both personal and from Stanford).
-   **Synchronization**: The RAG is synchronized with the local project directory (workbooks) and updated with new articles added during learning sessions.

## Development Conventions
-   **Depth-First Mastery**: Progression is gated by verified understanding. Do not move to a new topic until the current one is mastered through mathematical derivation or code implementation.
-   **Implementation Path**:
    -   Start with **NumPy** for raw mathematical foundations to avoid "magic" library functions.
    -   Transition to **PyTorch** for architectural scaling and GPU acceleration.
-   **Validation**: Every implementation must be validated (e.g., using finite-difference gradient checks) before being considered complete.
-   **Hardware Awareness**: Every design decision should be evaluated against VRAM limits (for GPU) and memory bandwidth (for CPU).

## Key Commands
Most of the work is done in Jupyter Notebooks (`.ipynb`) or standalone Python scripts.

-   **Run Tokenizer**: `python 02_tokenizer/main.py` (or similar scripts in the tokenizer directory).
-   **General Execution**: `python <file>.py`
