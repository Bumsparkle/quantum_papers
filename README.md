

# Papers Found on: 2026-04-09

### On the Computational Complexity of Geometrically Local QAC0 circuits
* **Authors:** Yangjing Dong et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.07178v1
* **Abstract:** The computational complexity of $\mathsf{QAC}^0$, which are constant-depth, polynomial-size quantum circuit families consisting of arbitrary single-qubit unitaries and $n$-qubit generalized Toffoli gates, has gained tremendous focus recently.   In this work, we initiate the study of the computational complexity of geometrically local $\mathsf{QAC}^0$ circuits, where all the generalized Toffoli gates act on nearest neighbor qubits. We show that any $\mathsf{QAC}^0$ circuit can be exactly simulated by a two-dimensional geometrically local $\mathsf{QAC}^0$ circuit, i.e., a $\mathsf{2D\text{-}QAC}^{0}$ circuit, with a quadratic size blow-up. This implies that $\mathsf{QAC}^0 = \mathsf{2D\text{-}QAC}^{0}$. We further show that if there existed a $\mathsf{QAC}^0$ circuit that computes Parity with a bounded constant error, then for any $\varepsilon > 0$, there would exist a $\mathsf{2D\text{-}QAC}^{0}$ circuit that exactly computes Parity, with a very "thin" width $n^\varepsilon$.   We further study the computational power of $\mathsf{1D\text{-}QAC}^{0} $ circuits, i.e., one-dimensional $\mathsf{QAC}^0$ circuits, which are the "thinnest" $\mathsf{2D\text{-}QAC}^{0}$ circuits. We prove a nearly logarithmic depth lower bound on $\mathsf{1D\text{-}QAC}^{0} $ circuits to compute the Parity function, even if allowing an unlimited number of ancilla. Furthermore, if the inputs are encoded in contiguous qubits, we prove that it requires a nearly linear depth $\mathsf{1D\text{-}QAC}^{0} $ circuit to compute the Parity function. This lower bound is almost tight. The results are proved via the combination of the restriction argument and the light-cone argument. These results may provide a new angle for studying the computational power of $\mathsf{QAC}^0$ circuits and for resolving the long-standing open problem of whether Parity is in $\mathsf{QAC}^0$.

### QCommute: a tool for symbolic computation of nested commutators in quantum many-body spin-1/2 systems
* **Authors:** Oleg Lychkovskiy et al.
* **Published (v1):** 2026-04-06
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.04778v2
* **Abstract:** We present QCommute, a software tool implemented in C++ for symbolic computation of nested commutators between a Hamiltonian and local observables in quantum many-body spin-1/2 systems on one-, two-, and three-dimensional hypercubic lattices. The computation is performed algebraically directly in the thermodynamic limit, and the Hamiltonian parameters are kept symbolic. Importantly, this way the entire parameter space is covered in a single run. The implementation supports extensive parallelization to achieve high computational performance. QCommute enables the investigation of quantum dynamics in strongly correlated regimes that are inaccessible to perturbative approaches, either through direct Taylor expansion in time or via advanced techniques such as the recursion method.

### Broken Quantum: A Systematic Formal Verification Study of Security Vulnerabilities Across the Open-Source Quantum Computing Simulator Ecosystem
* **Authors:** Dominik Blain et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.06712v1
* **Abstract:** Quantum computing simulators form the classical software foundation on which virtually all quantum algorithm research depends. We present Broken Quantum, the first comprehensive formal security audit of the open-source quantum computing simulator ecosystem. Applying COBALT QAI -- a four-module static analysis engine backed by the Z3 SMT solver -- we analyze 45 open-source quantum simulation frameworks from 22 organizations spanning 12 countries. We identify 547 security findings (40 CRITICAL, 492 HIGH, 15 MEDIUM) across four vulnerability classes: CWE-125/190 (C++ memory corruption), CWE-400 (Python resource exhaustion), CWE-502/94 (unsafe deserialization and code injection), and CWE-77/22 (QASM injection -- a novel, quantum-specific attack vector with no classical analog). All 13 vulnerability patterns are formally verified via Z3 satisfiability proofs (13/13 SAT). The 32-qubit boundary emerges as a consistent formal threshold in both C++ and Python vulnerability chains. Supply chain analysis identifies the first documented case of vulnerability transfer from a commercial quantum framework into US national laboratory infrastructure (IBM Qiskit Aer to XACC/Oak Ridge National Laboratory). Nine frameworks score 100/100 under all four scanners; Qiskit Aer,Cirq, tequila, PennyLane, and 5 others score 0/100.

