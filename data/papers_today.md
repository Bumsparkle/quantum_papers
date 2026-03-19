# Papers Found on: 2026-03-19

### The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery
* **Authors:** Narjes Ansari et al.
* **Published (v1):** 2026-03-18
* **Updated:** 2026-03-18
* **Link:** http://arxiv.org/abs/2603.17790v1
* **Abstract:** Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

### Data Obfuscation for Secure Use of Classical Values in Quantum Computation
* **Authors:** Amal Raj et al.
* **Published (v1):** 2026-03-18
* **Updated:** 2026-03-18
* **Link:** http://arxiv.org/abs/2603.17725v1
* **Abstract:** Quantum computing often requires classical data to be supplied to execution environments that may not be fully trusted or isolated. While encryption protects data at rest and in transit, it provides limited protection once computation begins, when classical values are encoded into quantum registers. This paper explores data obfuscation for protecting classical values during quantum computation. To the best of our knowledge, we present the first explicit data obfuscation technique designed to protect classical values during quantum execution. We propose an obfuscation technique that encodes sensitive data into structured quantum representations across multiple registers, avoiding direct exposure while preserving computational usability. Reversible quantum operations and amplitude amplification allow selective recovery of valid encodings without revealing the underlying data. We evaluate the feasibility of the proposed method through simulation and analyze its resource requirements and practical limitations. Our results highlight data obfuscation as a complementary security primitive for quantum computing.

### Implementation of non-local arbitrary two-qubit controlled gates via geometric quantum computation with Rydberg anti-blockade
* **Authors:** Le-Jiang Yu et al.
* **Published (v1):** 2026-03-18
* **Updated:** 2026-03-18
* **Link:** http://arxiv.org/abs/2603.17656v1
* **Abstract:** In the context of Rydberg anti-blockade, this paper proposes a new scheme for a high-fidelity controlled-unitary gate based on non-adiabatic holonomic quantum computation. Under specific detuning and interaction conditions, the scheme achieves a suitable evolution path for non-adiabatic holonomic quantum computation through reverse engineering of pulse parameters. Numerical simulations show that the geometric gate maintains high fidelity even in the presence of spontaneous radiation and laser intensity errors. Finally,we extend our designed quantum gates to non-local gates and investigate their use in converting four-qubit entangled states. This finding indicates the potential applicability of our scheme to complex quantum information processing tasks.

### Allocating Access to Quantum Computing: A Legal-Ethical Framework
* **Authors:** Benedict Lane et al.
* **Published (v1):** 2026-03-18
* **Updated:** 2026-03-18
* **Link:** http://arxiv.org/abs/2603.17597v1
* **Abstract:** Along with the increased availability and capabilities of quantum computers comes the core question: how can access to quantum computing be allocated in a responsible way? This report introduces a general legal-ethical framework that providers of access to quantum computing can apply to develop robust access policies tailored to their specific context. We demonstrate the applicability of this general legal-ethical framework in the specific context of a small, 16-qubit quantum computer that will be hosted by SURF (the Dutch IT cooperative for research and education), integrated with Snellius (the Dutch national supercomputer), and operated jointly as part of the EuroSSQ-HPC consortium, procured in partnership with the EU-wide EuroHPC Joint Undertaking.

### General circuit compilation protocol into partially fault-tolerant quantum computing architecture
* **Authors:** Tomochika Kurita et al.
* **Published (v1):** 2026-03-18
* **Updated:** 2026-03-18
* **Link:** http://arxiv.org/abs/2603.17428v1
* **Abstract:** As we are entering an early-FTQC era, circuit execution protocols with logical qubits and certain error-correcting codes are being discussed. Here, we propose a circuit execution protocol for the space-time efficient analog rotation (STAR) architecture. Gate operations within the STAR architecture is based on lattice surgery with surface codes, but it allows direct execution of continuous gates $Rz(θ)$ as non-Clifford gates instead of $T = Rz(π/4)$. $Rz(θ)$ operations involve creation of resource states $|m_θ\rangle = \frac{1}{\sqrt{2}} (|0 \rangle + e^{iθ} |1\rangle ) $ followed by ZZ joint measurements with target logical qubits. While employing $Rz(θ)$ enables more efficient circuit execution, both their creations and joint measurements are probabilistic processes and adopt repeat-until-success (RUS) protocols which are likely to result in considerable time overhead. Our circuit execution protocol aims to reduce such time overhead by parallel trials of resource state creations and more frequent trials of joint measurements. By employing quadratic unconstrained binary optimization (QUBO) in determining resource state allocations within the space, we successfully make our protocol efficient. Furthermore, we proposed performance estimators given the target circuit and qubit topology. It successfully predicts the time performance within less time than actual simulations do, and helps find the optimal qubit topology to run the target circuits efficiently.

