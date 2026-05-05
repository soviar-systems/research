# Research Hub: AI Architecture & Engineering

This repository is a dedicated research and learning hub focused on high-precision AI systems. It departs from "vibe-based" AI development in favor of a first-principles engineering approach, treating LLMs as untrusted components within a verifiable system.

## 🎯 Core Pillars

The research is divided into three primary tracks, each with its own mentor-led curriculum:

### 1. AI Code Generation Engineering (`/ai_code_generation_engineer`)
**Goal:** Build a verifiable code generation fabric that transforms natural language specs into production-grade, verified code.
- **Key Focus Areas:** 
  - Structural code manipulation (AST/CST using `libcst`, `ast-grep`).
  - Verification layers (mypy, property-based testing with `hypothesis`).
  - Secure execution (hardened containers, seccomp, Podman).
  - Integration as a verifiable component (AST-based hallucination correction).

### 2. SLM from Scratch (`/slm_from_scratch`)
**Goal:** Architect a ~100M parameter Small Language Model from first principles to achieve bare-metal understanding.
- **Key Focus Areas:**
  - Mathematical foundations (transitioning from raw NumPy to PyTorch).
  - CUDA-aware design and VRAM calculus.
  - Hardware-specific optimization for both high-VRAM GPUs (RTX 4090ti) and CPU-only systems (Debian 13).
  - Implementation of Transformer components (BPE, RoPE, MHA, KV Cache).

### 3. Precision RAG (`/rag_precision_engineering`)
**Goal:** Transition from "Naive RAG" to a deterministic "Precision Engine" for technical knowledge bases.
- **Key Focus Areas:**
  - The "Physics of Retrieval": Tokenization and the Fragment Problem.
  - Structural Retrieval: Parent-Document Retrieval and Recursive Chunking.
  - Precision Layers: Hybrid Search (BM25) and Cross-Encoder Reranking.
  - Deterministic retrieval tools to bypass probabilistic RAG failures.

## 🌿 Project Organization & Workflow

### Repository Relationship
This research hub is conceptually and structurally linked to the `mentor_generator` repository:
- **Architectural Source:** `../mentor_generator` is the authoritative architectural repository for the Mentor system, containing the "Law" (ADRs, blueprints, generation logic, and system tools).
- **Artifacts Hub:** The `/research` directory serves as the repository for the resulting artifacts (curricula, student logs, and specific track implementations) generated and managed by that architecture.

**Crucial: Tooling Location**
Any deterministic tools used by the mentors (e.g., `mentor_critical_retrieval.py`) are now centrally managed in `../mentor_generator/apps/web/tools/`. 
- **Context:** These are specifically **Open WebUI Tools**, designed to be uploaded to the Open WebUI platform and configured via "Valves." 
- **Runtime:** They execute within the Open WebUI container environment, not as standalone scripts on the host. Do not recreate them here; refer to the source in the generator repository.

### Branch-Based Development
The project uses a prefixed branching strategy to isolate the development of different research tracks:
- `rag/*` $\rightarrow$ Retrieval-Augmented Generation research (e.g., `rag/brand-new-course`).
- `slm/*` $\rightarrow$ Small Language Model research.
- `ai_code/*` $\rightarrow$ AI Code Generation research.
- `main` $\rightarrow$ The integrated source of truth where verified research is merged.

### Pedagogical Framework: Skeptical Mastery
All tracks employ a "Skeptical Mastery" approach to learning:
- **Assume No Knowledge:** Understanding is only credited after a rigorous demonstration of reasoning or implementation.
- **Atomic Learning Objectives (ALOs):** Complex topics are broken into the smallest indivisible units of concept.
- **Mastery Gating:** Progression is strictly gated by the completion of the current ALO.
- **Validation Before Abstraction:** Raw implementation (e.g., NumPy) must be verified before introducing library abstractions (e.g., PyTorch).

### Technical Enforcement
Skeptical Mastery is not a probabilistic guideline, but a deterministic architectural constraint. It is enforced via the `mentor_generator` infrastructure:
- **Role-Based Asset Manifests (mentor_generator: ADR-26012, ADR-26014):** The Mentor's access to verification criteria (ALOs) is governed by a strict manifest, preventing "vibe-based" grading or skipping of prerequisites.
- **Instructional Decoupling (mentor_generator: ADR-26014):** Behavioral "Laws" are separated from operational "Blueprints," ensuring that the Mentor follows the exact verification protocol defined in the templates.
- **Directive-Driven Control (mentor_generator: ADR-26013):** Tool-level guardrails use the `[DIRECTIVE]` pattern to force the Mentor to re-align with the authorized asset manifest upon any retrieval failure.

## 💻 Infrastructure & Environment

### Hardware Targets
- **Compute Node:** RTX 4090ti (16GB VRAM) — Used for training, embedding, and reranking models.
- **Deployment Node:** Debian 13 (CPU-only) — Used for latency profiling, resource constraint testing, and CPU inference.

### Tooling
- **Open WebUI:** Used as the primary interface for interacting with the mentor models.
- **Custom Tools:** Deterministic retrieval scripts (e.g., `mentor_critical_retrieval.py`) are used to ensure the mentors access the exact versions of syllabi and user profiles.

## 🛠️ Development Conventions
- **Verification First:** Any proposed AI-generated code must be passed through a verification layer (tests, types, or static analysis) before being considered "correct."
- **Deterministic over Probabilistic:** Prefer deterministic file access and structural manipulation over probabilistic LLM reasoning for critical system state.
