# User Profile

## User Information
- **User Language:** English
- **Initial Assessment:** Dynamic Calibration Required: The user's level must be calibrated each session by observing the 'learning.log' and current interaction. Assume the user has gaps in understanding unless proven otherwise through rigorous reasoning. Calibration should happen incrementally, not as a one-time event.
- **Professional Skills/Goals:**
    - LLM architecture design
    - CUDA optimization readiness
    - AI Architect competency
- **Environment State:** Dual environment focus: High-VRAM GPU (4090ti) for training/optimization, and CPU-only (Debian 13) for efficiency/deployment analysis.

## Constraints & Strategy
### Hardware Limits
- Lenovo Legion 7 Pro with NVIDIA RTX 4090ti 16GB VRAM (Fedora 42)
- Debian 13 without GPU, 4 cores, 8 GB RAM.

### Software Stack
- Primary focus on PyTorch for implementation and CUDA/bare-metal concepts.

### Efficiency Principles
- Focus on algorithms working within constraints, specifically VRAM management (GPU) and latency (CPU).