### PhasorFlow: A Python Library for Unit Circle Based Computing
* **Authors:** Dibakar Sigdel et al.
* **Published (v1):** 2026-03-16
* **Updated:** 2026-03-18
* **Link:** http://arxiv.org/abs/2603.15886v2
* **Abstract:** We present PhasorFlow, an open-source Python library introducing a computational paradigm operating on the $S^1$ unit circle. Inputs are encoded as complex phasors $z = e^{iθ}$ on the $N$-Torus ($\mathbb{T}^N$). As computation proceeds via unitary wave interference gates, global norm is preserved while individual components drift into $\mathbb{C}^N$, allowing algorithms to natively leverage continuous geometric gradients for predictive learning. PhasorFlow provides three core contributions. First, we formalize the Phasor Circuit model ($N$ unit circle threads, $M$ gates) and introduce a 22-gate library covering Standard Unitary, Non-Linear, Neuromorphic, and Encoding operations with full matrix algebra simulation. Second, we present the Variational Phasor Circuit (VPC), analogous to Variational Quantum Circuits (VQC), enabling optimization of continuous phase parameters for classical machine learning tasks. Third, we introduce the Phasor Transformer, replacing expensive $QK^TV$ attention with a parameter-free, DFT-based token mixing layer inspired by FNet. We validate PhasorFlow on non-linear spatial classification, time-series prediction, financial volatility detection, and neuromorphic tasks including neural binding and oscillatory associative memory. Our results establish unit circle computing as a deterministic, lightweight, and mathematically principled alternative to classical neural networks and quantum circuits. It operates on classical hardware while sharing quantum mechanics' unitary foundations. PhasorFlow is available at https://github.com/mindverse-computing/phasorflow.

### Noise-resilient nonadiabatic geometric quantum computation for bosonic binomial codes
* **Authors:** Dong-Sheng Li et al.
* **Published (v1):** 2026-03-18
* **Updated:** 2026-03-18
* **Link:** http://arxiv.org/abs/2603.17250v1
* **Abstract:** The binomial code is renowned for its parity-mediated loss immunity and loss-error recoverability, while geometric phases are widely recognized for their intrinsic resilience against noise. Capitalizing on their complementary merits, we propose a noise-resilient protocol to realize Nonadiabatic geometric quantum computation with binomial codes in a superconducting system composed of a microwave cavity %off-resonantly dispersively coupled to a %three-level qutrit. The control field %geometric quantum computation   is designed by %combining geometric phases, integrating reverse engineering and optimal control. This design provides a customized control protocol featuring strong error-tolerance and inherent noise-resilience. Using experimentally accessible parameters in superconducting systems, numerical simulations show that the protocol yields relatively high average fidelity for geometric quantum gates based on binomial code, even in the presence of parameter fluctuations and decoherence. Thus, this protocol may provide a practical approach for realizing reliable Nonadiabatic geometric quantum computation with binomial codes in current technology.

### Quantum reservoir computing with classical and nonclassical states in an integrated optical circuit
* **Authors:** S. Świerczewski et al.
* **Published (v1):** 2026-03-17
* **Updated:** 2026-03-17
* **Link:** http://arxiv.org/abs/2603.17103v1
* **Abstract:** Quantum reservoir computing (QRC) is a hardware-implementation-friendly quantum neural network scheme with minimal physical system requirements and a proven advantage over classical counterparts. We use an extension of the positive-P phase space method to efficiently simulate a bosonic, linear silicon-chip based QRC system excited with a single nonclassical state, a "kitten" state. In combination with input-encoding coherent states, our method allows to obtain exact results for all correlation functions without Hilbert space cutoff. Surprisingly, we find that such a setting - where the only "quantumness'' derives from a single input mode, is sufficient to obtain significant (over 9-fold) reduction of classification error over the classical counterpart. Our work provides a promising direction toward efficient quantum computation with accessible optical hardware.
