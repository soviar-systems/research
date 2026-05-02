# Precision RAG: The Master Syllabus

This document is the absolute source of truth for the course progression. Each Atomic Learning Objective (ALO) must be verified through rigorous demonstration before proceeding.

---

## # Executive Roadmap
*High-level orientation for the student and mentor.*

| Phase & Title | Primary Goal | Estimated Time |
|----------------|---------------|-----------------|
| Phase 1: The Physics of Retrieval | Understand the mathematical foundations of embeddings and the fundamental failure modes of Naive RAG. | 3-5 days |
| Phase 2: Structural Retrieval | Solve the fragmentation problem using hierarchical chunking and Parent-Document Retrieval. | 5-7 days |
| Phase 3: The Precision Layer | Eliminate semantic noise using Hybrid Search (BM25) and Cross-Encoder Reranking. | 5-7 days |
| Phase 4: Open WebUI Integration | Implement the Precision Engine in a real-world environment and optimize top-k. | 3-5 days |
| Phase 5: The Guardrail Audit | Establish metrics for Faithfulness and Relevance to eliminate hallucinations. | 3-5 days |

---

## # Detailed Curriculum
*The exhaustive, flat list of every ALO. This section is a fixed asset for mirroring.*

### Phase 1: The Physics of Retrieval
**Stage 1.1: Vector Spaces**
- **ALO 1.1:** The Embedding Function: Explain the transformation of text into a high-dimensional vector and the concept of "semantic space."
- **ALO 1.2:** Cosine Similarity: Manually calculate the distance between two vectors and explain why it's used over Euclidean distance for text.
- **ALO 1.3:** The "Vibe" Problem: Demonstrate a case where two sentences are semantically "close" but factually contradictory.

**Stage 1.2: The Naive RAG Failure**
- **ALO 1.4:** The Chunking Paradox: Explain how fixed-size chunking destroys context (the "Fragment Problem").
- **ALO 1.5:** Top-K Noise: Analyze the trade-off between recall (high K) and precision (low K) and how it triggers the Conciseness Trap.

### Phase 2: Structural Retrieval
**Stage 2.1: Advanced Chunking**
- **ALO 2.1:** Recursive Character Splitting: Implement a splitter that respects structural boundaries (paragraphs, sections) rather than just token counts.
- **ALO 2.2:** Overlap Strategy: Prove how sliding window overlap prevents information loss at chunk boundaries.

**Stage 2.2: Parent-Document Retrieval (PDR)**
- **ALO 2.3:** The Child-Parent Relationship: Design a schema where small "child" chunks are used for search, but large "parent" chunks are used for synthesis.
- **ALO 2.4:** Contextual Injection: Implement a retrieval loop that fetches the parent document once a child chunk hits the similarity threshold.

### Phase 3: The Precision Layer
**Stage 3.1: Hybrid Search**
- **ALO 3.1:** BM25 Explained: Implement basic keyword search and explain why it's superior for exact technical terms (e.g., formula names).
- **ALO 3.2:** Reciprocal Rank Fusion (RRF): Implement a method to combine Vector and BM25 results into a single, ranked list.

**Stage 3.2: Reranking**
- **ALO 3.3:** Bi-Encoders vs. Cross-Encoders: Explain the architectural difference and why Cross-Encoders are significantly more accurate but slower.
- **ALO 3.4:** The Reranking Pipeline: Implement a two-stage process: (Fast Retrieval $\rightarrow$ Slow Reranking $\rightarrow$ Final Top-K).

### Phase 4: Open WebUI Integration
**Stage 4.1: Configuration**
- **ALO 4.1:** Embedding Model Selection: Compare BGE, Cohere, and OpenAI embeddings for technical documentation.
- **ALO 4.2:** Open WebUI RAG Settings: Optimize chunk size, overlap, and top-k based on the specific technical volume.

**Stage 4.2: Customization**
- **ALO 4.3:** RAG-Specific System Prompts: Design prompts that force the LLM to cite specific chunks and flag "insufficient evidence."

### Phase 5: The Guardrail Audit
**Stage 5.1: Evaluation Metrics**
- **ALO 5.1:** Faithfulness: Define and measure how much of the answer is derived *strictly* from the retrieved context.
- **ALO 5.2:** Answer Relevance: Measure how well the retrieved context actually answers the user's query.

**Stage 5.2: The Hallucination Loop**
- **ALO 5.3:** Ground Truth Testing: Create a "Golden Dataset" of Q&A pairs to benchmark the Precision Engine.

---

## # ALO Specifications
*Proof of Mastery requirements.*

- **Mathematical Proof**: Required for ALO 1.2, 3.1.
- **Implementation Proof**: Required for ALO 2.1, 2.3, 3.2, 4.2.
- **Architectural Reasoning**: Required for ALO 1.3, 1.5, 3.3, 5.1.
