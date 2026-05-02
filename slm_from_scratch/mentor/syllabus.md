# SLM From Scratch: The Master Syllabus

This document is the absolute source of truth for the course progression. Each Atomic Learning Objective (ALO) must be verified through rigorous demonstration (math, code, or architectural reasoning) before proceeding.

---

## # Executive Roadmap
*High-level orientation for the student and mentor.*

| Phase & Title | Primary Goal | Estimated Time |
|----------------|---------------|-----------------|
| Phase 1: Foundational Neurons & Backprop | Understand the physics of learning. Move from a single mathematical operation to a multi-layer network using only NumPy. | 7-10 days |
| Phase 2: Core Components of the Transformer | Deconstruct the "Attention is All You Need" architecture. Move from raw math to PyTorch modules. | 12-16 days |
| Phase 3: Optimization & Architecture | Optimize for memory and speed. Understand the gap between "mathematically correct" and "computationally efficient." | 10-14 days |
| Phase 4: Training & Alignment | Scale the model. Move from a block to a 100M parameter model trained on real data. | 12-15 days |
| Phase 5: Architectural Review & Deployment | Professionalize the system. Validate the model's efficiency across different hardware targets. | 7-10 days |

---

## # Detailed Curriculum
*The exhaustive, flat list of every ALO. This section is a fixed asset for external presentation.*

### Phase 1: Foundational Neurons & Backprop
**Stage 1.1: The Single Neuron**
- **ALO 1.1:** The Linear Sum: Implement $\sum (w_i x_i) + b$ and explain the geometric meaning of weights and bias.
- **ALO 1.2:** Activation Functions: Implement Sigmoid, ReLU, and Tanh. Manually derive their derivatives on paper.
- **ALO 1.3:** Forward Pass: Implement a single neuron forward pass in NumPy.

**Stage 1.2: The Mechanics of Backprop**
- **ALO 1.4:** The Chain Rule: Manually derive the gradient of the loss with respect to weights for a single neuron.
- **ALO 1.5:** NumPy Backprop: Implement the backward pass for a single neuron.
- **ALO 1.6:** Gradient Descent: Implement the weight update rule and explain the impact of the learning rate.
- **ALO 1.7:** Finite-Difference Check: Implement a gradient checker to verify the analytical gradient against numerical approximation.

**Stage 1.3: The Bridge (MLP in NumPy)**
- **ALO 1.8:** Matrix Vectorization: Transition from loops to matrix multiplications ($\mathbf{Wx} + \mathbf{b}$).
- **ALO 1.9:** Multi-Layer Perceptron (MLP): Implement a 2-layer network in NumPy.
- **ALO 1.10:** Layered Backprop: Implement backpropagation through multiple layers, maintaining the Jacobian chain.

### Phase 2: Core Components of the Transformer
**Stage 2.1: Tokenization & Embeddings**
- **ALO 2.1:** Tokenization Theory: Compare Character-level, Word-level, and Subword (BPE/WordPiece) tokenization.
- **ALO 2.2:** BPE Implementation: Implement a basic Byte Pair Encoding (BPE) tokenizer from scratch.
- **ALO 2.3:** Embedding Spaces: Implement a trainable embedding layer and explain high-dimensional vector representation.
- **ALO 2.4:** Positional Encoding: Implement Absolute Positional Embeddings and explain why Transformers need them.
- **ALO 2.5:** RoPE: Implement Rotary Positional Embeddings and explain the rotation matrix logic.

**Stage 2.2: The Attention Mechanism**
- **ALO 2.6:** QKV Math: Implement the calculation of Query, Key, and Value matrices.
- **ALO 2.7:** Scaled Dot-Product Attention: Implement $\text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ and explain the scaling factor $\sqrt{d_k}$.
- **ALO 2.8:** Causal Masking: Implement the look-ahead mask for decoder-only models.
- **ALO 2.9:** Multi-Head Attention (MHA): Implement MHA and analyze the $O(n^2)$ time and space complexity.

**Stage 2.3: PyTorch Transition**
- **ALO 2.10:** PyTorch Tensors: Map NumPy operations to PyTorch tensors and CUDA device movement.
- **ALO 2.11:** Autograd: Compare manual NumPy backprop with `loss.backward()` in PyTorch.
- **ALO 2.12:** Attention Block: Implement a full MHA block as a `torch.nn.Module`.

