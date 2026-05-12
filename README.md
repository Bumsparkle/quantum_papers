

# Papers Found on: 2026-05-12

### Computation of entanglement for quantum states by a Consensus-Based Optimization method
* **Authors:** Michael Herty et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-11
* **Link:** http://arxiv.org/abs/2605.03773v2
* **Abstract:** The computation of quantum entanglement can be formulated as a high-dimensional nonconvex optimization problem with orthogonality constraints. In this work, we propose structure-preserving consensus-based optimization (CBO) methods for entanglement computation, with one approach based on a Hermitian formulation and the other evolving directly on the unitary manifold. To handle the variable dimension of the feasible set, we introduce a cross-dimensional interaction mechanism allowing exchange of information between particles of different sizes. Numerical experiments demonstrate that the proposed methods achieve accurate approximations.

### FusionRCG: Orchestrating Recursive Computation Graphs across GPU Memory Hierarchies
* **Authors:** Yihong Zhang et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-11
* **Link:** http://arxiv.org/abs/2605.10312v1
* **Abstract:** Evaluating high-dimensional integrals via deep hierarchical recurrences is a dominant cost in quantum chemistry. While CPUs manage these efficiently, GPUs suffer a critical mismatch: limited per-thread memory is quickly overwhelmed by an explosion of simultaneously live intermediate variables. As recurrence scales, this forces massive data spilling to global memory, collapsing performance into a severe memory-bound regime. We present FusionRCG, a framework that jointly optimizes computation graph structure and GPU memory mapping. Exploiting the inherent topological flexibility of recurrence graphs, using electron repulsion integrals as an example, we contribute: (1) liveness-aware graph orchestration to minimize peak live intermediates; (2) algebraic dimensionality reduction via stepwise Cartesian-to-spherical fusion, shrinking intermediate footprints by up to $7.7\times$; and (3) an adaptive multi-tier kernel architecture routing graphs across the memory hierarchy. Evaluated on NVIDIA A100 GPUs, FusionRCG achieves up to $3.09\times$ end-to-end SCF speedup over GPU4PySCF and maintains $75\%$ parallel efficiency at 64~GPUs, successfully rescuing these workloads from memory-bound limits.

### Computing eigenpairs of quantum many-body systems with Polfed.jl
* **Authors:** Rok Pintar et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-11
* **Link:** http://arxiv.org/abs/2605.10191v1
* **Abstract:** We present Polfed.jl, an open-source Julia package implementing the Polynomially Filtered Exact Diagonalization (POLFED) algorithm for computing mid-spectrum eigenvalues and eigenvectors (shortly, eigenpairs) of quantum many-body Hamiltonians. Access to such eigenpairs is essential for studying non-equilibrium many-body physics, but is hindered by the exponential growth of Hilbert-space dimension. POLFED addresses this challenge through a polynomial spectral transformation evaluated on the fly within a Lanczos iteration, preserving Hamiltonian sparsity and substantially reducing memory costs compared to other diagonalization methods. The package supports flexible energy targeting, automatic optimization of the spectral mapping for structured Hamiltonians, and GPU acceleration, which is particularly effective since the dominant computational cost reduces to repeated sparse matrix-vector multiplications. Benchmarks on disordered spin-chain and fermionic models demonstrate access to larger system sizes than alternative approaches, and CPU--GPU comparisons confirm significant speedups. In particular, we also provide code for constructing the quantum sun model Hamiltonian, a toy model of a many-body ergodicity-breaking transition. While our focus is on many-body Hamiltonians, Polfed.jl may be applied to any large sparse matrix.

### Estimating The Energy Consumption of Quantum Computing from A Full System Aspect
* **Authors:** Siyuan Niu et al.
* **Published (v1):** 2026-05-10
* **Updated:** 2026-05-10
* **Link:** http://arxiv.org/abs/2605.09580v1
* **Abstract:** Quantum computing promises disruptive capabilities, yet its energy footprint has received far less attention than its asymptotic speedups. We present a first-order, full-system energy model for quantum computing in an high performance computing (HPC) context. The model separates costs common to NISQ and FTQC, such as system maintenance and classical processing, from regime-specific ones such as error mitigation for NISQ and error correction for FTQC. We instantiate the model on 96- and 100-qubit Heisenberg time-evolution simulations on IBM Eagle r3 and a representative VQE workload, and sketch the FTQC energy pipeline. We find that NISQ energy is dominated by the QEM sampling multiplier, while FTQC cost shifts to physical-qubit overhead set by the code distance and magic states. Our model provides actionable insights into the energy consumption of both NISQ and FTQC workloads, and paves the way toward energy-efficient quantum advantage.

