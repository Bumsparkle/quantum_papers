

# Papers Found on: 2026-03-02

### Advanced Scheduling Strategies for Distributed Quantum Computing Jobs
* **Authors:** Gongyu Ni et al.
* **Published (v1):** 2026-02-27
* **Updated:** 2026-02-27
* **Link:** http://arxiv.org/abs/2602.24152v1
* **Abstract:** Scaling the number of qubits available across multiple quantum devices is an active area of research within distributed quantum computing (DQC). This includes quantum circuit compilation and execution management on multiple quantum devices in the network. The latter aspect is very challenging because, while reducing the makespan of job batches remains a relevant objective, novel quantum-specific constraints must be considered, including QPU utilization, non-local gate density, and the latency associated with queued DQC jobs. In this work, a range of scheduling strategies is proposed, simulated, and evaluated, including heuristics that prioritize resource maximization for QPU utilization, node selection based on heterogeneous network connectivity, asynchronous node release upon job completion, and a scheduling strategy based on reinforcement learning with proximal policy optimization. These approaches are benchmarked against traditional FIFO and LIST schedulers under varying DQC job types and network conditions for the allocation of DQC jobs to devices within a network.

### Optimized Compilation for Distributed Quantum Computing
* **Authors:** Michele Bandini et al.
* **Published (v1):** 2026-02-27
* **Updated:** 2026-02-27
* **Link:** http://arxiv.org/abs/2602.24062v1
* **Abstract:** In many practical applications, quantum algorithms require several qubits, significantly more than those available with current noisy intermediate-scale quantum processors. Distributed quantum computing (DQC) is considered a scalable approach to increasing the number of available qubits for computational tasks. In the DQC setting, a quantum compiler must find the best partitioning for the quantum algorithm and then perform smart non-local operations scheduling to optimize the consumption of Einstein-Podolsky-Rosen (EPR) pairs. In this work, the focus is on minimizing the use of EPR pairs when the circuit structure allows for multiple non-local gates to utilize a single TeleGate operation. This is achieved by using a greedy algorithm that explores the circuit and groups together the gates that could share an EPR pair while also changing the order of commutative gates when necessary. With this preliminary pass, the compiled circuits show reduced depth and EPR usage. Since the quality of each EPR pair quickly deteriorates, the number of non-local gates using the same EPR pair should also be bounded. This means that, depending on the features of the target quantum network, the user can achieve different levels of optimization. Here, it is shown that this approach brings benefits even while assuming a low EPR pair lifetime.

### Large-scale portfolio optimization on a trapped-ion quantum computer
* **Authors:** Alejandro Gomez Cadavid et al.
* **Published (v1):** 2026-02-27
* **Updated:** 2026-02-27
* **Link:** http://arxiv.org/abs/2602.23976v1
* **Abstract:** We present an end-to-end pipeline for large-scale portfolio selection with cardinality constraints and experimentally demonstrate it on trapped-ion quantum processors using hardware-aware decomposition. Building on RMT-based correlation-matrix denoising and community detection, we identify correlated asset groups and introduce a correlation-guided greedy splitting scheme that caps each cluster by the executable qubit budget. Each cluster defines a hardware-embeddable QUBO subproblem that we solve using bias-field digitized counterdiabatic quantum optimization (BF-DCQO), a non-variational method that avoids classical parameter-training loops. We recombine low-energy candidates into global portfolios and enforce feasibility with a two-stage post-processing routine: fast repair followed by a cardinality-preserving swap local search. We benchmark the workflow on a 250-asset universe taken from the S&P 500 and execute subproblems on a 64-qubit Barium development system similar to the forthcoming IonQ Tempo line. We observe that larger executable subproblem sizes reduce decomposition error and systematically improve final objective values and risk-return trade-offs relative to randomized baselines under identical post-processing. Overall, the results establish a hardware-tested route for scaling financial optimization problems, defined by a trade space in which executable problem size and circuit cost are balanced against the resulting solution quality.



