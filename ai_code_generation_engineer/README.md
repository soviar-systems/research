---
jupytext:
  formats: md:myst
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

# AI Code Generation Engineering

+++

Building a verifiable code generation fabric is a **systems problem**, not just an AI one. Our mission is to treat LLMs as *untrusted components* and build the verifiable fabric that makes their output **production-grade**.

I’m your Senior AI Code Generation Engineer mentor. We’re here to build systems that don’t just generate code—but prove it correct. Let’s begin by mapping your pipeline from spec to sandbox.


# Learning Roadmap: Production-Grade Agentic Code Systems

| Phase | Title                                      | Key Topics                                                                                                               | Hands-On Project                                                                                     | Est. Sessions |
|-------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------|
| 1     | Foundations of Structured Code Manipulation | `ast` vs `libcst`, safe refactoring, pattern matching (`ast-grep`, Semgrep), custom linters, round-trip safety            | Refactor legacy Python module with `libcst`; write Semgrep rule for unverified LLM output             | 3–4           |
| 2     | Verification & Correctness Layers          | Type checking (mypy), property-based testing (`hypothesis`), invariants, static analysis, Pass@1 metrics                  | Build test harness validating LLM-generated functions against property specs                         | 3–4           |
| 3     | Secure Execution Environments              | Hardened containers, Firecracker/gVisor, seccomp, resource limits, execution auditing                                     | Deploy sandboxed execution service using Podman + seccomp                                             | 2–3           |
| 4     | LLM Integration as a Verifiable Component  | Structured prompts, AST-based hallucination correction, retry-and-verify pipelines, observability                          | FastAPI endpoint: spec → LLM → AST parse → error correction → verified output                        | 3–4           |
| 5     | Full Agentic System Architecture           | Orchestration, LSP integration, self-improvement from failures, monitoring, ethical/safety considerations                 | Build minimal “metacompiler for AI agents” from natural language spec to deployable verified modules  | 4–5           |

# What You’ll Gain

By the end of this course, you will be able to:
- **Manipulate code structurally** using ASTs/CSTs without breaking semantics or formatting.
- **Verify correctness** of generated code through type systems, property tests, and static analysis.
- **Execute untrusted code safely** using hardened sandboxes tailored to your local infrastructure (Podman, seccomp, etc.).
- **Treat LLMs as fallible components**—correcting errors via structural feedback, not blind trust.
- **Architect end-to-end agentic systems** that are observable, auditable, and production-ready.

This isn’t theoretical. You’ll ship real tools that integrate with your existing stack: Forgejo, Traefik, Podman kube, and systemd services.

# How Sessions Work

- **Pacing**: Depth-first. We move only when you’ve *demonstrated* mastery—not just acknowledged it.
- **Session Length**: ~1–2 hours daily, as you indicated. Each session focuses on **one small step**, validated before proceeding.
- **My Role**: I’ll explain, ask you to reason aloud, and guide refinement. No fluff. No fake praise. Just engineering-grade feedback.
- **Your Role**: Engage actively. Try, fail, explain your thinking. That’s how we harden understanding.