### Protocol for Efficient Generation of Fusion-Based Quantum Computing Resource States from Quantum Emitters
* **Authors:** Nishad Manohar et al.
* **Published (v1):** 2026-05-10
* **Updated:** 2026-05-10
* **Link:** http://arxiv.org/abs/2605.09325v1
* **Abstract:** Fusion-based quantum computing (FBQC) relies on a set of small, typically photonic, resource states that are fused together through Bell state measurements. The main bottleneck of FBQC is the low rate of generating the resource states, which stems from the probabilistic nature of photonic fusion gates. Previous work introduced a general algorithm for constructing circuits that deterministically generate photonic resource states from a minimal number of quantum emitters for a specified photon emission ordering. However, finding the minimal number of emitters and CNOT gates across all possible orderings is an NP-hard problem. Here, we exploit the symmetries present in FBQC resource states to dramatically simplify this optimization problem. We find that logically encoded 24-photon FBQC resource states can be produced using as few as 3 emitters and 11 CNOTs.

### Efficient and Stable Computation of Gravitational-Wave Fluxes from Generic Kerr Orbits via a Unified HeunC Framework
* **Authors:** Changkai Chen et al.
* **Published (v1):** 2026-05-10
* **Updated:** 2026-05-10
* **Link:** http://arxiv.org/abs/2605.09250v1
* **Abstract:** Modeling extreme-mass-ratio inspirals hinges on the accurate and efficient computation of gravitational-wave fluxes from generic Kerr orbits. Conventional frequency-domain techniques are often limited by costly auxiliary parameter searches and numerical instabilities in the strong-field or high-frequency regimes. We address these challenges by reformulating both the angular and radial Teukolsky equations in terms of confluent Heun functions. Employing a hybrid analytic continuation algorithm to compute the connection coefficients eliminates the dependence on auxiliary parameters, directly yielding globally convergent solutions and scattering amplitudes. To resolve the highly oscillatory source integrands for generic orbits, we implement an adaptive bi-power mapping quadrature. Comprehensive benchmarks under standard double-precision arithmetic demonstrate that, for the total radiative flux summed over 168 low-order modes, our method achieves relative errors of order $10^{-11}$, with computational costs typically reduced by factors of 2--3 and 3--10 compared to the state-of-the-art \texttt{GeneralizedSasakiNakamura.jl} and \texttt{pybhpt} packages, respectively. These demonstrated gains in precision and efficiency establish the framework as a robust tool for strong-field perturbation theory, providing the numerical foundation for high-order self-force calculations and rapid, high-precision waveform generation.

### Nonlinear Coherent Transport in 2D Thermal Metamaterials: From Solitons and Topological Defects to Quantum Computing
* **Authors:** R. A. C. Correa et al.
* **Published (v1):** 2026-05-04
* **Updated:** 2026-05-04
* **Link:** http://arxiv.org/abs/2605.08162v1
* **Abstract:** Understanding heat transport in low-dimensional and nano-architectured materials remains a central challenge in nonequilibrium statistical physics due to persistent deviations from Fourier's law. These deviations are driven by anharmonicity, reduced dimensionality, and the emergence of long-lived coherent excitations. In this work, we develop a unified theoretical framework for two-dimensional thermal metamaterials that combines nonlinear lattice dynamics, soliton-based effective field theories, and geometrically organized defect networks as guiding structures for energy flow. We introduce minimal discrete and continuum-inspired models suitable for controlled benchmarking of thermal transport in patterned two-dimensional architectures and identify a two-channel transport mechanism in which coherent nonlinear excitations coexist with incoherent hydrodynamic modes. The interplay between these channels is shown to be highly sensitive to geometry, nonlinearity, and temperature, offering new avenues for thermal management. We establish rigorous connections between microscopic nonlinearity, geometry-driven channeling of heat in two dimensions, and quantum-enabled exploration of both high-occupation classical regimes and genuinely quantum regimes beyond the reach of standard simulation strategies. The theoretical predictions are corroborated by recent experimental and computational results in Stone-Wales-defected PdSSe monolayers and silicon phononic crystal nanostructures, which exhibit ultra-low thermal conductivity coexisting with high carrier mobility and strong anisotropy -- direct manifestations of the two-channel mechanism. This synthesis provides actionable guidance for the design of engineered heat-spreading architectures and positions quantum simulation as a transformative tool for advancing the theory of nonlinear heat transport.



