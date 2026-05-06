

# Papers Found on: 2026-05-06

### FTPrimitiveBench: A Benchmark Suite For Logical Computation Under Hardware-Motivated and Biased Noise Models
* **Authors:** Shuwen Kan et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.04049v1
* **Abstract:** Fault-tolerant quantum computing requires understanding how error-correcting codes perform on diverse physical hardware. This is typically assessed via noisy stabilizer simulation of logical circuits at HPC scale, combined with a noise model that yields a logical error rate for the relevant code distances and depths. The uniform depolarizing model is the standard baseline, but its homogeneous assumptions fail to capture the heterogeneity, asymmetries, and correlations of real devices, where Pauli, measurement, and spatio-temporal errors are not weakly coupled. Yet these same structured features create opportunities for joint code-hardware co-design, motivating noise models that more faithfully reflect target hardware while remaining tractable to simulate.   We introduce FTPrimitiveBench, a systematic benchmarking approach for studying how logical primitives interact with hardware-motivated noise. It supports both custom specifications and representative structured noise families: Pauli bias, measurement bias, and spatial or spatio-temporal non-uniformity -- together with generators for core surface-code Clifford primitives: logical memory, lattice surgery, transversal logical Hadamard, and the logical phase gate via lattice surgery. We find that structured noise affects these primitives in qualitatively distinct ways, with outcomes shaped by the interplay between noise model, primitive, and decoder choice. These results extend memory benchmarks to active logical computation, where the interaction between noise structure and primitive implementation matters. By standardizing the link between noise-model specification and primitive construction, FTPrimitiveBench enables reproducible comparative studies of QEC protocols and decoders, supporting hardware-aware co-design of fault-tolerant architectures. Code: https://github.com/ShuwenKan/FTPrimitiveBench.

### Space-Time Tradeoffs of Pauli-Based Computation in Distributed qLDPC Architectures
* **Authors:** Naphan Benchasattabuse et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03854v1
* **Abstract:** Pauli-based computation (PBC) provides a universal framework for executing fault-tolerant quantum algorithms using Pauli measurements and magic states. In monolithic architectures, the serialized nature of PBC directly ties runtime to a circuit's T-gate count, making it slow on metrics like circuit depth. However, in distributed quantum computing (DQC), the primary bottleneck is remote Bell pair generation. We investigate the tradeoff between error-correcting code block size and execution time of PBC within the Q-Fly architecture at intermediate scale, limiting individual node capacities to reflect near-term constraints while supplying abundant network nodes to minimize routing and compilation effects. We find that large qLDPC code blocks outperform the surface code baseline in terms of execution time by up to an order of magnitude when evaluated against quantum optimization algorithms. By moving groups of qubits to free nodes to bypass the sequential bottleneck of PBC, the large-block architecture minimizes network operations and achieves faster overall execution. This demonstrates that PBC is a competitive model in the distributed regime, establishing it as a practical compilation baseline for qLDPC systems before invoking more efficient transversal or homological gates.

### Computation of entanglement for quantum states by a Consensus-Based Optimization method
* **Authors:** Michael Herty et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03773v1
* **Abstract:** The computation of quantum entanglement can be formulated as a high-dimensional nonconvex optimization problem with orthogonality constraints. In this work, we propose structure-preserving consensus-based optimization (CBO) methods for entanglement computation, with one approach based on a Hermitian formulation and the other evolving directly on the unitary manifold. To handle the variable dimension of the feasible set, we introduce a cross-dimensional interaction mechanism allowing exchange of information between particles of different sizes. Numerical experiments demonstrate that the proposed methods achieve accurate approximations.

### A Critical Comment on 'Entropy Computing: A Paradigm for Optimization in Open Photonic Systems'
* **Authors:** Ali Hamed Moosavian et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03612v1
* **Abstract:** In this article, we take a close look at Entropy Quantum Computing (EQC), a computational paradigm developed by Quantum Computing Inc. (QCi), which deviates from mainstream quantum computing by embracing rather than battling environmental noise and decoherence arXiv:2407.04512 . In their words this approach purports EQC as an open quantum system that turns "entropy into super-power fuels of its computing engine". We show that some of the claims in the main article can be made more rigorous, and yet these are still not good enough to beat state of the art classical algorithms on conventional classical computers. Note that these conclusions reflect the technology's current early stage of development and are not meant to discourage its pursuit. Continued rigorous exploration is necessary to fully assess the long-term viability and potential advantages of this distinct computational approach.

### Harnessing DEN models for quantum computing tasks on neutral atom QPUs
* **Authors:** Chiara Vercellino et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03503v1
* **Abstract:** We present our work on effectively representing unit-disk graphs on the registers of neutral atom quantum machines. Specifically, we aimed to embed graphs corresponding to proteins and cellular antenna networks into unit-disk graphs, ensuring compatibility with the registers of two real QPUs: Orion Alpha by PASQAL and Aquila by QuEra. To address machine-specific constraints, we made adjustments and integrated Distance Encoder Networks (DEN) from our previous work. Despite these challenges, we successfully embedded up to 76% of protein-representing graphs for a quantum machine learning classification task on the Aquila QPU, and all subgraphs derived from 90 antenna geographical positions in Turin, Italy, on the Orion Alpha QPU. In the latter case, the graphs represented instances of the graph coloring problem, which we tackled using the hybrid quantum-classical algorithm BBQ-mIS. These promising results underscore the effectiveness and versatility of our embedding approach for representing unit-disk graphs on neutral atom quantum computers across diverse applications.



# Papers Found on: 2026-05-06

