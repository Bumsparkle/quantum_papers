# Papers Found on: 2026-01-13

### Mechanical Resonator-based Quantum Computing
* **Authors:** Yu Yang et al.
* **Published (v1):** 2026-01-12
* **Updated:** 2026-01-12
* **Link:** http://arxiv.org/abs/2601.07825v1
* **Abstract:** Hybrid quantum systems combine the unique advantages of different physical platforms with the goal of realizing more powerful and practical quantum information processing devices. Mechanical systems, such as bulk acoustic wave resonators, feature a large number of highly coherent harmonic modes in a compact footprint, which complements the strong nonlinearities and fast operation times of superconducting quantum circuits. Here, we demonstrate an architecture for mechanical resonator-based quantum computing, in which a superconducting qubit is used to perform quantum gates on a collection of mechanical modes. We show the implementation of a universal gate set, composed of single-qubit gates and controlled arbitrary-phase gates, and showcase their use in the quantum Fourier transform and quantum period finding algorithms. These results pave the way toward using mechanical systems to build crucial components for future quantum technologies, such as quantum random-access memories.

### Computing quantum magic of state vectors
* **Authors:** Piotr Sierant et al.
* **Published (v1):** 2026-01-12
* **Updated:** 2026-01-12
* **Link:** http://arxiv.org/abs/2601.07824v1
* **Abstract:** Non-stabilizerness, also known as ``magic,'' quantifies how far a quantum state departs from the stabilizer set. It is a central resource behind quantum advantage and a useful probe of the complexity of many-body quantum states. Yet standard magic quantifiers, such as the stabilizer Rényi entropy (SRE) for qubits and the mana for qutrits, are costly to evaluate numerically, with the computational complexity growing rapidly with the number $N$ of qudits. Here we introduce efficient, numerically exact algorithms that exploit the fast Hadamard transform to compute the SRE for qubits ($d=2$) and the mana for qutrits ($d=3$) for pure states given as state vectors. Our methods reduce the runtime to $O(N d^{2N})$, an exponential improvement over the naive $O(d^{3N})$ scaling, while exposing substantial parallelism and enabling GPU acceleration. We further show how to combine the fast Hadamard transform with Monte Carlo sampling to estimate the SRE of state vectors, and we extend the approach to compute the mana of mixed states. All algorithms are implemented in the open-source Julia package HadaMAG.jl, which provides a high-performance, GPU-enabled toolbox for computing SRE and mana. The package, together with the methods developed in this work, offers a practical route to large-scale numerical studies of magic in quantum many-body systems.

### Measurement-based acceleration of optical computations
* **Authors:** I. V. Vovchenko et al.
* **Published (v1):** 2026-01-12
* **Updated:** 2026-01-12
* **Link:** http://arxiv.org/abs/2601.07814v1
* **Abstract:** Analog coprocessors are intensively developing nowadays with the aim to optimize energy computations of neural networks. In this work we focus on the possibility of using detection of collective oscillations in optical systems for computational purposes. We show that in a system of coupled resonators, collective oscillations can be used to implement matrix-vector multiplication. The matrix is formed by the coupling constants between the resonators, and the input vector is formed by the initial occupancies of the involved modes. The frequency of the collective oscillations is growing with the number of the involved modes, similarly to Rabi oscillations. The time needed for their detection, i.e., averaging, decreases with an increase in the input vector dimension. We discuss the limitations imposed on parallel computation in the system by restriction of the allowed optical frequency band.

### Thermodynamic Recycling in Quantum Computing: Demonstration Using the Harrow-Hassidim-Lloyd Algorithm and Information Erasure
* **Authors:** Nobumasa Ishida et al.
* **Published (v1):** 2026-01-12
* **Updated:** 2026-01-12
* **Link:** http://arxiv.org/abs/2601.07522v1
* **Abstract:** Branch selection, including postselection, is a standard method for implementing nonunitary transformations in quantum algorithms. Conventionally, states associated with unsuccessful branches are discarded and treated as useless. Here we propose a generic framework that reuses these failure branches as thermodynamic resources. The central element is an athermal bath that is naturally generated during the reset of a failure branch. By coupling this bath to a target system prior to relaxation, useful thermodynamic tasks can be performed, enabling performance beyond conventional thermodynamic limits. As an application, we analyze information erasure and derive the resulting gain analytically. We further demonstrate the framework by implementing the Harrow-Hassidim-Lloyd algorithm on IBM's superconducting quantum processor. Despite substantial noise and errors in current hardware, our method achieves erasure with heat dissipation below the Landauer limit. These results establish a practical connection between quantum computing and quantum thermodynamics and suggest a route toward reducing thermodynamic costs in future large-scale quantum computers.