# Papers Found on: 2026-05-12

### Computation of entanglement for quantum states by a Consensus-Based Optimization method
* **Authors:** Michael Herty et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-11
* **Link:** http://arxiv.org/abs/2605.03773v2
* **Abstract:** The computation of quantum entanglement can be formulated as a high-dimensional nonconvex optimization problem with orthogonality constraints. In this work, we propose structure-preserving consensus-based optimization (CBO) methods for entanglement computation, with one approach based on a Hermitian formulation and the other evolving directly on the unitary manifold. To handle the variable dimension of the feasible set, we introduce a cross-dimensional interaction mechanism allowing exchange of information between particles of different sizes. Numerical experiments demonstrate that the proposed methods achieve accurate approximations.

### FusionRCG: Orchestrating Recursive Computation Graphs across GPU Memory Hierarchies
* **Authors:** Yihong Zhang et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-11
* **Link:** http://arxiv.org/abs/2605.10312v1
* **Abstract:** Evaluating high-dimensional integrals via deep hierarchical recurrences is a dominant cost in quantum chemistry. While CPUs manage these efficiently, GPUs suffer a critical mismatch: limited per-thread memory is quickly overwhelmed by an explosion of simultaneously live intermediate variables. As recurrence scales, this forces massive data spilling to global memory, collapsing performance into a severe memory-bound regime. We present FusionRCG, a framework that jointly optimizes computation graph structure and GPU memory mapping. Exploiting the inherent topological flexibility of recurrence graphs, using electron repulsion integrals as an example, we contribute: (1) liveness-aware graph orchestration to minimize peak live intermediates; (2) algebraic dimensionality reduction via stepwise Cartesian-to-spherical fusion, shrinking intermediate footprints by up to $7.7\times$; and (3) an adaptive multi-tier kernel architecture routing graphs across the memory hierarchy. Evaluated on NVIDIA A100 GPUs, FusionRCG achieves up to $3.09\times$ end-to-end SCF speedup over GPU4PySCF and maintains $75\%$ parallel efficiency at 64~GPUs, successfully rescuing these workloads from memory-bound limits.

### Computing eigenpairs of quantum many-body systems with Polfed.jl
* **Authors:** Rok Pintar et al.
* **Published (v1):** 2026-05-11
* **Updated:** 2026-05-11
* **Link:** http://arxiv.org/abs/2605.10191v1
* **Abstract:** We present Polfed.jl, an open-source Julia package implementing the Polynomially Filtered Exact Diagonalization (POLFED) algorithm for computing mid-spectrum eigenvalues and eigenvectors (shortly, eigenpairs) of quantum many-body Hamiltonians. Access to such eigenpairs is essential for studying non-equilibrium many-body physics, but is hindered by the exponential growth of Hilbert-space dimension. POLFED addresses this challenge through a polynomial spectral transformation evaluated on the fly within a Lanczos iteration, preserving Hamiltonian sparsity and substantially reducing memory costs compared to other diagonalization methods. The package supports flexible energy targeting, automatic optimization of the spectral mapping for structured Hamiltonians, and GPU acceleration, which is particularly effective since the dominant computational cost reduces to repeated sparse matrix-vector multiplications. Benchmarks on disordered spin-chain and fermionic models demonstrate access to larger system sizes than alternative approaches, and CPU--GPU comparisons confirm significant speedups. In particular, we also provide code for constructing the quantum sun model Hamiltonian, a toy model of a many-body ergodicity-breaking transition. While our focus is on many-body Hamiltonians, Polfed.jl may be applied to any large sparse matrix.

### Estimating The Energy Consumption of Quantum Computing from A Full System Aspect
* **Authors:** Siyuan Niu et al.
* **Published (v1):** 2026-05-10
* **Updated:** 2026-05-10
* **Link:** http://arxiv.org/abs/2605.09580v1
* **Abstract:** Quantum computing promises disruptive capabilities, yet its energy footprint has received far less attention than its asymptotic speedups. We present a first-order, full-system energy model for quantum computing in an high performance computing (HPC) context. The model separates costs common to NISQ and FTQC, such as system maintenance and classical processing, from regime-specific ones such as error mitigation for NISQ and error correction for FTQC. We instantiate the model on 96- and 100-qubit Heisenberg time-evolution simulations on IBM Eagle r3 and a representative VQE workload, and sketch the FTQC energy pipeline. We find that NISQ energy is dominated by the QEM sampling multiplier, while FTQC cost shifts to physical-qubit overhead set by the code distance and magic states. Our model provides actionable insights into the energy consumption of both NISQ and FTQC workloads, and paves the way toward energy-efficient quantum advantage.