### Phase 3: Optimization & Architecture
**Stage 3.1: Structural Refinements**
- **ALO 3.1:** LayerNorm: Implement Layer Normalization and explain why it is preferred over BatchNorm for NLP.
- **ALO 3.2:** Feed-Forward Networks (FFN): Implement the position-wise FFN and explain its role as a "knowledge store."
- **ALO 3.3:** Residual Connections: Implement skip-connections and explain their role in solving the vanishing gradient problem.

**Stage 3.2: Memory & Inference Optimization**
- **ALO 3.4:** The KV Cache: Implement the KV cache mechanism and prove the inference speedup.
- **ALO 3.5:** Flash Attention Theory: Explain the Tiling approach and the trade-off between HBM (High Bandwidth Memory) and SRAM.
- **ALO 3.6:** VRAM Calculus: Calculate the exact VRAM requirement for a model given: parameters, optimizer states (AdamW), and activation tensors.

**Stage 3.3: Optimizer Dynamics**
- **ALO 3.7:** AdamW: Implement or analyze the AdamW update rule, specifically the decoupled weight decay.
- **ALO 3.8:** Learning Rate Scheduling: Implement Cosine Decay with Warm-up and explain its necessity for stability.

### Phase 4: Training & Alignment
**Stage 4.1: Data Theory & Preparation**
- **ALO 4.1:** Pre-training Corpora: Analyze the requirements for a pre-training dataset (diversity, scale, cleaning).
- **ALO 4.2:** SFT Datasets: Design an instruction-tuning dataset and explain the difference between "completion" and "instruction" data.
- **ALO 4.3:** Data Pipeline: Implement a high-performance PyTorch DataLoader with sharding.

**Stage 4.2: The Training Loop**
- **ALO 4.4:** Loss Functions: Implement Cross-Entropy loss and explain the role of the softmax temperature.
- **ALO 4.5:** Evaluation Metrics: Implement and explain Perplexity (PPL) and Cross-Entropy as measures of model quality.
- **ALO 4.6:** Training Loop: Implement a full training loop (using PyTorch Lightning or native PyTorch) with gradient clipping.

**Stage 4.3: Efficiency & Alignment**
- **ALO 4.7:** Parameter Efficiency: Implement LoRA (Low-Rank Adaptation) and explain the $A \times B$ matrix decomposition.
- **ALO 4.8:** Alignment Concepts: Explain the conceptual flow of SFT $\rightarrow$ Reward Modeling $\rightarrow$ PPO/DPO.
- **ALO 4.9:** The 100M Model: Execute the training of a 100M parameter model and analyze the loss curve.

### Phase 5: Architectural Review & Deployment
**Stage 5.1: The Full Trace**
- **ALO 5.1:** Bare-Metal Trace: Trace a single token from input $\rightarrow$ tokenizer $\rightarrow$ embeddings $\rightarrow$ N layers $\rightarrow$ LM head $\rightarrow$ output.
- **ALO 5.2:** Sampling Strategies: Implement Top-k, Top-p (nucleus), and Temperature sampling.

**Stage 5.2: Quantization & Efficiency**
- **ALO 5.3:** Quantization Theory: Explain the mapping from FP32 $\rightarrow$ FP16 $\rightarrow$ INT8.
- **ALO 5.4:** CPU vs GPU: Analyze the memory bandwidth bottleneck on CPU and implement a basic CPU-optimized inference path.

**Stage 5.3: Final Defense**
- **ALO 5.5:** Architectural Defense: Provide a rigorous justification for every design choice (e.g., "Why RoPE over Absolute?", "Why AdamW over SGD?") against the specific hardware constraints of the target system.

---

## # ALO Specifications
*The internal "Skeptical Mastery" gate definitions. Defines exactly what constitutes Proof of Mastery.*

**Phase 1**
- **ALO 1.1:** Proof = Correct implementation of linear sum in NumPy + explanation of weight geometry (hyperplane).
- **ALO 1.2:** Proof = Correct implementation of Sigmoid, ReLU, Tanh + manual derivation of derivatives.
- **ALO 1.3:** Proof = Functional NumPy forward pass of single neuron.
- **ALO 1.4:** Proof = Manual derivation of gradient $\frac{\partial L}{\partial w}$ and $\frac{\partial L}{\partial b}$ for single neuron.
- **ALO 1.5:** Proof = Functional NumPy backward pass for single neuron.
- **ALO 1.6:** Proof = Implementation of SGD update + reasoning on learning rate's impact on loss landscape.
- **ALO 1.7:** Proof = Numerical gradient check result matching analytical gradient within $10^{-7}$ tolerance.
- **ALO 1.8:** Proof = Implementation of matrix multiplication for batch forward pass + explanation of broadcasting.
- **ALO 1.9:** Proof = Functional 2-layer MLP in NumPy (forward + backward).
- **ALO 1.10:** Proof = Correct backprop through MLP with verification of gradient flow to the first layer.