### Deterministic linear-optical computing with symmetry-based qubits
* **Authors:** David S. Simon et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.06584v1
* **Abstract:** A particular type of linear optical multiport, the Grover four-port, has previously been shown to couple the spatial symmetry of a photon to its direction of travel. It is shown here that use of a nonstandard choice of qubit, based on symmetry, allows Grover four ports to act as compact, low-resource deterministic linear optical controlledNOTgates, with no post-selection or ancilla measurements required. This approach allows programmable devices, made from Grover multiports in combination with other standard optical components, that can implement multiple different one-, two-, and three-qubit gates, including the Fredkin and Toffoli gates.

### Probing the Planck scale with quantum computation
* **Authors:** Boaz Katz et al.
* **Published (v1):** 2026-04-07
* **Updated:** 2026-04-07
* **Link:** http://arxiv.org/abs/2604.06322v1
* **Abstract:** General relativity and quantum mechanics are incompatible at the Planck scale. This contention can be examined if a quantum computer is set to operate at a rate that exceeds the classical limit of one operation per Planck volume-time, or equivalently $2^{491}$ m$^{-3}$ s$^{-1}$. Here we quantify the relation between the logical qubit count and the extent to which classicality is challenged. We argue that 500 logical qubits are sufficient to reject theories confined to a laboratory. We account for the operational cost of computation and communication at all scales up to and including the observable universe, ultimately constrained by a 1600-logical-qubit computer. Remarkably, current plans for commercial quantum computers are projected to surpass this limit, thereby putting the quantum-gravity standoff to the test.

### Heterogeneous architectures enable a 138x reduction in physical qubit requirements for fault-tolerant quantum computing under detailed accounting
* **Authors:** Pranav S. Mundada et al.
* **Published (v1):** 2026-04-07
* **Updated:** 2026-04-07
* **Link:** http://arxiv.org/abs/2604.06319v1
* **Abstract:** Quantum computer hardware is predicted to scale over hundreds of thousands of qubits coming online in the next decade. Despite significant theoretical and experimental QEC progress, quantum computer architecture has suffered a significant gap, with bottom-up physical-device-driven challenges largely disconnected from top-down QEC-code-driven considerations. In this work, we unify these two views, presenting a complete heterogeneous quantum computing architecture incorporating task-specific hardware selection and QEC encoding, and agnostic to code selection or physical qubit parameters. Our approach further enables special-purpose processing modules, and includes a full microarchitecture for fault-tolerant implementation of interfaces between quantum processing units and quantum memories. Using this architecture and a new fully featured compiler functioning across subsystems at the scale of $1,000$ logical qubits, we schedule and orchestrate a variety of algorithms down to hardware-specific instructions; a detailed accounting of all operations reveals up to 551x reduction in algorithmic logical error and up to 138x reduction in physical-qubit overhead compared to a monolithic baseline architecture. We then consider the factorization of 2048-bit RSA-integers; using an experimentally demonstrated grid-coupling topology, factoring RSA-2048 requires 381k physical qubits and 9.2 days, which can be reduced to 4.9 days via addition of an algorithm-specific accelerator for the Adder subroutine (requiring 439k qubits). Finally, assuming hypothetical long-range coupling, implementing quantum memory using qLDPC codes reduces the resources required for factoring to just 190k qubits and under 10 days. These results and the tooling we have built indicate that heterogeneous quantum-computer architectures can deliver significant, verifiable benefits on realistic hardware.



