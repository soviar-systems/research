# Post-Mortem: Syllabus Retrieval Failure during First Session Protocol

**Date:** 2026-05-02
**Incident ID:** 1777723918_syllabus-rag-query-drift
**Status:** Resolved (Analysis Complete)

## 1. Executive Summary
During the `first_session` protocol, the Mentor failed to retrieve and report the full `syllabus.md` (Executive Roadmap and Detailed Curriculum) verbatim, despite the file being present in the RAG knowledge base. The Mentor instead reported fragmented ALOs and struggled to complete the "Syllabus Synchronization Audit" step. 

Investigation revealed that a high-density persona update caused "Query Drift," leading the model to prioritize pedagogical theory over operational document retrieval.

## 2. Symptoms
- **Retrieval Gap:** The Mentor failed to output the full roadmap table and exhaustive ALO list.
- **Fragmented Output:** The Mentor provided only a small subset of ALOs (specifically ALOs 2.8 through 2.12).
- **Protocol Friction:** The Mentor exhibited internal conflict/struggle because the provided RAG context did not match the strict 100% fidelity requirement of the protocol.

## 3. Evidence & Investigation

### 3.1 Analysis of Chat Export
Examination of `chat-export-1777721062998.json` reveals the internal RAG query generation process. In the `statusHistory` of the first interaction, the following queries were generated:

**Citations from `chat-export-1777721062998.json`:**
```json
"action": "queries_generated",
"queries": [
    "pedagogical framework for teaching LLM architecture from first principles",
    "best practices for mentoring deep learning and computer architecture",
    "Socratic method for technical education and engineering mastery"
]
```

### 3.2 The RAG Failure Mechanism (Probabilistic Retrieval)
The failure stems from a fundamental mismatch between how RAG works and what the protocol requires:
1. **Operational vs. Conceptual Queries:** To retrieve the `syllabus.md` fully, the model needs to generate operational queries (e.g., *"Retrieve full syllabus detailed curriculum"*). Instead, it generated conceptual queries about *how* to teach.
2. **Similarity Search Drift:** The RAG engine uses vector similarity. Queries about "Socratic methods" returned chunks describing the *philosophy* of the course. Since the syllabus was mentioned in those sections, the RAG returned fragments as "relevant" examples, but not the structured document itself.
3. **Chunking Limitations:** RAG splits documents into small fragments. Without a query that targets the *entire* structure, the engine only returns the top-K most similar pieces, making it mathematically impossible to retrieve a full, multi-page document via standard similarity search.

## 4. Root Cause Analysis

### 4.1 Persona Overload & Query Drift
The updated system prompt significantly increased the density of the **David Malan** persona and the **Skeptical Mastery** framework. This caused a shift in the model's internal attention:
- **Previous Versions:** Prioritized the *operational task* (Retrieve the syllabus $\rightarrow$ Generate "Syllabus" query $\rightarrow$ Get chunks $\rightarrow$ Present them).
- **New Version:** Prioritized the *persona identity* (Be a world-class mentor $\rightarrow$ Generate "Pedagogy" query $\rightarrow$ Get theory $\rightarrow$ Attempt to apply theory to fragments).

The model's "intent" shifted from "I need the syllabus file" to "I need to ensure I am acting like a pedagogical expert," causing the search queries to drift away from the target asset.

### 4.2 The Strictness Paradox
The new prompt introduced a high-severity penalty for syllabus errors:
> *"Any omission or summarization of these sections is a critical protocol failure. Completeness is mandatory..."*

This created a paradox that did not exist in previous versions. Previously, the model might have provided fragmented results and the user would accept them. Now, the model recognizes the RAG results are incomplete and, fearing a "critical protocol failure," it struggles to output them at all.

## 5. Architectural Mismatch: RAG vs. Protocol
The core of the issue is the use of **Probabilistic Retrieval** for a **Deterministic Requirement**.

- **RAG (Probabilistic):** Designed to find a "needle in a haystack." It is highly efficient for extraction but unreliable for reproduction.
- **Syllabus Audit (Deterministic):** Requires the "entire haystack." It is a configuration-loading task, not a knowledge-search task.

Using RAG for a verbatim synchronization audit is an architectural mismatch; you cannot guarantee 100% fidelity using a similarity-based search.

## 6. Proposed Production-Ready Solutions

To resolve this, the system must move from "pushing" context via RAG to "pulling" assets deterministically.

### Option A: Static Asset Injection (Recommended)
Inject the full content of `syllabus.md` directly into the **System Prompt** or **Permanent Context Window**.
- **Pros:** 100% reliability, lowest latency, removes query drift.
- **Cons:** Higher constant token cost.

### Option B: Tool-Based Deterministic Access
Provide the Mentor with a `read_file(path)` tool.
- **Workflow:** Mentor reaches Step 3 $\rightarrow$ Calls `read_file("mentor/syllabus.md")` $\rightarrow$ Receives entire raw text.
- **Pros:** Guaranteed fidelity, token-efficient (on-demand).
- **Cons:** Requires tool implementation and one extra turn.

### Option C: Metadata-Driven Collection Retrieval
Implement "Collection" retrieval in the RAG engine using metadata tags.
- **Workflow:** Tag all chunks of `syllabus.md` with `doc_id: "master_syllabus"`. Trigger a "Fetch All" command for that ID.
- **Pros:** Scales to many different syllabi.
- **Cons:** Requires database schema changes.

### Comparison Matrix

| Feature | Static Injection | Tool-Based Access | Metadata Collection |
| :--- | :--- | :--- | :--- |
| **Reliability** | 100% | 100% | 99% |
| **Latency** | Lowest | Medium | Medium |
| **Token Cost** | Higher (Constant) | Lower (On-demand) | Lower (On-demand) |
| **Implementation** | Trivial | Medium | High |

## 7. Conclusion & Lessons Learned
- **Persona vs. Operation:** High-density persona prompts can "drift" a model's search intent. Operational tasks must be decoupled from persona alignment.
- **RAG for Verbatimity:** RAG is unsuitable for verbatim mirroring. For critical protocol assets, deterministic access is mandatory.
- **Strictness Requires Precision:** If a prompt demands 100% fidelity, the retrieval mechanism must be deterministic (Full File Read) rather than probabilistic (Similarity Search).
