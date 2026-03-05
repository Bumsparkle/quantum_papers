

# Papers Found on: 2026-03-05

### HyQBench: A Benchmark Suite for Hybrid CV-DV Quantum Computing
* **Authors:** Shubdeep Mohapatra et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.04398v1
* **Abstract:** Hybrid continuous-variable (CV)-discrete-variable (DV) quantum systems present a promising direction for quantum computing by combining the high dimensional encoding capabilities of qumodes with the control offered by DV qubits on the coupled qumodes. There have been exciting recent progresses on hybrid CV-DV quantum computing, including variational algorithms, error correction, compiler-level optimizations for Hamiltonian simulation, etc. However, there is a lack of a standardized CV-DV benchmark suite for assessing various emerging hardware platforms and evaluating software optimizations on hybrid CV-DV circuits. In this work, we introduce a simulation and benchmarking framework for hybrid CV-DV circuits, implemented using Bosonic Qiskit-a tool specifically designed to model CV-DV systems, along with QuTip for functional correctness verification. We construct and characterize representative CV-DV benchmarks, including cat state generation, GKP state generation, CV-DV state transfers, hybrid quantum Fourier transform, variational quantum algorithms, Hamiltonian simulation, and Shor's algorithm. To assess circuit complexity and scalability, we define a feature map organized into two categories: general features (e.g., qubit/qumode count, gate counts) and CV-DV-specific features (e.g., Wigner negativity, energy, truncation cost). These metrics enable evaluation of both classical simulability and hardware resource requirements. Our results, including one benchmark on real hardware, demonstrate that hybrid CV-DV architectures are not only viable but well-suited for a range of computational tasks, from optimization to Hamiltonian simulation. This framework lays the groundwork for systematic evaluation and future development of hybrid quantum systems.

### Benchmarking Quantum Computers via Protocols, Comparing IBM's Heron vs IBM's Eagle
* **Authors:** Nitay Mayo et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.04377v1
* **Abstract:** As quantum computing hardware rapidly advances, objectively evaluating the capabilities and error rates of new processors remains a critical challenge for the field. A clear and realistic understanding of current quantum performance is essential to guide research priorities and drive meaningful progress. In this work, we apply and extend a protocol-based benchmarking methodology (presented in arXiv:2505.12441) that utilizes well-defined quantumness thresholds. By evaluating performance at protocol level rather then the gate level, this approach provides a transparent and intuitive assessment of whether specific quantum processors, or isolated sub-chips within them, can demonstrate a practical quantum advantage. To illustrate the utility of this method, we compare two generations of IBM quantum computers: the older Eagle architecture and the newer Heron architecture. Our findings reveal the genuine operational strengths and limitations of these devices, demonstrating substantial performance improvements in the newer Heron generation.

### Efficient Time-Aware Partitioning of Quantum Circuits for Distributed Quantum Computing
* **Authors:** Raymond P. H. Wu et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.04126v1
* **Abstract:** To overcome the physical limitations of scaling monolithic quantum computers, distributed quantum computing (DQC) interconnects multiple smaller-scale quantum processing units (QPUs) to form a quantum network. However, this approach introduces a critical challenge, namely the high cost of quantum communication between remote QPUs incurred by quantum state teleportation and quantum gate teleportation. To minimize this communication overhead, DQC compilers must strategically partition quantum circuits by mapping logical qubits to distributed physical QPUs. Static graph partitioning methods are fundamentally ill-equipped for this task as they ignore execution dynamics and underlying network topology, while metaheuristics require substantial computational runtime. In this work, we propose a heuristic based on beam search to solve the circuit partitioning problem. Our time-aware algorithm incrementally constructs a low-cost sequence of qubit assignments across successive time steps to minimize overall communication overhead. The time and space complexities of the proposed algorithm scale quadratically with the number of qubits and linearly with circuit depth, offering a significant computational speedup over common metaheuristics. We demonstrate that our proposed algorithm consistently achieves significantly lower communication costs than static baselines across varying circuit sizes, depths, and network topologies, providing an efficient compilation tool for near-term distributed quantum hardware.

