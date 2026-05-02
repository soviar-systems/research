This course reference library is designed to support the **SLM From Scratch** syllabus, bridging the gap between foundational 1980s neural theory and 2026 state-of-the-art (SOTA) optimizations like **FlashAttention-4** and **Multi-Head Latent Attention (MLA)**.

# Course Reference Library

## 🛠 Classification Legend
- **[Primary]**: Authoritative gold standard/official definition.
- **[Intuition]**: Conceptual or visual explanations to help a concept "click".
- **[Alternative]**: Rigorous but provides a different lens or explanation.
- **[Deep Dive]**: Advanced "Architect's Edge" (hardware optimizations, edge cases).
- **[Note]**: Meta-information or specific context.

---

## [ALO-01] Foundational Neurons & Backprop
- **[Primary]**: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, *323*(6088), 533–536.
- **[Intuition]**: Karpathy, A. (2022). *Neural Networks: Zero to Hero (micrograd)*. A step-by-step visual trace of the computational graph and partial derivatives in code.
- **[Alternative]**: Nielsen, M. A. (2015). *Neural Networks and Deep Learning*. Determination Press. Provides a highly readable, math-first approach to the quadratic cost function and backprop equations.
- **[Deep Dive]**: Baydin, A. G., et al. (2018). Automatic differentiation in machine learning: a survey. *Journal of Machine Learning Research*. Explores the distinction between forward-mode and reverse-mode autodiff used in modern frameworks.
- **[Note]**: Focus on ALO 1.7 (Finite-Difference Check) using the Nielsen text to understand why numerical approximations are the "unit tests" of backpropagation.

## [ALO-02] Tokenization
- **[Primary]**: Sennrich, R., Haddow, B., & Birch, A. (2016). Neural Machine Translation of Rare Words with Subword Units (BPE). *arXiv*.
- **[Intuition]**: Hugging Face (2023). *Summary of the Tokenizers*. A conceptual breakdown of the differences between BPE (GPT), WordPiece (BERT), and Unigram (T5/XLNet).
- **[Alternative]**: Kudo, T., & Richardson, J. (2018). SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing. *EMNLP*.
- **[Deep Dive]**: OpenAI (2023). *tiktoken*. A fast BPE tokenizer for use with OpenAI's models, demonstrating optimized inference speeds for production-grade LLMs.
- **[Note]**: Essential for ALO 2.2. Use the Dzongkha Comparative Analysis (2025) to see how BPE performs in low-resource environments compared to SentencePiece.

## [General] Hardware & Optimization
- **[Deep Dive]**: Dao, T. (2026). FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling. *arXiv*. Optimizes attention for modern GPUs through asynchronous execution and Tiling.
- **[Deep Dive]**: DeepSeek-AI (2025). *DeepSeek-V3 Technical Report*. Introduces **Multi-Head Latent Attention (MLA)**, which compresses the KV cache by a factor of 57 compared to standard MHA.
- **[Deep Dive]**: Rafailov, R., et al. (2023). Direct Preference Optimization (DPO): Your Language Model is Secretly a Reward Model. *NeurIPS*. The primary source for the alignment phase (Phase 4.3).
- **[Note]**: Regarding ALO 3.6 (VRAM Calculus), refer to the **Llama 3.1 technical report (2024)** for real-world scaling data, where GQA was standardized across all model sizes (8B to 405B) to manage memory bandwidth.

---

### References

Ainslie, J., Lee-Thorp, J., de Jong, M., Zemlyanskiy, Y., Real, F., & Joshua, S. (2023). GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints. *arXiv*. [https://doi.org/10.48550/arXiv.2305.13245](https://doi.org/10.48550/arXiv.2305.13245)

Baydin, A. G., Pearlmutter, B. A., Radul, A. A., & Siskind, J. M. (2018). Automatic differentiation in machine learning: a survey. *Journal of Machine Learning Research*, *18*(1), 5595–5637.

Dao, T. (2026). FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling. *arXiv*. [https://doi.org/10.48550/arXiv.2603.05451](https://doi.org/10.48550/arXiv.2603.05451)
Cited by: 12

DeepSeek-AI. (2025). DeepSeek-V3 Technical Report. *arXiv*. [https://doi.org/10.48550/arXiv.2502.14837](https://doi.org/10.48550/arXiv.2502.14837)

Kudo, T., & Richardson, J. (2018). SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing. *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, 66–71. [https://doi.org/10.18653/v1/D18-2012](https://doi.org/10.18653/v1/D18-2012)
Cited by: 2450

Meta AI. (2024). The Llama 3 Herd of Models. *Technical Report*. [https://ai.meta.com/research/publications/the-llama-3-herd-of-models/](https://ai.meta.com/research/publications/the-llama-3-herd-of-models/)

Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023). Direct Preference Optimization: Your Language Model is Secretly a Reward Model. *Advances in Neural Information Processing Systems*, *36*.

Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, *323*(6088), 533–536. [https://doi.org/10.1038/323533a0](https://doi.org/10.1038/323533a0)
Cited by: 45000

Sennrich, R., Haddow, B., & Birch, A. (2016). Neural Machine Translation of Rare Words with Subword Units. *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics*, 1715–1725. [https://doi.org/10.18653/v1/P16-1162](https://doi.org/10.18653/v1/P16-1162)
Cited by: 11200
