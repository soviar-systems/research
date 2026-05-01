# QWEN.md - Building a Small LLM from First Principles

## Project Overview
This project is a depth-first, structured learning course aimed at building a Small Language Model (SLM) from the ground up. The primary objective is to prepare the user for a role as an **AI Architect**, with a heavy emphasis on **CUDA-aware design**, bare-metal understanding of transformer architecture, and hardware-specific optimization (VRAM and latency).

The curriculum is designed to transition from manual mathematical implementations in NumPy to a fully functional 100M parameter LLM using PyTorch, ending with deployment analysis on CPU-only systems.

### Learning Roadmap
The project is divided into five phases:
1.  **Foundational Neurons & Backprop**: Manual NumPy implementation of neurons, activations, and gradient descent.
2.  **Core Transformer Components**: PyTorch implementation of BPE tokenization, positional embeddings, and Multi-Head Attention.
3.  **Optimization & Architecture**: Implementing KV Cache, Flash Attention, LayerNorm, and AdamW.
4.  **Training & Alignment**: Dataset preparation, training loops, SFT, and basic PPO/DPO.
5.  **Architectural Review & Deployment**: Quantization (INT8), CPU inference profiling, and final system audit.

## Directory Structure
-   `01_foundational_neurons_and_backprop/`: Materials and implementations for Phase 1.
-   `02_tokenizer/`: Materials and implementations for Phase 2 (including BPE tokenizer code).
-   `data/`: Storage for datasets used during training.
-   `mentor_slm_from_scratch.json`: **Critical State File**. Contains the mentor's profile, the detailed learning plan, and the user's current progress (mastered concepts, session logs, and next focus).
-   `ReadMe.md` / `ReadMe.ipynb`: Course introduction and hardware requirements.

## Hardware Context
The project targets two specific environments to understand the trade-offs between high-performance compute and constrained deployment:
-   **Development (Phases 1-4)**: Lenovo Legion 7 Pro (RTX 4090ti, 16GB VRAM) on Fedora 42.
-   **Deployment Analysis (Phase 5)**: Dell (CPU-only, 8GB RAM) on Debian 13.

## Mentor & Learning Setup
The learning process is guided by a hand-crafted SLM mentor system prompt implemented in **Open WebUI** using the `gemma-4-31b-it` model.
-   **Knowledge Base (RAG)**: The mentor utilizes a RAG system containing books, articles, and lecture notes (both personal and from Stanford).
-   **Synchronization**: The RAG is synchronized with the local project directory (workbooks) and updated with new articles added during learning sessions to ensure the mentor has comprehensive access to all necessary literature.

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