### Protocol for Efficient Generation of Fusion-Based Quantum Computing Resource States from Quantum Emitters
* **Authors:** Nishad Manohar et al.
* **Published (v1):** 2026-05-10
* **Updated:** 2026-05-10
* **Link:** http://arxiv.org/abs/2605.09325v1
* **Abstract:** Fusion-based quantum computing (FBQC) relies on a set of small, typically photonic, resource states that are fused together through Bell state measurements. The main bottleneck of FBQC is the low rate of generating the resource states, which stems from the probabilistic nature of photonic fusion gates. Previous work introduced a general algorithm for constructing circuits that deterministically generate photonic resource states from a minimal number of quantum emitters for a specified photon emission ordering. However, finding the minimal number of emitters and CNOT gates across all possible orderings is an NP-hard problem. Here, we exploit the symmetries present in FBQC resource states to dramatically simplify this optimization problem. We find that logically encoded 24-photon FBQC resource states can be produced using as few as 3 emitters and 11 CNOTs.

### Efficient and Stable Computation of Gravitational-Wave Fluxes from Generic Kerr Orbits via a Unified HeunC Framework
* **Authors:** Changkai Chen et al.
* **Published (v1):** 2026-05-10
* **Updated:** 2026-05-10
* **Link:** http://arxiv.org/abs/2605.09250v1
* **Abstract:** Modeling extreme-mass-ratio inspirals hinges on the accurate and efficient computation of gravitational-wave fluxes from generic Kerr orbits. Conventional frequency-domain techniques are often limited by costly auxiliary parameter searches and numerical instabilities in the strong-field or high-frequency regimes. We address these challenges by reformulating both the angular and radial Teukolsky equations in terms of confluent Heun functions. Employing a hybrid analytic continuation algorithm to compute the connection coefficients eliminates the dependence on auxiliary parameters, directly yielding globally convergent solutions and scattering amplitudes. To resolve the highly oscillatory source integrands for generic orbits, we implement an adaptive bi-power mapping quadrature. Comprehensive benchmarks under standard double-precision arithmetic demonstrate that, for the total radiative flux summed over 168 low-order modes, our method achieves relative errors of order $10^{-11}$, with computational costs typically reduced by factors of 2--3 and 3--10 compared to the state-of-the-art \texttt{GeneralizedSasakiNakamura.jl} and \texttt{pybhpt} packages, respectively. These demonstrated gains in precision and efficiency establish the framework as a robust tool for strong-field perturbation theory, providing the numerical foundation for high-order self-force calculations and rapid, high-precision waveform generation.

### Nonlinear Coherent Transport in 2D Thermal Metamaterials: From Solitons and Topological Defects to Quantum Computing
* **Authors:** R. A. C. Correa et al.
* **Published (v1):** 2026-05-04
* **Updated:** 2026-05-04
* **Link:** http://arxiv.org/abs/2605.08162v1
* **Abstract:** Understanding heat transport in low-dimensional and nano-architectured materials remains a central challenge in nonequilibrium statistical physics due to persistent deviations from Fourier's law. These deviations are driven by anharmonicity, reduced dimensionality, and the emergence of long-lived coherent excitations. In this work, we develop a unified theoretical framework for two-dimensional thermal metamaterials that combines nonlinear lattice dynamics, soliton-based effective field theories, and geometrically organized defect networks as guiding structures for energy flow. We introduce minimal discrete and continuum-inspired models suitable for controlled benchmarking of thermal transport in patterned two-dimensional architectures and identify a two-channel transport mechanism in which coherent nonlinear excitations coexist with incoherent hydrodynamic modes. The interplay between these channels is shown to be highly sensitive to geometry, nonlinearity, and temperature, offering new avenues for thermal management. We establish rigorous connections between microscopic nonlinearity, geometry-driven channeling of heat in two dimensions, and quantum-enabled exploration of both high-occupation classical regimes and genuinely quantum regimes beyond the reach of standard simulation strategies. The theoretical predictions are corroborated by recent experimental and computational results in Stone-Wales-defected PdSSe monolayers and silicon phononic crystal nanostructures, which exhibit ultra-low thermal conductivity coexisting with high carrier mobility and strong anisotropy -- direct manifestations of the two-channel mechanism. This synthesis provides actionable guidance for the design of engineered heat-spreading architectures and positions quantum simulation as a transformative tool for advancing the theory of nonlinear heat transport.