### Fault-tolerant modular quantum computing with surface codes using single-shot emission-based hardware
* **Authors:** Siddhant Singh et al.
* **Published (v1):** 2026-01-12
* **Updated:** 2026-01-12
* **Link:** http://arxiv.org/abs/2601.07241v1
* **Abstract:** Fault-tolerant modular quantum computing requires stabilizer measurements across the modules in a quantum network. For this, entangled states of high quality and rate must be distributed. Currently, two main types of entanglement distribution protocols exist, namely emission-based and scattering-based, each with its own advantages and drawbacks. On the one hand, scattering-based protocols with cavities or waveguides are fast but demand stringent hardware such as high-efficiency integrated circulators or strong waveguide coupling. On the other hand, emission-based platforms are experimentally feasible but so far rely on Bell-pair fusion with extensive use of slow two-qubit memory gates, limiting thresholds to $\approx 0.16\%$. Here, we consider a fully distributed surface code using emission-based entanglement schemes that generate GHZ states in a single shot, i.e., without the need for Bell-pair fusions. We show that our optical setup produces Bell pairs, W states, and GHZ states, enabling both memory-based and optical protocols for distilling high-fidelity GHZ states with significantly improved success rates. Furthermore, we introduce protocols that completely eliminate the need for memory-based two-qubit gates, achieving thresholds of $\approx 0.19\%$ with modest hardware enhancements, increasing to above $\approx 0.24\%$ with photon-number-resolving detectors. These results show the feasibility of emission-based architectures for scalable fault-tolerant operation.

### Digital Predistortion of Power Amplifiers for Quantum Computing
* **Authors:** Marvin Jaeger et al.
* **Published (v1):** 2026-01-10
* **Updated:** 2026-01-10
* **Link:** http://arxiv.org/abs/2601.06524v1
* **Abstract:** Power amplifiers (PA) are essential for microwavecontrolled trapped-ion and semiconductor spin based quantum computers (QC). They adjust the power level of the control signal and therefore the processing time of the QC. Their nonlinearities and memory effects degrade the signal quality and, thus, the fidelity of qubit gate operations. Driving the PA with a significant input power back-off reduces nonlinear effects but is neither power-efficient nor cost-effective. To overcome this limitation, this letter augments the conventional signal generation system applied in QCs by digital predistortion (DPD) to linearize the radio frequency (RF) channel. Numerical analysis of the qubit behavior based on measured representative control signals indicates that DPD improves its fidelity.

### Algorithms for Computing the Petz-Augustin Capacity
* **Authors:** Chun-Neng Chu et al.
* **Published (v1):** 2026-01-10
* **Updated:** 2026-01-10
* **Link:** http://arxiv.org/abs/2601.06492v1
* **Abstract:** We propose the first algorithms with non-asymptotic convergence guarantees for computing the Petz-Augustin capacity, which generalizes the channel capacity and characterizes the optimal error exponent in classical-quantum channel coding. This capacity can be equivalently expressed as the maximization of two generalizations of mutual information: the Petz-Rényi information and the Petz-Augustin information. To maximize the Petz-Rényi information, we show that it corresponds to a convex Hölder-smooth optimization problem, and hence the universal fast gradient method of Nesterov (2015), along with its convergence guarantees, readily applies. Regarding the maximization of the Petz-Augustin information, we adopt a two-layered approach: we show that the objective function is smooth relative to the negative Shannon entropy and can be efficiently optimized by entropic mirror descent; each iteration of entropic mirror descent requires computing the Petz-Augustin information, for which we propose a novel fixed-point algorithm and establish its contractivity with respect to the Thompson metric. Notably, this two-layered approach can be viewed as a generalization of the mirror-descent interpretation of the Blahut-Arimoto algorithm due to He et al. (2024).

### Bipartitioning of Graph States for Distributed Measurement-Based Quantum Computing
* **Authors:** Kjell Fredrik Pettersen et al.
* **Published (v1):** 2026-01-09
* **Updated:** 2026-01-09
* **Link:** http://arxiv.org/abs/2601.06332v1
* **Abstract:** Measurement-Based Quantum Computing (MBQC) is inherently well-suited for Distributed Quantum Computing (DQC): once a resource state is prepared and distributed across a network of quantum nodes, computation proceeds through local measurements coordinated by classical communication. However, since non-local gates acting on different Quantum Processing Units (QPUs) are a bottleneck, it is crucial to optimize the qubit assignment to minimize inter-node entanglement of the shared resource. For graph state resources shared across two QPUs, this task reduces to finding bipartitions with minimal cut rank. We introduce a simulated annealing-based algorithm that efficiently updates the cut rank when two vertices swap sides across a bipartition, such that computing the new cut rank from scratch, which would be much more expensive, is not necessary. We show that the approach is highly effective for determining qubit assignments in distributed MBQC by testing it on grid graphs and the measurement-based Quantum Approximate Optimization Algorithm (QAOA).