### FTPrimitiveBench: A Benchmark Suite For Logical Computation Under Hardware-Motivated and Biased Noise Models
* **Authors:** Shuwen Kan et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.04049v1
* **Abstract:** Fault-tolerant quantum computing requires understanding how error-correcting codes perform on diverse physical hardware. This is typically assessed via noisy stabilizer simulation of logical circuits at HPC scale, combined with a noise model that yields a logical error rate for the relevant code distances and depths. The uniform depolarizing model is the standard baseline, but its homogeneous assumptions fail to capture the heterogeneity, asymmetries, and correlations of real devices, where Pauli, measurement, and spatio-temporal errors are not weakly coupled. Yet these same structured features create opportunities for joint code-hardware co-design, motivating noise models that more faithfully reflect target hardware while remaining tractable to simulate.   We introduce FTPrimitiveBench, a systematic benchmarking approach for studying how logical primitives interact with hardware-motivated noise. It supports both custom specifications and representative structured noise families: Pauli bias, measurement bias, and spatial or spatio-temporal non-uniformity -- together with generators for core surface-code Clifford primitives: logical memory, lattice surgery, transversal logical Hadamard, and the logical phase gate via lattice surgery. We find that structured noise affects these primitives in qualitatively distinct ways, with outcomes shaped by the interplay between noise model, primitive, and decoder choice. These results extend memory benchmarks to active logical computation, where the interaction between noise structure and primitive implementation matters. By standardizing the link between noise-model specification and primitive construction, FTPrimitiveBench enables reproducible comparative studies of QEC protocols and decoders, supporting hardware-aware co-design of fault-tolerant architectures. Code: https://github.com/ShuwenKan/FTPrimitiveBench.

### Space-Time Tradeoffs of Pauli-Based Computation in Distributed qLDPC Architectures
* **Authors:** Naphan Benchasattabuse et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03854v1
* **Abstract:** Pauli-based computation (PBC) provides a universal framework for executing fault-tolerant quantum algorithms using Pauli measurements and magic states. In monolithic architectures, the serialized nature of PBC directly ties runtime to a circuit's T-gate count, making it slow on metrics like circuit depth. However, in distributed quantum computing (DQC), the primary bottleneck is remote Bell pair generation. We investigate the tradeoff between error-correcting code block size and execution time of PBC within the Q-Fly architecture at intermediate scale, limiting individual node capacities to reflect near-term constraints while supplying abundant network nodes to minimize routing and compilation effects. We find that large qLDPC code blocks outperform the surface code baseline in terms of execution time by up to an order of magnitude when evaluated against quantum optimization algorithms. By moving groups of qubits to free nodes to bypass the sequential bottleneck of PBC, the large-block architecture minimizes network operations and achieves faster overall execution. This demonstrates that PBC is a competitive model in the distributed regime, establishing it as a practical compilation baseline for qLDPC systems before invoking more efficient transversal or homological gates.

### Computation of entanglement for quantum states by a Consensus-Based Optimization method
* **Authors:** Michael Herty et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03773v1
* **Abstract:** The computation of quantum entanglement can be formulated as a high-dimensional nonconvex optimization problem with orthogonality constraints. In this work, we propose structure-preserving consensus-based optimization (CBO) methods for entanglement computation, with one approach based on a Hermitian formulation and the other evolving directly on the unitary manifold. To handle the variable dimension of the feasible set, we introduce a cross-dimensional interaction mechanism allowing exchange of information between particles of different sizes. Numerical experiments demonstrate that the proposed methods achieve accurate approximations.

### A Critical Comment on 'Entropy Computing: A Paradigm for Optimization in Open Photonic Systems'
* **Authors:** Ali Hamed Moosavian et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03612v1
* **Abstract:** In this article, we take a close look at Entropy Quantum Computing (EQC), a computational paradigm developed by Quantum Computing Inc. (QCi), which deviates from mainstream quantum computing by embracing rather than battling environmental noise and decoherence arXiv:2407.04512 . In their words this approach purports EQC as an open quantum system that turns "entropy into super-power fuels of its computing engine". We show that some of the claims in the main article can be made more rigorous, and yet these are still not good enough to beat state of the art classical algorithms on conventional classical computers. Note that these conclusions reflect the technology's current early stage of development and are not meant to discourage its pursuit. Continued rigorous exploration is necessary to fully assess the long-term viability and potential advantages of this distinct computational approach.

### Harnessing DEN models for quantum computing tasks on neutral atom QPUs
* **Authors:** Chiara Vercellino et al.
* **Published (v1):** 2026-05-05
* **Updated:** 2026-05-05
* **Link:** http://arxiv.org/abs/2605.03503v1
* **Abstract:** We present our work on effectively representing unit-disk graphs on the registers of neutral atom quantum machines. Specifically, we aimed to embed graphs corresponding to proteins and cellular antenna networks into unit-disk graphs, ensuring compatibility with the registers of two real QPUs: Orion Alpha by PASQAL and Aquila by QuEra. To address machine-specific constraints, we made adjustments and integrated Distance Encoder Networks (DEN) from our previous work. Despite these challenges, we successfully embedded up to 76% of protein-representing graphs for a quantum machine learning classification task on the Aquila QPU, and all subgraphs derived from 90 antenna geographical positions in Turin, Italy, on the Orion Alpha QPU. In the latter case, the graphs represented instances of the graph coloring problem, which we tackled using the hybrid quantum-classical algorithm BBQ-mIS. These promising results underscore the effectiveness and versatility of our embedding approach for representing unit-disk graphs on neutral atom quantum computers across diverse applications.