### Quantum anomaly for benchmarking quantum computing
* **Authors:** Tomoya Hayata et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.03697v1
* **Abstract:** Given the rapid advances in quantum computing hardware, establishing systematic strategies for verifying the correctness of quantum computations has become increasingly important. Exploiting the fact that the axial anomaly in gauge theories is exact to all orders in perturbation theory, we propose the axial anomaly as a nontrivial benchmark for quantum simulations of lattice gauge theories. We simulate anomalous axial-charge production in ${\mathbb Z}_N$ lattice gauge theories on the trapped-ion quantum computer ``Reimei''. After taking the U(1), infinitesimal time, and infinite volume limits, we successfully reproduce the anomaly coefficient within statistical uncertainties, even without error mitigation. Our results demonstrate that the axial anomaly can be simulated on current quantum computers and serves as a verification test of quantum computations.

### Observation of Improved Accuracy over Classical Sparse Ground-State Solvers using a Quantum Computer
* **Authors:** William Kirby et al.
* **Published (v1):** 2026-03-03
* **Updated:** 2026-03-03
* **Link:** http://arxiv.org/abs/2603.03496v1
* **Abstract:** We experimentally demonstrate that a hybrid quantum-classical algorithm can outperform purely classical, off-the-shelf selected configuration interaction methods. First, we construct a class of local Hamiltonian problems with sparse ground states, and show that representative classical heuristics fail to find the ground state of a specific 49-qubit instance. Next, we show that the sample-based Krylov quantum diagonalization algorithm, run on an IBM Heron R3 processor, succeeds at the same task. This algorithm uses quantum samples from a grid of time-evolved quantum states, and offers provable convergence guarantees for sparse ground state problems with guiding states. While the problem is also solvable classically using two iterative solvers that we designed specifically to target our Hamiltonian construction, this work resolves the previously open question of whether a sample-based quantum diagonalization algorithm can outperform standard selected configuration interaction heuristics.



# Papers Found on: 2026-03-05

### HyQBench: A Benchmark Suite for Hybrid CV-DV Quantum Computing
* **Authors:** Shubdeep Mohapatra et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.04398v1
* **Abstract:** Hybrid continuous-variable (CV)-discrete-variable (DV) quantum systems present a promising direction for quantum computing by combining the high dimensional encoding capabilities of qumodes with the control offered by DV qubits on the coupled qumodes. There have been exciting recent progresses on hybrid CV-DV quantum computing, including variational algorithms, error correction, compiler-level optimizations for Hamiltonian simulation, etc. However, there is a lack of a standardized CV-DV benchmark suite for assessing various emerging hardware platforms and evaluating software optimizations on hybrid CV-DV circuits. In this work, we introduce a simulation and benchmarking framework for hybrid CV-DV circuits, implemented using Bosonic Qiskit-a tool specifically designed to model CV-DV systems, along with QuTip for functional correctness verification. We construct and characterize representative CV-DV benchmarks, including cat state generation, GKP state generation, CV-DV state transfers, hybrid quantum Fourier transform, variational quantum algorithms, Hamiltonian simulation, and Shor's algorithm. To assess circuit complexity and scalability, we define a feature map organized into two categories: general features (e.g., qubit/qumode count, gate counts) and CV-DV-specific features (e.g., Wigner negativity, energy, truncation cost). These metrics enable evaluation of both classical simulability and hardware resource requirements. Our results, including one benchmark on real hardware, demonstrate that hybrid CV-DV architectures are not only viable but well-suited for a range of computational tasks, from optimization to Hamiltonian simulation. This framework lays the groundwork for systematic evaluation and future development of hybrid quantum systems.