# Papers Found on: 2026-04-09

### On the Computational Complexity of Geometrically Local QAC0 circuits
* **Authors:** Yangjing Dong et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.07178v1
* **Abstract:** The computational complexity of $\mathsf{QAC}^0$, which are constant-depth, polynomial-size quantum circuit families consisting of arbitrary single-qubit unitaries and $n$-qubit generalized Toffoli gates, has gained tremendous focus recently.   In this work, we initiate the study of the computational complexity of geometrically local $\mathsf{QAC}^0$ circuits, where all the generalized Toffoli gates act on nearest neighbor qubits. We show that any $\mathsf{QAC}^0$ circuit can be exactly simulated by a two-dimensional geometrically local $\mathsf{QAC}^0$ circuit, i.e., a $\mathsf{2D\text{-}QAC}^{0}$ circuit, with a quadratic size blow-up. This implies that $\mathsf{QAC}^0 = \mathsf{2D\text{-}QAC}^{0}$. We further show that if there existed a $\mathsf{QAC}^0$ circuit that computes Parity with a bounded constant error, then for any $\varepsilon > 0$, there would exist a $\mathsf{2D\text{-}QAC}^{0}$ circuit that exactly computes Parity, with a very "thin" width $n^\varepsilon$.   We further study the computational power of $\mathsf{1D\text{-}QAC}^{0} $ circuits, i.e., one-dimensional $\mathsf{QAC}^0$ circuits, which are the "thinnest" $\mathsf{2D\text{-}QAC}^{0}$ circuits. We prove a nearly logarithmic depth lower bound on $\mathsf{1D\text{-}QAC}^{0} $ circuits to compute the Parity function, even if allowing an unlimited number of ancilla. Furthermore, if the inputs are encoded in contiguous qubits, we prove that it requires a nearly linear depth $\mathsf{1D\text{-}QAC}^{0} $ circuit to compute the Parity function. This lower bound is almost tight. The results are proved via the combination of the restriction argument and the light-cone argument. These results may provide a new angle for studying the computational power of $\mathsf{QAC}^0$ circuits and for resolving the long-standing open problem of whether Parity is in $\mathsf{QAC}^0$.

### QCommute: a tool for symbolic computation of nested commutators in quantum many-body spin-1/2 systems
* **Authors:** Oleg Lychkovskiy et al.
* **Published (v1):** 2026-04-06
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.04778v2
* **Abstract:** We present QCommute, a software tool implemented in C++ for symbolic computation of nested commutators between a Hamiltonian and local observables in quantum many-body spin-1/2 systems on one-, two-, and three-dimensional hypercubic lattices. The computation is performed algebraically directly in the thermodynamic limit, and the Hamiltonian parameters are kept symbolic. Importantly, this way the entire parameter space is covered in a single run. The implementation supports extensive parallelization to achieve high computational performance. QCommute enables the investigation of quantum dynamics in strongly correlated regimes that are inaccessible to perturbative approaches, either through direct Taylor expansion in time or via advanced techniques such as the recursion method.

### Broken Quantum: A Systematic Formal Verification Study of Security Vulnerabilities Across the Open-Source Quantum Computing Simulator Ecosystem
* **Authors:** Dominik Blain et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.06712v1
* **Abstract:** Quantum computing simulators form the classical software foundation on which virtually all quantum algorithm research depends. We present Broken Quantum, the first comprehensive formal security audit of the open-source quantum computing simulator ecosystem. Applying COBALT QAI -- a four-module static analysis engine backed by the Z3 SMT solver -- we analyze 45 open-source quantum simulation frameworks from 22 organizations spanning 12 countries. We identify 547 security findings (40 CRITICAL, 492 HIGH, 15 MEDIUM) across four vulnerability classes: CWE-125/190 (C++ memory corruption), CWE-400 (Python resource exhaustion), CWE-502/94 (unsafe deserialization and code injection), and CWE-77/22 (QASM injection -- a novel, quantum-specific attack vector with no classical analog). All 13 vulnerability patterns are formally verified via Z3 satisfiability proofs (13/13 SAT). The 32-qubit boundary emerges as a consistent formal threshold in both C++ and Python vulnerability chains. Supply chain analysis identifies the first documented case of vulnerability transfer from a commercial quantum framework into US national laboratory infrastructure (IBM Qiskit Aer to XACC/Oak Ridge National Laboratory). Nine frameworks score 100/100 under all four scanners; Qiskit Aer,Cirq, tequila, PennyLane, and 5 others score 0/100.

