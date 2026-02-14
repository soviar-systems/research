---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: bash
  display_name: Bash
  language: bash
---

# Phase 1: Foundations of Structured Code Manipulation

+++

# Session 1. Tree Structures

+++

Let’s begin with **Phase 1, Topic 1**: understanding the fundamental difference between Python’s built-in `ast` module and the third-party `libcst` library—and when to use each in production agentic systems.

Both parse Python code into tree structures, but they serve different purposes:

- **`ast` (Abstract Syntax Tree)**:  
  - Part of Python’s standard library.  
  - **Lossy**: discards formatting, comments, and whitespace.  
  - Ideal for **analysis** (e.g., static checks, type inference) where exact source fidelity isn’t needed.
  - Fast and lightweight.

- **`libcst` (Concrete Syntax Tree)**:  
  - Maintains **full fidelity** to the original source: comments, spacing, indentation, even trailing commas.  
  - Enables **safe, round-trip refactoring**: parse → transform → regenerate code that passes `git diff` scrutiny.  
  - Slightly heavier, but essential when your agent must *modify* human-written code without disrupting style or collaboration workflows.

In production agentic systems, you’ll often use **both**: 
- `ast` for quick validation passes, and 
- `libcst` when you need to *rewrite* code reliably.

Now, consider this scenario:  
You’re building a tool that automatically adds type annotations to legacy Python functions using LLM suggestions. The output must preserve all existing comments and formatting so developers don’t reject the changes during code review.

**Which parser should you use—`ast` or `libcst`? And why?**

+++



+++



+++
