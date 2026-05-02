# Precision RAG for Technical Knowledge Bases: A First-Principles Course

*"If you cannot explain the retrieval path, you cannot trust the answer."*

This course is designed to move the student from **Naive RAG** (fragmented vector search) to a **Precision Engine** (high-fidelity retrieval) capable of handling dense technical textbooks and research papers without introducing "prompt trash."

## The Vision
Most RAG systems are "vibe-based"—they retrieve things that *sound* similar. For an AI Architect, this is unacceptable. We need **deterministic precision**. This course focuses on the engineering of the retrieval pipeline to ensure that the LLM receives the exact, complete, and correct evidence required to answer complex technical queries.

## Pedagogical Framework: Skeptical Mastery
This course follows the **Skeptical Mastery** approach:
1. **Assume No Knowledge**: You don't "understand" a retrieval strategy until you can prove why it fails in a specific edge case.
2. **Mastery Gating**: Progression is gated by rigorous demonstration (e.g., manually calculating a cosine similarity or designing a chunking strategy for a complex mathematical proof).
3. **One ALO per Session**: We focus on one Atomic Learning Objective (ALO) at a time to prevent cognitive overload.
4. **Validation Before Abstraction**: We analyze the raw vectors and chunks before moving to high-level configurations in Open WebUI.

## Course Roadmap

| Phase | Focus | Goal |
|---|---|---|
| **Phase 1** | The Physics of Retrieval | Master Tokenization, Vector Spaces, Embeddings, and the "Fragment Problem." |
| **Phase 2** | Structural Retrieval | Implement Parent-Document Retrieval and Recursive Chunking. |
| **Phase 3** | The Precision Layer | Integrate Hybrid Search (BM25) and Cross-Encoder Reranking. |
| **Phase 4** | Open WebUI Integration | Deploy the Precision Engine into a production environment. |
| **Phase 5** | The Guardrail Audit | Build a verification loop for Faithfulness and Relevance. |
| **Phase 6** | Domain Adaptation | Optimize the embedding engine via synthetic data and fine-tuning. |

## Hardware Context
- **Primary**: RTX 4090ti (16GB VRAM) - used for embedding and reranking models.
- **Secondary**: Debian 13 (CPU) - used for testing latency and resource constraints.

---
**Course Artifacts:**
- `mentor/system_prompt.json`: The RAG Architect persona.
- `mentor/syllabus.md`: The absolute source of truth for progression.
- `mentor/learning.log`: The ledger of mastered retrieval concepts.