### Deterministic linear-optical computing with symmetry-based qubits
* **Authors:** David S. Simon et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.06584v1
* **Abstract:** A particular type of linear optical multiport, the Grover four-port, has previously been shown to couple the spatial symmetry of a photon to its direction of travel. It is shown here that use of a nonstandard choice of qubit, based on symmetry, allows Grover four ports to act as compact, low-resource deterministic linear optical controlledNOTgates, with no post-selection or ancilla measurements required. This approach allows programmable devices, made from Grover multiports in combination with other standard optical components, that can implement multiple different one-, two-, and three-qubit gates, including the Fredkin and Toffoli gates.

### Probing the Planck scale with quantum computation
* **Authors:** Boaz Katz et al.
* **Published (v1):** 2026-04-07
* **Updated:** 2026-04-07
* **Link:** http://arxiv.org/abs/2604.06322v1
* **Abstract:** General relativity and quantum mechanics are incompatible at the Planck scale. This contention can be examined if a quantum computer is set to operate at a rate that exceeds the classical limit of one operation per Planck volume-time, or equivalently $2^{491}$ m$^{-3}$ s$^{-1}$. Here we quantify the relation between the logical qubit count and the extent to which classicality is challenged. We argue that 500 logical qubits are sufficient to reject theories confined to a laboratory. We account for the operational cost of computation and communication at all scales up to and including the observable universe, ultimately constrained by a 1600-logical-qubit computer. Remarkably, current plans for commercial quantum computers are projected to surpass this limit, thereby putting the quantum-gravity standoff to the test.

### Heterogeneous architectures enable a 138x reduction in physical qubit requirements for fault-tolerant quantum computing under detailed accounting
* **Authors:** Pranav S. Mundada et al.
* **Published (v1):** 2026-04-07
* **Updated:** 2026-04-07
* **Link:** http://arxiv.org/abs/2604.06319v1
* **Abstract:** Quantum computer hardware is predicted to scale over hundreds of thousands of qubits coming online in the next decade. Despite significant theoretical and experimental QEC progress, quantum computer architecture has suffered a significant gap, with bottom-up physical-device-driven challenges largely disconnected from top-down QEC-code-driven considerations. In this work, we unify these two views, presenting a complete heterogeneous quantum computing architecture incorporating task-specific hardware selection and QEC encoding, and agnostic to code selection or physical qubit parameters. Our approach further enables special-purpose processing modules, and includes a full microarchitecture for fault-tolerant implementation of interfaces between quantum processing units and quantum memories. Using this architecture and a new fully featured compiler functioning across subsystems at the scale of $1,000$ logical qubits, we schedule and orchestrate a variety of algorithms down to hardware-specific instructions; a detailed accounting of all operations reveals up to 551x reduction in algorithmic logical error and up to 138x reduction in physical-qubit overhead compared to a monolithic baseline architecture. We then consider the factorization of 2048-bit RSA-integers; using an experimentally demonstrated grid-coupling topology, factoring RSA-2048 requires 381k physical qubits and 9.2 days, which can be reduced to 4.9 days via addition of an algorithm-specific accelerator for the Adder subroutine (requiring 439k qubits). Finally, assuming hypothetical long-range coupling, implementing quantum memory using qLDPC codes reduces the resources required for factoring to just 190k qubits and under 10 days. These results and the tooling we have built indicate that heterogeneous quantum-computer architectures can deliver significant, verifiable benefits on realistic hardware.

