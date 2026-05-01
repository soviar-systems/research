# SLM Syllabus: Atomic Learning Objectives (ALOs)

This document serves as the structural map for the "Building a Small LLM from First Principles" course. Each entry is an Atomic Learning Objective (ALO)—the smallest unit of knowledge that must be rigorously validated before progression.

## Phase 1: Foundational Neurons & Backprop
*Goal: Manual NumPy implementation of the smallest possible learning unit.*
- [ ] **ALO 1.1: The Linear Neuron** - Mathematical representation of $z = wx + b$ and the concept of weights/biases.
- [ ] **ALO 1.2: Activation Functions** - Mathematical derivation and purpose of Sigmoid, Tanh, and ReLU.
- [ ] **ALO 1.3: Scalar Forward Pass** - Implementation of a single neuron forward pass in NumPy.
- [ ] **ALO 1.4: The Chain Rule** - Mathematical understanding of how gradients propagate backward through nested functions.
- [ ] **ALO 1.5: Scalar Backward Pass** - Manual derivation and NumPy implementation of the gradient for a single neuron.
- [ ] **ALO 1.6: Gradient Descent Update** - Implementation of the weight update rule $\theta = \theta - \eta \nabla J(\theta)$.
- [ ] **ALO 1.7: Convergence & Loss** - Understanding Mean Squared Error (MSE) and the concept of reaching a local minimum.

## Phase 2: Core Transformer Components
*Goal: Transition to PyTorch and implement the building blocks of the Attention mechanism.*
- [ ] **ALO 2.1: BPE Tokenization** - Mathematical and algorithmic understanding of Byte Pair Encoding.
- [ ] **ALO 2.2: Embedding Spaces** - Representation of tokens as vectors and the purpose of the embedding matrix.
- [ ] **ALO 2.3: Positional Encoding** - Mathematical implementation of Absolute and Rotary (RoPE) positional embeddings.
- [ ] **ALO 2.4: QKV Projection** - Understanding the linear transformations that create Query, Key, and Value vectors.
- [ ] **ALO 2.5: Scaled Dot-Product Attention** - Mathematical derivation and implementation of the core attention formula.
- [ ] **ALO 2.6: Multi-Head Attention (MHA)** - Parallelizing attention heads and the final linear projection.
- [ ] **ALO 2.7: Feed-Forward Network (FFN)** - The role of the position-wise MLP in the transformer block.

## Phase 3: Optimization & Architecture
*Goal: Moving from a naive transformer to a production-ready architecture.*
- [ ] **ALO 3.1: LayerNorm & RMSNorm** - Mathematical understanding of normalization and its effect on training stability.
- [ ] **ALO 3.2: Residual Connections** - The "highway" for gradients and the mitigation of the vanishing gradient problem.
- [ ] **ALO 3.3: KV Cache (Conceptual)** - Understanding why we cache Keys and Values during auto-regressive generation.
- [ ] **ALO 3.4: KV Cache (Implementation)** - Modifying the attention block to support incremental decoding.
- [ ] **ALO 3.5: Flash Attention (Conceptual)** - Understanding IO-awareness and the reduction of memory reads/writes.
- [ ] **ALO 3.6: AdamW Optimizer** - Mathematical difference between SGD and AdamW (weight decay).
- [ ] **ALO 3.7: Learning Rate Schedulers** - Implementation of Warmup and Cosine Decay.

## Phase 4: Training & Alignment
*Goal: Scaling the model to 100M parameters and aligning it with user intent.*
- [ ] **ALO 4.1: Data Pipeline** - Tokenizing large corpora, shuffling, and creating efficient PyTorch DataLoaders.
- [ ] **ALO 4.2: The Training Loop** - Implementing the outer loop (epochs) and inner loop (batches) with gradient clipping.
- [ ] **ALO 4.3: Cross-Entropy Loss** - Understanding the mathematical objective of next-token prediction.
- [ ] **ALO 4.4: Supervised Fine-Tuning (SFT)** - Transitioning from base model to an instruction-following model.
- [ ] **ALO 4.5: RLHF/PPO Basics** - Understanding the Reward Model and the PPO objective function.
- [ ] **ALO 4.6: DPO (Direct Preference Optimization)** - Implementing alignment without a separate reward model.

## Phase 5: Architectural Review & Deployment
*Goal: Optimizing for the target hardware and defending the design.*
- [ ] **ALO 5.1: INT8 Quantization** - Mathematical principles of mapping FP32 weights to 8-bit integers.
- [ ] **ALO 5.2: Memory Footprint Analysis** - Calculating VRAM usage for weights, gradients, and KV Cache.
- [ ] **ALO 5.3: CPU Inference Profiling** - Analyzing latency and bottlenecks on the Debian 13 system.
- [ ] **ALO 5.4: Final Architectural Defense** - A comprehensive review justifying every design choice against hardware constraints.