### Benchmarking Quantum Computers via Protocols, Comparing IBM's Heron vs IBM's Eagle
* **Authors:** Nitay Mayo et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.04377v1
* **Abstract:** As quantum computing hardware rapidly advances, objectively evaluating the capabilities and error rates of new processors remains a critical challenge for the field. A clear and realistic understanding of current quantum performance is essential to guide research priorities and drive meaningful progress. In this work, we apply and extend a protocol-based benchmarking methodology (presented in arXiv:2505.12441) that utilizes well-defined quantumness thresholds. By evaluating performance at protocol level rather then the gate level, this approach provides a transparent and intuitive assessment of whether specific quantum processors, or isolated sub-chips within them, can demonstrate a practical quantum advantage. To illustrate the utility of this method, we compare two generations of IBM quantum computers: the older Eagle architecture and the newer Heron architecture. Our findings reveal the genuine operational strengths and limitations of these devices, demonstrating substantial performance improvements in the newer Heron generation.

### Efficient Time-Aware Partitioning of Quantum Circuits for Distributed Quantum Computing
* **Authors:** Raymond P. H. Wu et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.04126v1
* **Abstract:** To overcome the physical limitations of scaling monolithic quantum computers, distributed quantum computing (DQC) interconnects multiple smaller-scale quantum processing units (QPUs) to form a quantum network. However, this approach introduces a critical challenge, namely the high cost of quantum communication between remote QPUs incurred by quantum state teleportation and quantum gate teleportation. To minimize this communication overhead, DQC compilers must strategically partition quantum circuits by mapping logical qubits to distributed physical QPUs. Static graph partitioning methods are fundamentally ill-equipped for this task as they ignore execution dynamics and underlying network topology, while metaheuristics require substantial computational runtime. In this work, we propose a heuristic based on beam search to solve the circuit partitioning problem. Our time-aware algorithm incrementally constructs a low-cost sequence of qubit assignments across successive time steps to minimize overall communication overhead. The time and space complexities of the proposed algorithm scale quadratically with the number of qubits and linearly with circuit depth, offering a significant computational speedup over common metaheuristics. We demonstrate that our proposed algorithm consistently achieves significantly lower communication costs than static baselines across varying circuit sizes, depths, and network topologies, providing an efficient compilation tool for near-term distributed quantum hardware.

### Quantum anomaly for benchmarking quantum computing
* **Authors:** Tomoya Hayata et al.
* **Published (v1):** 2026-03-04
* **Updated:** 2026-03-04
* **Link:** http://arxiv.org/abs/2603.03697v1
* **Abstract:** Given the rapid advances in quantum computing hardware, establishing systematic strategies for verifying the correctness of quantum computations has become increasingly important. Exploiting the fact that the axial anomaly in gauge theories is exact to all orders in perturbation theory, we propose the axial anomaly as a nontrivial benchmark for quantum simulations of lattice gauge theories. We simulate anomalous axial-charge production in ${\mathbb Z}_N$ lattice gauge theories on the trapped-ion quantum computer ``Reimei''. After taking the U(1), infinitesimal time, and infinite volume limits, we successfully reproduce the anomaly coefficient within statistical uncertainties, even without error mitigation. Our results demonstrate that the axial anomaly can be simulated on current quantum computers and serves as a verification test of quantum computations.

### Observation of Improved Accuracy over Classical Sparse Ground-State Solvers using a Quantum Computer
* **Authors:** William Kirby et al.
* **Published (v1):** 2026-03-03
* **Updated:** 2026-03-03
* **Link:** http://arxiv.org/abs/2603.03496v1
* **Abstract:** We experimentally demonstrate that a hybrid quantum-classical algorithm can outperform purely classical, off-the-shelf selected configuration interaction methods. First, we construct a class of local Hamiltonian problems with sparse ground states, and show that representative classical heuristics fail to find the ground state of a specific 49-qubit instance. Next, we show that the sample-based Krylov quantum diagonalization algorithm, run on an IBM Heron R3 processor, succeeds at the same task. This algorithm uses quantum samples from a grid of time-evolved quantum states, and offers provable convergence guarantees for sparse ground state problems with guiding states. While the problem is also solvable classically using two iterative solvers that we designed specifically to target our Hamiltonian construction, this work resolves the previously open question of whether a sample-based quantum diagonalization algorithm can outperform standard selected configuration interaction heuristics.

