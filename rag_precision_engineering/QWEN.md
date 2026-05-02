# Project Context: Precision RAG for Technical Knowledge Bases

## Directory Overview
This directory contains the materials and instructional framework for a first-principles course on building **Precision RAG (Retrieval-Augmented Generation)** engines. 

The goal of the project is to transition from "Naive RAG" (basic vector search) to a high-fidelity retrieval system capable of handling dense technical documentation without introducing "prompt trash" or hallucinations. The course employs a **Skeptical Mastery** pedagogical approach, requiring rigorous proof of understanding (mathematical proofs, implementation, or architectural reasoning) before progressing through the curriculum.

## Key Files

### Root Directory
- `ReadMe.md`: Contains the vision, pedagogical framework (Skeptical Mastery), and the high-level course roadmap.

### `/mentor` Directory
- `syllabus.md`: The **absolute source of truth** for course progression. It defines the five phases of the course and the specific Atomic Learning Objectives (ALOs) that must be mastered in each stage.
- `system_prompt.json`: Defines the "RAG Architect" persona. It includes:
    - **Mentor Profile**: Style, expertise, and tone (rigorous, intellectually honest, focused on the "physics of retrieval").
    - **Learning Framework**: Strict rules for interaction, including "one topic per session," "one small step" blocks, and mandatory breaks after questions.
    - **Session Lifecycle**: Protocols for starting new sessions and resuming subsequent ones.
    - **Peer Review**: An internal check-list to ensure persona consistency and pedagogical compliance.

## Usage
This directory is intended to be used as the context for an AI Mentor (the RAG Architect). Future interactions should:
1. **Refer to `syllabus.md`** for any questions regarding course progression or learning objectives.
2. **Adhere to the protocols in `system_prompt.json`** when acting as the mentor, ensuring that the "Skeptical Mastery" approach is maintained.
3. **Follow the Roadmap** defined in `ReadMe.md` to guide the student through the five phases of Precision RAG engineering.
4. **Validate Mastery** using the specifications in the syllabus (e.g., requiring a mathematical proof for Cosine Similarity) before moving to the next ALO.
