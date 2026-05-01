*"The real understanding comes when we get our hands dirty and build these things"* - says my first AI mentor Richard Feynman.

The goal of this course is a preparation for AI-backend optimization (e.g., CUDA, tensor cores, memory hierarchy tuning).

I use my own mentor prompt generated with the help from my another prompt ["mentor_generator v0.24.3"](https://github.com/lefthand67/mentor_generator) to learn LLMs under the hood by building it from scratch. The idea stems from the [Stanford CS336 course](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) but this course is interactive though it needs hallucination checks.

***

*"What I cannot create, I do not understand."* - Richard Feynman

Hello, and welcome. We are beginning **“Building a Small LLM from First Principles”**, a depth-first course tailored to your profile:
- Your goal is professional readiness as an **AI Architect**, with emphasis on **CUDA-aware design** and **bare-metal understanding**.
- You operate in two environments: a high-VRAM GPU (RTX 4090ti, 16 GB) and a CPU-only Debian 13 system—so **VRAM and latency constraints** are central to every design decision.

## Goals & Practical Skills

By the end of this course, you will:
- **Architect** a 100M-parameter LLM from scratch.
- **Explain** every component down to memory layout and gradient flow.
- **Optimize** for both VRAM (4090ti) and CPU (Debian 13) constraints.
- **Defend** your design choices in an AI Architect interview with mathematical and hardware-aware reasoning.

## Pedagogical Framework: Skeptical Mastery

This course rejects passive learning. It is built on the principle of **Skeptical Pedagogy**: Assume the user has no correct understanding of a topic until they provide a rigorous demonstration of reasoning. "Mostly understanding" is insufficient for an AI Architect role and often masks critical gaps.

**The Atomic Learning Objective (ALO):** An ALO is the smallest indivisible unit of a concept that can be independently validated through reasoning or implementation. Breaking complex topics into ALOs prevents cognitive overload and ensures no gaps in the foundational mental model.

1.  **Assume No Knowledge**: The mentor assumes the user has a gap in understanding until a rigorous demonstration of reasoning is provided.
2.  **Mastery Gating**: Progression is strictly gated. You cannot move to a new ALO until the current one is mastered through mathematical derivation or code implementation. Passive acknowledgment ("I get it") is invalid.
3.  **One ALO per Session**: To prevent cognitive overload and shallow learning, each session focuses on exactly one **Atomic Learning Objective (ALO)**. A session ends once the ALO is mastered.
4.  **Dynamic Calibration**: The mentor does not rely on a static "Intermediate" label. It calibrates your level incrementally by observing your reasoning process in each session.

### Advanced Pedagogical Constraints

- **System Prompt Maturation**: The mentor's governing rules are evolved manually. Observed failures in the `learning.log` are identified as patterns and converted into strict pedagogical rules in the system prompt to prevent recurrence.
- **Prompt Simplicity & Instruction Budget**: To avoid "Agentic Friction" and the "Instruction-Scaling Tipping Point," the system prompt avoids complex programmatic protocols (e.g., FSMs, rigid JSON loops). It focuses on pedagogical goals, using simple human-readable anchors for state (e.g., Markdown session logs) rather than trying to force the LLM into a rigid programmatic state.
    - *Note on FSMs*: A Finite State Machine (FSM) is a model where a system exists in one of a finite number of states and transitions between them based on inputs. In prompting, attempting to enforce a rigid FSM often leads the LLM to prioritize state-tracking over execution, causing "instruction decay."

### Administrative Notes
- Each session is **~1 hour**.
- **No deadlines**—progress is gated solely by verified understanding.
- You must **demonstrate reasoning**, not just recall.
- We use **one small step at a time**, with micro-validation.

## Implementation Philosophy: Validation Before Abstraction

To ensure foundational clarity and avoid "over-architecting," this project adheres to the following coding principle:

**Insist on code validation before abstraction.** 
Encourage raw implementation (e.g., raw NumPy) to verify mathematical correctness and logic before introducing modular design, encapsulation, or library abstractions (e.g., PyTorch).

**Why:** Abstractions can mask bugs in the underlying logic. By proving the math in its simplest form first, we ensure that the subsequent architecture is built on a verified foundation.


The curriculum is not a timeline, but a map of **Atomic Learning Objectives (ALOs)** detailed in `syllabus.md`.

| Phase | Focus | Hands-On | Estimated Time | Core ALOs |
|------|--------|----------|-----------------|-------------------|
| **Phase 1** | Foundational Neurons & Backprop | NumPy: single neuron, activation, gradient descent | 5–7 days | ALO 1.1 $\rightarrow$ 1.7 |
| **Phase 2** | Core Transformer Components | PyTorch: tokenization, positional encoding, attention | 10–14 days | ALO 2.1 $\rightarrow$ 2.7 |
| **Phase 3** | Optimization & Architecture | KV Cache, Flash Attention, LayerNorm, AdamW | 10–12 days | ALO 3.1 $\rightarrow$ 3.7 |
| **Phase 4** | Training & Alignment | Dataset prep, training loop, SFT, basic PPO/DPO | 12–15 days | ALO 4.1 $\rightarrow$ 4.6 |
| **Phase 5** | Architectural Review & Deployment | Quantization (INT8), CPU inference, full system audit | 7–10 days | ALO 5.1 $\rightarrow$ 5.4 |

*Total estimated commitment: **~50–60 hours**, paced by **mastery**, not calendar.*

## The Trinity of State Architecture

To maintain absolute pedagogical continuity and avoid "Instruction Drift," the project decouples the mentor's state into three discrete components. This separates the **Control Plane** (management and state definitions) from the **Execution Plane** (code and notebook work).

### 1. The System Prompt (The Law)
Stored in `mentor/system_prompt.json`. It defines the **how**: the persona, the skeptical rules, and the interaction protocols. It is a stable specification that does not change based on user progress.

### 2. The User Profile (The Context)
Stored in `mentor/user_profile.md`. It defines the **who**: goals, professional background, and critical hardware constraints (4090ti vs CPU-only).

### 3. The Learning Log (The Evidence)
Stored in `mentor/learning.log`. It defines the **what**: a permanent, append-only ledger of mastered ALOs. Each entry contains the "Proof of Mastery" (the reasoning or code that passed the Skeptical Gate).

**Session Flow:**
`Syllabus` $\rightarrow$ `Skeptical Session (One ALO)` $\rightarrow$ `Mastery Gate` $\rightarrow$ `Append Proof to learning.log` $\rightarrow$ `Next ALO`.


## Hardware Selection & Requirements

**Hardware Requirements Analysis:**

| Component | RTX 4090ti | Weaker Laptop | Impact |
|-----------|------------|---------------|---------|
| **VRAM** | 16GB | Shared system RAM (8GB total) | Limits model size and batch size |
| **Compute** | High parallel throughput | Limited CPU cores | Slower training times |
| **Memory Bandwidth** | ~1 TB/s | ~50 GB/s | Significant bottleneck for matrix ops |
| **Practical Limits** | 100M param model feasible | ~10M param model maximum | Scales final project scope |

### Constraint Analysis: Running on a Weaker Laptop
While the core concepts of computational graphs and transformer mechanics remain identical regardless of hardware, using the weaker laptop (CPU-only) would require the following adjustments:
1. **Phase 1-3**: Completely feasible (algorithmic implementations).
2. **Phase 4**: Model scale reduced from 100M to ~10M parameters.
3. **Training Time**: 10-50x slower execution.
4. **Batch Size**: Minimal (possibly 1).

**Hardware Selection Rule:**
- **Phases 1–4**: Use **only the Lenovo Legion 7 Pro (RTX 4090ti)**. The focus is on building and understanding the LLM on a capable system.
- **Phase 5**: Use **both systems**. The **Dell (Debian 13, CPU-only)** is reserved for deployment analysis, latency profiling, and efficiency testing.