**Phase 2**
- **ALO 2.1:** Proof = Comparative analysis of tokenization types with specific edge-case examples.
- **ALO 2.2:** Proof = Functional BPE tokenizer that can train on a corpus and encode/decode text.
- **ALO 2.3:** Proof = PyTorch embedding layer implementation + explanation of the embedding matrix as a lookup table.
- **ALO 2.4:** Proof = Correct sinusoidal positional encoding implementation + explanation of why relative distance is preserved.
- **ALO 2.5:** Proof = Implementation of RoPE rotation matrix + explanation of how it encodes relative position.
- **ALO 2.6:** Proof = Correct calculation of $Q, K, V$ from input embeddings using linear projections.
- **ALO 2.7:** Proof = Implementation of Scaled Dot-Product Attention + explanation of why scaling by $\sqrt{d_k}$ prevents gradient vanishing.
- **ALO 2.8:** Proof = Correct causal mask implementation ensuring no future token visibility.
- **ALO 2.9:** Proof = Implementation of MHA + analysis of $O(n^2)$ complexity relative to sequence length.
- **ALO 2.10:** Proof = Functional migration of a NumPy op to PyTorch with `.to('cuda')` management.
- **ALO 2.11:** Proof = Comparison of manual gradient calculation vs `autograd` for a simple operation.
- **ALO 2.12:** Proof = Full MHA PyTorch module passing a basic shape-consistency test.

**Phase 3**
- **ALO 3.1:** Proof = Correct LayerNorm implementation + explanation of why it stabilizes training better than BatchNorm in NLP.
- **ALO 3.2:** Proof = Implementation of FFN + explanation of its role as a key-value memory.
- **ALO 3.3:** Proof = Implementation of skip-connections + explanation of the "identity path" for gradients.
- **ALO 3.4:** Proof = Functional KV cache implementation + proof of $O(1)$ per-token generation vs $O(n)$.
- **ALO 3.5:** Proof = Explanation of Flash Attention's Tiling approach and the HBM vs SRAM bottleneck.
- **ALO 3.6:** Proof = Exact VRAM calculation for a specific model config (params, optimizer, activations) on a 4090ti.
- **ALO 3.7:** Proof = Implementation/Analysis of AdamW decoupled weight decay vs standard Adam.
- **ALO 3.8:** Proof = Functional Cosine Decay with Warm-up implementation + reasoning on stability.

**Phase 4**
- **ALO 4.1:** Proof = Analysis of a specific dataset's diversity and cleaning pipeline.
- **ALO 4.2:** Proof = Design of an SFT prompt template + explanation of the completion vs instruction gap.
- **ALO 4.3:** Proof = Functional PyTorch DataLoader with sharding for large datasets.
- **ALO 4.4:** Proof = Correct Cross-Entropy implementation + explanation of temperature's effect on probability distribution.
- **ALO 4.5:** Proof = Implementation of Perplexity (PPL) calculation from cross-entropy loss.
- **ALO 4.6:** Proof = Functional training loop with gradient clipping and loss logging.
- **ALO 4.7:** Proof = Functional LoRA implementation + explanation of the low-rank update $W + AB$.
- **ALO 4.8:** Proof = Conceptual flow diagram of SFT $\rightarrow$ Reward Model $\rightarrow$ PPO/DPO.
- **ALO 4.9:** Proof = Successful training of a 100M model with a decreasing loss curve.

**Phase 5**
- **ALO 5.1:** Proof = Step-by-step trace of a token through the entire model pipeline.
- **ALO 5.2:** Proof = Correct implementation of Top-k, Top-p, and Temperature sampling.
- **ALO 5.3:** Proof = Explanation of quantization mapping (FP32 $\rightarrow$ INT8) and the role of scale/zero-point.
- **ALO 5.4:** Proof = Comparison of inference latency on CPU vs GPU for a fixed model size.
- **ALO 5.5:** Proof = Rigorous defense of all architectural choices against hardware constraints.