# Papers Found on: 2026-03-02

### Advanced Scheduling Strategies for Distributed Quantum Computing Jobs
* **Authors:** Gongyu Ni et al.
* **Published (v1):** 2026-02-27
* **Updated:** 2026-02-27
* **Link:** http://arxiv.org/abs/2602.24152v1
* **Abstract:** Scaling the number of qubits available across multiple quantum devices is an active area of research within distributed quantum computing (DQC). This includes quantum circuit compilation and execution management on multiple quantum devices in the network. The latter aspect is very challenging because, while reducing the makespan of job batches remains a relevant objective, novel quantum-specific constraints must be considered, including QPU utilization, non-local gate density, and the latency associated with queued DQC jobs. In this work, a range of scheduling strategies is proposed, simulated, and evaluated, including heuristics that prioritize resource maximization for QPU utilization, node selection based on heterogeneous network connectivity, asynchronous node release upon job completion, and a scheduling strategy based on reinforcement learning with proximal policy optimization. These approaches are benchmarked against traditional FIFO and LIST schedulers under varying DQC job types and network conditions for the allocation of DQC jobs to devices within a network.

### Optimized Compilation for Distributed Quantum Computing
* **Authors:** Michele Bandini et al.
* **Published (v1):** 2026-02-27
* **Updated:** 2026-02-27
* **Link:** http://arxiv.org/abs/2602.24062v1
* **Abstract:** In many practical applications, quantum algorithms require several qubits, significantly more than those available with current noisy intermediate-scale quantum processors. Distributed quantum computing (DQC) is considered a scalable approach to increasing the number of available qubits for computational tasks. In the DQC setting, a quantum compiler must find the best partitioning for the quantum algorithm and then perform smart non-local operations scheduling to optimize the consumption of Einstein-Podolsky-Rosen (EPR) pairs. In this work, the focus is on minimizing the use of EPR pairs when the circuit structure allows for multiple non-local gates to utilize a single TeleGate operation. This is achieved by using a greedy algorithm that explores the circuit and groups together the gates that could share an EPR pair while also changing the order of commutative gates when necessary. With this preliminary pass, the compiled circuits show reduced depth and EPR usage. Since the quality of each EPR pair quickly deteriorates, the number of non-local gates using the same EPR pair should also be bounded. This means that, depending on the features of the target quantum network, the user can achieve different levels of optimization. Here, it is shown that this approach brings benefits even while assuming a low EPR pair lifetime.

### Large-scale portfolio optimization on a trapped-ion quantum computer
* **Authors:** Alejandro Gomez Cadavid et al.
* **Published (v1):** 2026-02-27
* **Updated:** 2026-02-27
* **Link:** http://arxiv.org/abs/2602.23976v1
* **Abstract:** We present an end-to-end pipeline for large-scale portfolio selection with cardinality constraints and experimentally demonstrate it on trapped-ion quantum processors using hardware-aware decomposition. Building on RMT-based correlation-matrix denoising and community detection, we identify correlated asset groups and introduce a correlation-guided greedy splitting scheme that caps each cluster by the executable qubit budget. Each cluster defines a hardware-embeddable QUBO subproblem that we solve using bias-field digitized counterdiabatic quantum optimization (BF-DCQO), a non-variational method that avoids classical parameter-training loops. We recombine low-energy candidates into global portfolios and enforce feasibility with a two-stage post-processing routine: fast repair followed by a cardinality-preserving swap local search. We benchmark the workflow on a 250-asset universe taken from the S&P 500 and execute subproblems on a 64-qubit Barium development system similar to the forthcoming IonQ Tempo line. We observe that larger executable subproblem sizes reduce decomposition error and systematically improve final objective values and risk-return trade-offs relative to randomized baselines under identical post-processing. Overall, the results establish a hardware-tested route for scaling financial optimization problems, defined by a trade space in which executable problem size and circuit cost are balanced against the resulting solution quality.

