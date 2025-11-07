# Automated arXiv Paper Tracker

This repository is my personal, automated paper tracker. It uses a GitHub Action to run a Python script every 24 hours, scraping [arXiv.org](https://arxiv.org/) for new papers that match my interests.

The keywords I'm currently tracking are defined in `config.ini`.

## Latest Papers Found

*This section is automatically updated by the script every 24 hours.*

<!-- LATEST_PAPERS_START -->

# Papers Found on: 2025-11-07

### Unclonable Cryptography in Linear Quantum Memory
* **Authors:** Omri Shmueli et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04633v1
* **Abstract:** Quantum cryptography is a rapidly-developing area which leverages quantum information to accomplish classically-impossible tasks. In many of these protocols, quantum states are used as long-term cryptographic keys. Typically, this is to ensure the keys cannot be copied by an adversary, owing to the quantum no-cloning theorem. Unfortunately, due to quantum state's tendency to decohere, persistent quantum memory will likely be one of the most challenging resources for quantum computers. As such, it will be important to minimize persistent memory in quantum protocols.   In this work, we consider the case of one-shot signatures (OSS), and more general quantum signing tokens. These are important unclonable primitives, where quantum signing keys allow for signing a single message but not two. Naturally, these quantum signing keys would require storage in long-term quantum memory. Very recently, the first OSS was constructed in a classical oracle model and also in the standard model, but we observe that the quantum memory required for these protocols is quite large. In this work, we significantly decrease the quantum secret key size, in some cases achieving asymptotically optimal size. To do so, we develop novel techniques for proving the security of cryptosystems using coset states, which are one of the main tools used in unclonable cryptography.

### Qubit Mapping and Routing tailored to Advanced Quantum ISAs: Not as Costly as You Think
* **Authors:** Zhaohui Yang et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04608v1
* **Abstract:** Qubit mapping/routing is a critical stage in compilation for both near-term and fault-tolerant quantum computers, yet existing scalable methods typically impose several times the routing overhead in terms of circuit depth or duration. This inefficiency stems from a fundamental disconnect: compilers rely on an abstract routing model (e.g., three-$ \mathrm{CX} $-unrolled SWAP insertion) that completely ignores the idiosyncrasies of native gates supported by physical devices.   Recent hardware breakthroughs have enabled high-precision implementations of diverse instruction set architectures (ISAs) beyond standard $\mathrm{CX}$-based gates. Advanced ISAs involving gates such as $\mathrm{\sqrt{iSWAP}}$ and $\mathrm{ZZ}(\theta)$ gates offer superior circuit synthesis capabilities and can be realized with higher fidelities. However, systematic compiler optimization strategies tailored to these advanced ISAs are lacking.   To address this, we propose Canopus, a unified qubit mapping/routing framework applicable to diverse quantum ISAs. Built upon the canonical representation of two-qubit gates, Canopus centers on qubit routing to perform deep co-optimization in an ISA-aware approach. Canopus leverages the two-qubit canonical representation and the monodromy polytope to model the synthesis cost for more intelligent $ \mathrm{SWAP} $ insertion during the routing stage. We also formalize the commutation relations between two-qubit gates through the canonical form, providing a generalized approach to commutativity-based optimizations. Experiments show that Canopus consistently reduces routing overhead by 15\%-35\% compared to state-of-the-art methods across different ISAs and topologies. Our work also presents a coherent method for co-exploration of program patterns, quantum ISAs, and hardware topologies.

### Double-bracket quantum algorithms for high-fidelity ground state preparation
* **Authors:** Matteo Robbiati et al.
* **Published (v1):** 2024-08-07
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2408.03987v2
* **Abstract:** Ground state preparation is a central application for quantum computers but remains challenging in practice. In this work, we quantitatively investigate the performance and gate counts of double-bracket quantum algorithms (DBQAs) for ground state preparation. We propose a practical strategy in which DBQAs refine initial state preparation circuits, and we compile them for Heisenberg chains using controlled-Z and single-qubit gates. Warm-started DBQAs consistently improve both the energy and ground-state fidelity relative to the initial states provided by variational ans\"atze, indicating that DBQAs offer an effective unitary synthesis method. To demonstrate compatibility with near-term hardware, we executed a proof-of-concept example on IBM devices. With error mitigation, we observed a statistically significant improvement over the corresponding warm-start circuit. Furthermore, numerical emulations for the same system size indicate that executing DBQAs on Quantinuum's hardware could achieve similar cost-function gains without requiring error mitigation. These findings suggest that DBQAs are a promising approach for enhancing ground-state approximations on near-term quantum devices.

### QCircuitBench: A Large-Scale Dataset for Benchmarking Quantum Algorithm Design
* **Authors:** Rui Yang et al.
* **Published (v1):** 2024-10-10
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2410.07961v2
* **Abstract:** Quantum computing is an emerging field recognized for the significant speedup it offers over classical computing through quantum algorithms. However, designing and implementing quantum algorithms pose challenges due to the complex nature of quantum mechanics and the necessity for precise control over quantum states. Despite the significant advancements in AI, there has been a lack of datasets specifically tailored for this purpose. In this work, we introduce QCircuitBench, the first benchmark dataset designed to evaluate AI's capability in designing and implementing quantum algorithms using quantum programming languages. Unlike using AI for writing traditional codes, this task is fundamentally more complicated due to highly flexible design space. Our key contributions include: 1. A general framework which formulates the key features of quantum algorithm design for Large Language Models. 2. Implementations for quantum algorithms from basic primitives to advanced applications, spanning 3 task suites, 25 algorithms, and 120,290 data points. 3. Automatic validation and verification functions, allowing for iterative evaluation and interactive reasoning without human inspection. 4. Promising potential as a training dataset through preliminary fine-tuning results. We observed several interesting experimental phenomena: LLMs tend to exhibit consistent error patterns, and fine-tuning does not always outperform few-shot learning. In all, QCircuitBench is a comprehensive benchmark for LLM-driven quantum algorithm design, and it reveals limitations of LLMs in this domain.

### Minimum measurements quantum protocol for band structure calculation
* **Authors:** Michal Krejčí et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04389v1
* **Abstract:** Protocols for quantum measurement are an essential part of quantum computing. Measurements are no longer confined to the final step of computation but are increasingly embedded within quantum circuits as integral components of noise-resilient algorithms. However, each observable typically requires a distinct measurement basis, often demanding a different circuit configuration. As the number of such configurations typically grows with the number of qubits, different measurement configurations constitute a major bottleneck. Focusing on electronic structure calculations in crystalline systems, we propose a measurement protocol that maximally reduces the number of measurement settings to just three, independent of the number of qubits. This makes it one of the few known protocols that do not scale with qubit number. In particular, we derive the measurement protocol from the symmetries of tight-binding (TB) Hamiltonians and implement it within the Variational Quantum Deflation (VQD) algorithm. We demonstrate its performance on two systems, namely a two-dimensional CuO$_2$ square lattice (3 qubits) and bilayer graphene (4 qubits). The protocol can be generalized to more complex many-body Hamiltonians with high symmetry, providing a potential path toward future demonstrations of quantum advantage.

### Neutral-atom quantum computation using multi-qubit geometric gates via adiabatic passage
* **Authors:** Sinchan Snigdha Rej et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04359v1
* **Abstract:** Adiabatic geometric phase gates offer enhanced robustness against fluctuations compared to con- ventional Rydberg blockade-based phase gates that rely on dynamical phase accumulation. We theoretically demonstrate two- and multi-qubit phase gates in a neutral atom architecture, relying on a double stimulated Raman adiabatic passage (double-STIRAP) pulse sequence that imprints a controllable geometric phase on the qubit systems. The system is designed in such a way that every atom is individually addressable, and moreover, no extra laser is required to be applied on the target atom while scaling up the system from two- to multi-qubit quantum gates. The gate fidelity has been numerically analyzed by changing the gate operation time, and we find that 98% to 99% fidelity can be achieved for gate time $\simeq$ 0.6 $\mu$s. We perform a systematic error analysis, which re- veals that our proposed gates can exhibit strong resilience against fluctuations in Rabi frequencies, finite blockade strength, and atomic position variations. These results establish our approach as a physically feasible and scalable pathway toward fault-tolerant quantum computation with neutral atoms. We simulate Grover's search algorithm for two-, three-, and four-qubit systems with high success probability and thereby demonstrate the utility and scalability of our proposed gates for quantum computation.

### Gauge invariance from quantum information principles
* **Authors:** Claudia Núñez et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04358v1
* **Abstract:** Entanglement is a hallmark of quantum theory, yet it alone does not capture the full extent of quantum complexity: some highly entangled states can still be classically simulated. Non-classical behavior also requires magic, the non-Clifford component that enables universal quantum computation. Here, we investigate whether the interplay between entanglement and magic constrains the structure of fundamental interactions. We study gluon-gluon and graviton-graviton scattering at tree level, explicitly breaking gauge and general covariance by modifying the quartic vertices and analyzing the resulting generation of entanglement and magic. We find that imposing maximal entanglement (MaxEnt) alone does not uniquely recover gauge-invariant and diffeomorphism-invariant interactions, but adding the condition of minimal, but nonzero, magic singles it out. Our results indicate that nature favors MaxEnt and low magic: maximal quantum correlations with limited non-Cliffordness, sufficient for universal quantum computing but close to classical simulability. This dual informational principle may underlie the emergence of gauge invariance in fundamental physics.

### Low-Level and NUMA-Aware Optimization for High-Performance Quantum Simulation
* **Authors:** Ali Rezaei et al.
* **Published (v1):** 2025-06-10
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2506.09198v2
* **Abstract:** Scalable classical simulation of quantum circuits is crucial for advancing quantum algorithm development and validating emerging hardware. This work focuses on performance enhancements through targeted low-level and NUMA-aware tuning on a single-node system, thereby not only advancing the efficiency of classical quantum simulations but also establishing a foundation for scalable, heterogeneous implementations that bridge toward noiseless quantum computing. Although few prior studies have reported similar hardware-level optimizations, such implementations have not been released as open-source software, limiting independent validation and further development. We introduce an open-source, high-performance extension to the QuEST state vector simulator that integrates state-of-the-art low-level and NUMA-aware optimizations for modern processors. Our approach emphasizes locality-aware computation and incorporates hardware-specific techniques including NUMA-aware memory allocation, thread pinning, AVX-512 vectorization, aggressive loop unrolling, and explicit memory prefetching. Experiments demonstrate substantial speedups--5.5-6.5x for single-qubit gate operations, 4.5x for two-qubit gates, 4x for Random Quantum Circuits (RQC), and 1.8x for the Quantum Fourier Transform (QFT). Algorithmic workloads further achieve 4.3-4.6x acceleration for Grover and 2.5x for Shor-like circuits. These results show that systematic, architecture-aware tuning can significantly extend the practical simulation capacity of classical quantum simulators on current hardware.

### Cluster States Generation with a Quantum Metasurface
* **Authors:** Yehonatan Levin et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04297v1
* **Abstract:** We investigate the implementation of photonic cluster state generation protocols using quantum metasurfaces comprising sub-wavelength atomic arrays which enables quantum-controlled reflectivity. These cluster states are generated using fundamental quantum logic gates and enable wide-ranging applications in quantum computation and communication. In the past few years, certain protocols have been developed, but their physical realizations induces natural losses on the system mainly originated from coupling the photonic structures, setting a limit on the efficiency and maximal qubit number. In this paper, we examine a physical implementation of two specific protocols for generating distinct cluster states: a two-dimensional cluster state and a tree cluster state. Our approach leverages the unique properties of a quantum metasurface and its free space settings to implement two-qubit quantum-logic gates, namely CNOT, CZ, and E gates, with practical fidelities exceeding 0.9, and potential speed-up due to parallelism. In addition, we analyze these protocols fidelities for practical conditions of potential implementation experiments, such as thermal fluctuation of trapped atoms.

### Two-photon interference between mutually-detuned resonance fluorescence signals scattered off a semiconductor quantum dot
* **Authors:** Guoqi Huang et al.
* **Published (v1):** 2025-01-28
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2501.16939v3
* **Abstract:** The radiative linewidth of a two-level emitter (TLE) fundamentally limits the bandwidth available for quantum information processing. Despite its importance, no prior experiment has systematically examined how driving detuning affects the indistinguishability of photons scattered from a TLE - a parameter critical for photonic quantum computing. Here, we perform post-selective two-photon interference measurements between mutually detuned resonance fluorescence signals from an InAs quantum dot embedded in a micropillar cavity. At small mutual laser detunings (<=0.5GHz), the results are accurately described by the pure-state model [Nat. Commun. 16, 6453 (2025)], which treats all resonance-fluorescence photons as spontaneous emission. At larger detunings, we uncover an anomalous feature in the two-photon interference, where the normalised second-order correlation function under orthogonal polarisations yields g2_vert(0) < 0.5.

### Quantum time-marching algorithms for solving linear transport problems including boundary conditions
* **Authors:** Sergio Bengoechea et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04271v1
* **Abstract:** This article presents the first complete application of a quantum time-marching algorithm for simulating multidimensional linear transport phenomena with arbitrary boundaries, whereby the success probabilities are problem intrinsic. The method adapts the linear combination of unitaries algorithm to block encode the diffusive dynamics, while arbitrary boundary conditions are enforced by the method of images only at the cost of one additional qubit per spatial dimension. As an alternative to the non-periodic reflection, the direct encoding of Neumann conditions by the unitary decomposition of the discrete time-marching operator is proposed. All presented algorithms indicate optimal success probabilities while maintaining linear time complexity, thereby securing the practical applicability of the quantum algorithm on fault-tolerant quantum computers. The proposed time-marching method is demonstrated through state-vector simulations of the heat equation in combination with Neumann, Dirichlet, and mixed boundary conditions.

### Space-Bounded Communication Complexity of Unitaries
* **Authors:** Longcheng Li et al.
* **Published (v1):** 2025-11-06
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2511.04250v1
* **Abstract:** We study space-bounded communication complexity for unitary implementation in distributed quantum processors, where we restrict the number of qubits per processor to ensure practical relevance and technical non-triviality. We model distributed quantum processors using distributed quantum circuits with nonlocal two-qubit gates, defining the communication complexity of a unitary as the minimum number of such nonlocal gates required for its realization.   Our contributions are twofold. First, for general $n$-qubit unitaries, we improve upon the trivial $O(4^n)$ communication bound. Considering $k$ pairwise-connected processors (each with $n/k$ data qubits and $m$ ancillas), we prove the communication complexity satisfies $O\left(\max\{4^{(1-1/k)n - m}, n\}\right)$--for example, $O(2^n)$ when $m=0$ and $k=2$--and establish the tightness of this upper bound. We further extend the analysis to approximation models and general network topologies. Second, for special unitaries, we show that both the Quantum Fourier Transform (QFT) and Clifford circuits admit linear upper bounds on communication complexity in the exact model, outperforming the trivial quadratic bounds applicable to these cases. In the approximation model, QFT's communication complexity reduces drastically from linear to logarithmic, while Clifford circuits retain a linear lower bound. These results offer fundamental insights for optimizing communication in distributed quantum unitary implementation, advancing the feasibility of large-scale distributed quantum computing (DQC) systems.

### Approximate Quadratization of High-Order Hamiltonians for Combinatorial Quantum Optimization
* **Authors:** Sabina Drăgoi et al.
* **Published (v1):** 2025-05-07
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2505.04700v2
* **Abstract:** Combinatorial optimization problems have wide-ranging applications in industry and academia. Quantum computers may help solve them by sampling from carefully prepared Ansatz quantum circuits. However, current quantum computers are limited by their qubit count, connectivity, and noise. This is particularly restrictive when considering optimization problems beyond the quadratic order. Here, we introduce Ansatze based on an approximate quadratization of high-order Hamiltonians which do not incur a qubit overhead. The price paid is a loss in the quality of the noiseless solution. Crucially, this approximation yields shallower Ansatze which are more robust to noise than the standard QAOA one. We show this through simulations of systems of 8 to 16 qubits with variable noise strengths. Furthermore, we also propose a noise-aware Ansatz design method for quadratic optimization problems. This method implements only part of the corresponding Hamiltonian by limiting the number of layers of SWAP gates in the Ansatz. We find that for both problem types, under noise, our approximate implementation of the full problem structure can significantly enhance the solution quality. Our work opens a path to enhance the solution quality that approximate quantum optimization achieves on noisy hardware.

### Bridging Quantum Computing and Nuclear Structure: Atomic Nuclei on a Trapped-Ion Quantum Computer
* **Authors:** Sota Yoshida et al.
* **Published (v1):** 2025-09-25
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2509.20642v2
* **Abstract:** We demonstrate quantum simulations of strongly correlated nuclear many-body systems on the RIKEN-Quantinuum Reimei trapped-ion quantum computer, targeting ground states of oxygen, calcium, and nickel isotopes. By combining a hard-core-boson representation of the nuclear shell model with a pair-unitary coupled-cluster doubles ansatz, we achieve sub-percent relative error in the ground-state energies compared to noise-free statevector simulations. Our approach leverages symmetry-aware state preparation and particle-number post-selection to efficiently capture pairing correlations characteristic of systems with same-species nucleons. These findings highlight the viability of high-fidelity trapped-ion platforms for nuclear physics applications and provide a foundation for scaling to more complex nuclear systems.

### Performance Evaluations of Signed and Unsigned Noisy Approximate Quantum Fourier Arithmetic
* **Authors:** Robert A. M. Basili et al.
* **Published (v1):** 2021-12-17
* **Updated:** 2025-11-06
* **Link:** http://arxiv.org/abs/2112.09349v2
* **Abstract:** The Quantum Fourier Transform (QFT) grants competitive advantages, especially in resource usage and circuit approximation, for performing arithmetic operations on quantum computers, and offers a potential route towards a numerical quantum-computational paradigm. In this paper, we utilize efficient techniques to implement QFT-based integer addition and multiplications. These operations are fundamental to various quantum applications including Shor's algorithm, weighted sum optimization problems in data processing and machine learning, and quantum algorithms requiring inner products. We carry out performance evaluations of these implementations based on IBM's superconducting qubit architecture using different compatible noise models. We isolate the sensitivity of the component quantum circuits on both one-/two-qubit gate error rates, and the number of the arithmetic operands' superposed integer states. We analyze performance, and identify the most effective approximation depths for unsigned quantum addition and quantum multiplication within the given context. We then perform a similar analysis of signed addition and compare to the unsigned results. We observe significant dependency of the optimal approximation depth on the degree of machine noise and the number of superposed states in certain performance regimes. Finally, we elaborate on the algorithmic challenges - relevant to signed, unsigned, modular and non-modular versions - that could also be applied to current implementations of QFT-based subtraction, division, exponentiation, and their potential tensor extensions. We analyze the performance trends in our results and speculate on possible future developments within this computational paradigm.

<!-- LATEST_PAPERS_END -->

## Full Archive

A complete, persistent JSON database of all papers found by this tracker is available in the `data/archive.json` file.