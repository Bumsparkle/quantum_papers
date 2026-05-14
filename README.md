

# Papers Found on: 2026-05-14

### Computing eigenpairs of quantum many-body systems with Polfed.jl
* **Authors:** Rok Pintar et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-13
* **Link:** http://arxiv.org/abs/2605.10191v2
* **Abstract:** We present Polfed$.$jl, an open-source Julia package implementing the Polynomially Filtered Exact Diagonalization (POLFED) algorithm for computing mid-spectrum eigenvalues and eigenvectors (shortly, eigenpairs) of quantum many-body Hamiltonians. Access to such eigenpairs is essential for studying non-equilibrium many-body physics, but is hindered by the exponential growth of Hilbert-space dimension. POLFED addresses this challenge through a polynomial spectral transformation evaluated on the fly within a Lanczos iteration, preserving Hamiltonian sparsity and substantially reducing memory costs compared to other diagonalization methods. The package supports flexible energy targeting, automatic optimization of the spectral mapping for structured Hamiltonians, and GPU acceleration, which is particularly effective since the dominant computational cost reduces to repeated sparse matrix-vector multiplications. Benchmarks on disordered spin-chain and fermionic models demonstrate access to larger system sizes than alternative approaches, and CPU--GPU comparisons confirm significant speedups. In particular, we also provide code for constructing the quantum sun model Hamiltonian, a toy model of a many-body ergodicity-breaking transition. While our focus is on many-body Hamiltonians, Polfed$.$jl may be applied to any large sparse matrix.

### FusionRCG: Orchestrating Recursive Computation Graphs across GPU Memory Hierarchies
* **Authors:** Yihong Zhang et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-13
* **Link:** http://arxiv.org/abs/2605.10312v2
* **Abstract:** Evaluating high-dimensional integrals via deep hierarchical recurrences is a dominant cost in quantum chemistry. While CPUs manage these efficiently, GPUs suffer a critical mismatch: limited per-thread memory is quickly overwhelmed by an explosion of simultaneously live intermediate variables. As recurrence scales, this forces massive data spilling to global memory, collapsing performance into a severe memory-bound regime. We present FusionRCG, a framework that jointly optimizes computation graph structure and GPU memory mapping. Exploiting the inherent topological flexibility of recurrence graphs, using electron repulsion integrals as an example, we contribute: (1) liveness-aware graph orchestration to minimize peak live intermediates; (2) algebraic dimensionality reduction via stepwise Cartesian-to-spherical fusion, shrinking intermediate footprints by up to $7.7\times$; and (3) an adaptive multi-tier kernel architecture routing graphs across the memory hierarchy. Evaluated on NVIDIA A100 GPUs, FusionRCG achieves up to $3.09\times$ end-to-end SCF speedup over GPU4PySCF and maintains $75\%$ parallel efficiency at 64~GPUs, successfully rescuing these workloads from memory-bound limits.



# Papers Found on: 2026-05-14

### Computing eigenpairs of quantum many-body systems with Polfed.jl
* **Authors:** Rok Pintar et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-13
* **Link:** http://arxiv.org/abs/2605.10191v2
* **Abstract:** We present Polfed$.$jl, an open-source Julia package implementing the Polynomially Filtered Exact Diagonalization (POLFED) algorithm for computing mid-spectrum eigenvalues and eigenvectors (shortly, eigenpairs) of quantum many-body Hamiltonians. Access to such eigenpairs is essential for studying non-equilibrium many-body physics, but is hindered by the exponential growth of Hilbert-space dimension. POLFED addresses this challenge through a polynomial spectral transformation evaluated on the fly within a Lanczos iteration, preserving Hamiltonian sparsity and substantially reducing memory costs compared to other diagonalization methods. The package supports flexible energy targeting, automatic optimization of the spectral mapping for structured Hamiltonians, and GPU acceleration, which is particularly effective since the dominant computational cost reduces to repeated sparse matrix-vector multiplications. Benchmarks on disordered spin-chain and fermionic models demonstrate access to larger system sizes than alternative approaches, and CPU--GPU comparisons confirm significant speedups. In particular, we also provide code for constructing the quantum sun model Hamiltonian, a toy model of a many-body ergodicity-breaking transition. While our focus is on many-body Hamiltonians, Polfed$.$jl may be applied to any large sparse matrix.

### FusionRCG: Orchestrating Recursive Computation Graphs across GPU Memory Hierarchies
* **Authors:** Yihong Zhang et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-13
* **Link:** http://arxiv.org/abs/2605.10312v2
* **Abstract:** Evaluating high-dimensional integrals via deep hierarchical recurrences is a dominant cost in quantum chemistry. While CPUs manage these efficiently, GPUs suffer a critical mismatch: limited per-thread memory is quickly overwhelmed by an explosion of simultaneously live intermediate variables. As recurrence scales, this forces massive data spilling to global memory, collapsing performance into a severe memory-bound regime. We present FusionRCG, a framework that jointly optimizes computation graph structure and GPU memory mapping. Exploiting the inherent topological flexibility of recurrence graphs, using electron repulsion integrals as an example, we contribute: (1) liveness-aware graph orchestration to minimize peak live intermediates; (2) algebraic dimensionality reduction via stepwise Cartesian-to-spherical fusion, shrinking intermediate footprints by up to $7.7\times$; and (3) an adaptive multi-tier kernel architecture routing graphs across the memory hierarchy. Evaluated on NVIDIA A100 GPUs, FusionRCG achieves up to $3.09\times$ end-to-end SCF speedup over GPU4PySCF and maintains $75\%$ parallel efficiency at 64~GPUs, successfully rescuing these workloads from memory-bound limits.

