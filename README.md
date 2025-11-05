# Automated arXiv Paper Tracker

This repository is my personal, automated paper tracker. It uses a GitHub Action to run a Python script every 24 hours, scraping [arXiv.org](https://arxiv.org/) for new papers that match my interests.

The keywords I'm currently tracking are defined in `config.ini`.

## Latest Papers Found

*This section is automatically updated by the script every 24 hours.*

<!-- LATEST_PAPERS_START -->

# Papers Found on: 2025-11-05

### Enhancing Federated Learning Privacy with QUBO
* **Authors:** Andras Ferenczi et al.
* **Published (v1):** 2025-11-04
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2511.02785v1
* **Abstract:** Federated learning (FL) is a widely used method for training machine learning (ML) models in a scalable way while preserving privacy (i.e., without centralizing raw data). Prior research shows that the risk of exposing sensitive data increases cumulatively as the number of iterations where a client's updates are included in the aggregated model increase. Attackers can launch membership inference attacks (MIA; deciding whether a sample or client participated), property inference attacks (PIA; inferring attributes of a client's data), and model inversion attacks (MI; reconstructing inputs), thereby inferring client-specific attributes and, in some cases, reconstructing inputs. In this paper, we mitigate risk by substantially reducing per client exposure using a quantum computing-inspired quadratic unconstrained binary optimization (QUBO) formulation that selects a small subset of client updates most relevant for each training round. In this work, we focus on two threat vectors: (i) information leakage by clients during training and (ii) adversaries who can query or obtain the global model. We assume a trusted central server and do not model server compromise. This method also assumes that the server has access to a validation/test set with global data distribution. Experiments on the MNIST dataset with 300 clients in 20 rounds showed a 95.2% per-round and 49% cumulative privacy exposure reduction, with 147 clients' updates never being used during training while maintaining in general the full-aggregation accuracy or even better. The method proved to be efficient at lower scale and more complex model as well. A CINIC-10 dataset-based experiment with 30 clients resulted in 82% per-round privacy improvement and 33% cumulative privacy.

### Quantum Network-Based Prediction of Cancer Driver Genes
* **Authors:** Patricia Marques et al.
* **Published (v1):** 2025-10-14
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2510.12628v2
* **Abstract:** Identification of cancer driver genes is fundamental for the development of targeted therapeutic interventions. The integration of mutational profiles with protein-protein interaction (PPI) networks offers a promising avenue for their detection [ 1, 2], but scaling to large network datasets is computationally demanding. Quantum computing offers compact representations and potential complexity reductions. Motivated by the classical method of Gumpinger et al. [3], in this work we introduce a supervised quantum framework that combines mutation scores with network topology via a novel state preparation scheme, Quantum Multi-order Moment Embedding (QMME). QMME encodes low-order statistical moments over the mutation scores of a node's immediate and second-order neighbors, and encodes this information into quantum states. These are used as inputs to a kernel-based quantum binary classifier that discriminates known driver genes from others. Simulations on an empirical PPI network demonstrate competitive performance, with a 12.6% recall gain over a classical baseline. The pipeline performs explicit quantum state preparation and requires no classical training, enabling an efficient, nearly end-to-end quantum workflow. A brief complexity analysis suggests the approach could achieve a quantum speedup in network-based cancer gene prediction. This work underscores the potential of supervised quantum graph learning frameworks to advance biological discovery.

### Mind the gaps: The fraught road to quantum advantage
* **Authors:** Jens Eisert et al.
* **Published (v1):** 2025-10-22
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2510.19928v2
* **Abstract:** Quantum computing is advancing rapidly, yet substantial gaps separate today's noisy intermediate-scale quantum (NISQ) devices from tomorrow's fault-tolerant application-scale quantum (FASQ) machines. We identify four related hurdles along the road ahead: (i) from error mitigation to active error detection and correction, (ii) from rudimentary error correction to scalable fault tolerance, (iii) from early heuristics to mature, verifiable algorithms, and (iv) from exploratory simulators to credible advantage in quantum simulation. Targeting these transitions will accelerate progress toward broadly useful quantum computing.

### Distributed Quantum Error Correction with Permutation-Invariant Approximate Codes
* **Authors:** Connor Clayton et al.
* **Published (v1):** 2025-09-29
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2509.25093v2
* **Abstract:** Modular quantum computing architectures require error correction schemes that remain effective in the presense of noisy inter-processor operations. We introduce a distributed quantum error correction framework based on approximate codes to address this challenge. Our approach enables concatenation of distinct local codes across modules while allowing logical operations composed primarily of processor-local gates. We derive a lower bound and present corresponding simulations which indicate that this nontraditional approach can provide marked advantage over existing approaches in the highly non-uniform error landscape of a distributed quantum computer. As a concrete realization, we present encoding and decoding circuits for the permutation-invariant W- state code and propose efficient methods for its preparation. These results highlight the potential of approximate distributed error correction strategies for scalable, modular, fault-tolerant quantum computation.

### Towards reconstructing quantum structured light on a quantum computer
* **Authors:** Mwezi Koni et al.
* **Published (v1):** 2025-09-26
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2509.21804v2
* **Abstract:** We introduce a variational quantum computing approach for reconstructing quantum states from measurement data. By mapping the reconstruction cost function onto an Ising model, the problem can be solved using a variational eigensolver on present-day quantum hardware. As a proof of concept, we demonstrate the method on quantum structured light, in particular, entangled photons carrying orbital angular momentum and show that the reconstruction procedure can yield reliable performance even on noisy devices. Our results highlight the potential of variational algorithms for efficient quantum state tomography, particularly for high-dimensional structured light, where classical approaches can face bottlenecks.

### Photonic implementation of quantum hidden subgroup database compression
* **Authors:** Qianyi Wang et al.
* **Published (v1):** 2025-11-04
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2511.02527v1
* **Abstract:** We experimentally demonstrate quantum data compression exploiting hidden subgroup symmetries using a photonic quantum processor. Classical databases containing generalized periodicities-symmetries that are in the worst cases inefficient for known classical algorithms to be detect-can efficiently compressed by quantum hidden subgroup algorithms. We implement a variational quantum autoencoder that autonomously learns both the symmetry type (e.g., $\mathbb{Z}_2 \times \mathbb{Z}_2$ vs. $\mathbb{Z}_4$) and the generalized period from structured data. The system uses single photons encoded in path, polarization, and time-bin degrees of freedom, with electronically controlled waveplates enabling tunable quantum gates. Training via gradient descent successfully identifies the hidden symmetry structure, achieving compression by eliminating redundant database entries. We demonstrate two circuit ansatzes: a parametrized generalized Fourier transform and a less-restricted architecture for Simon's symmetry. Both converge successfully, with the cost function approaching zero as training proceeds. These results provide experimental proof-of-principle that photonic quantum computers can compress classical databases by learning symmetries inaccessible to known efficient classical methods, opening pathways for quantum-enhanced information processing.

### Qonductor: A Cloud Orchestrator for Quantum Computing
* **Authors:** Emmanouil Giortamis et al.
* **Published (v1):** 2024-08-08
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2408.04312v2
* **Abstract:** We describe Qonductor, a cloud orchestrator for hybrid quantum-classical applications that run on heterogeneous hybrid resources. Qonductor abstracts away the complexity of hybrid programming and resource management by exposing the Qonductor API, a high-level and hardware-agnostic API. The resource estimator strategically balances quantum and classical resources to mitigate resource contention and the effects of hardware noise. The hybrid scheduler automates job scheduling on hybrid resources and balances the tradeoff between users' objectives of QoS and the cloud operator's objective of resource efficiency.   We implement an open-source prototype and evaluate Qonductor using more than 7000 real quantum runs on the IBM quantum cloud to simulate real cloud workloads. Qonductor achieves up to 54% lower job completion times (JCTs) while sacrificing 3% execution quality, balances the load across QPU, which increases quantum resource utilization by up to 66%, and scales with growing system sizes and loads.

### Quantum Circuit Implementation of Two Matrix Product Operations and Elementary Column Transformations
* **Authors:** Yu-Hang Liu et al.
* **Published (v1):** 2025-11-04
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2511.02413v1
* **Abstract:** This paper focuses on quantum algorithms for three key matrix operations: Hadamard (Schur) product, Kronecker (tensor) product, and elementary column transformations each. By designing specific unitary transformations and auxiliary quantum measurement, efficient quantum schemes with circuit diagrams are proposed. Their computational depths are: O(1) for Kronecker product; O(max(m,n)) for Hadamard product (linked to matrix dimensions); and O(m) for elementary column transformations of (2^n X 2^m) matrices (dependent only on column count).Notably, compared to traditional column transformation via matrix transposition and row transformations, this scheme reduces computation steps and quantum gate usage, lowering quantum computing energy costs.

### QSCL-EWIL: Quantum Stochastic Contrast Learning for Enhanced WiFi-Based Indoor Localization
* **Authors:** Muhammad Bilal Akram Dastagir et al.
* **Published (v1):** 2025-01-06
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2501.02884v2
* **Abstract:** WiFi-based indoor localization is essential for asset tracking, healthcare monitoring, and smart buildings. However, existing systems face challenges such as data variability, environmental noise, and difficulty detecting floor and building levels, compounded by limited labeled data and high received signal strength (RSS) collection costs. This paper introduces quantum stochastic contrast learning (QSCL), a novel framework grounded in rigorous theoretical foundations. We present four theorems and one lemma that establish the probabilistic augmentation, diversity enhancement, relationship preservation, and resilience of QSCL under quantum noise, supported by formal proofs. Leveraging these foundations, QSCL utilizes quantum computing (QC) to generate strong data augmentations with stochastic perturbations, enhancing data diversity, while classical weak augmentations provide subtle variations for robust feature learning. We propose a spatial temporal adaptive attention (STAA) encoder that integrates convolutional layers with adaptive attention mechanisms to capture spatial and temporal dependencies in sequential data. Furthermore, a bidirectional contrastive loss function is introduced to capture forward and reverse relationships between augmented views, ensuring robust representations. Comprehensive evaluations on the UJIIndoorLoc and UTSIndoorLoc datasets validate QSCL, demonstrating superior performance with reduced labeled data and resilience to quantum noise such as bit-flip, dephasing, and measurement noise. The proposed framework significantly improves localization accuracy, floor and building detection, and generalizability in challenging indoor environments.

### A Collaborative Framework for Quantum Optimisation and Quantum Neural Networks: Credit Feature Selection and Image Classification
* **Authors:** JiaNing Long et al.
* **Published (v1):** 2025-09-14
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2509.11110v2
* **Abstract:** This paper investigates the efficacy of quantum computing in two distinct machine learning tasks: feature selection for credit risk assessment and image classification for handwritten digit recognition. For the first task, we address the feature selection challenge of the German Credit Dataset by formulating it as a Quadratic Unconstrained Binary Optimization (QUBO) problem, which is solved using quantum annealing to identify the optimal feature subset. Experimental results show that the resulting credit scoring model maintains high classification precision despite using a minimal number of features. For the second task, we focus on classifying handwritten digits 3 and 6 in the MNIST dataset using Quantum Neural Networks (QNNs). Through meticulous data preprocessing (downsampling, binarization), quantum encoding (FRQI and compressed FRQI), and the design of QNN architectures (CRADL and CRAML), we demonstrate that QNNs can effectively handle high-dimensional image data. Our findings highlight the potential of quantum computing in solving practical machine learning problems while emphasizing the need to balance resource expenditure and model efficacy.

### Towards efficient quantum algorithms for diffusion probabilistic models
* **Authors:** Yunfei Wang et al.
* **Published (v1):** 2025-02-20
* **Updated:** 2025-11-04
* **Link:** http://arxiv.org/abs/2502.14252v2
* **Abstract:** A diffusion probabilistic model (DPM) is a generative model renowned for its ability to produce high-quality outputs in tasks such as image and audio generation. However, training DPMs on large, high-dimensional datasets such as high-resolution images or audio incurs significant computational, energy, and hardware costs. In this work, we introduce efficient quantum algorithms for implementing DPMs through various quantum ODE solvers. These algorithms highlight the potential of quantum Carleman linearization for diverse mathematical structures, leveraging state-of-the-art quantum linear system solvers (QLSS) or linear combination of Hamiltonian simulations (LCHS). Specifically, we focus on two approaches: DPM-solver-$k$ which employs exact $k$-th order derivatives to compute a polynomial approximation of $\epsilon_\theta(x_\lambda,\lambda)$; and UniPC which uses finite difference of $\epsilon_\theta(x_\lambda,\lambda)$ at different points $(x_{s_m}, \lambda_{s_m})$ to approximate higher-order derivatives. As such, this work represents one of the most direct and pragmatic applications of quantum algorithms to large-scale machine learning models, presumably taking substantial steps towards demonstrating the practical utility of quantum computing.

### Software for Creating Scalable Benchmarks from Quantum Algorithms
* **Authors:** Noah Siekierski et al.
* **Published (v1):** 2025-11-03
* **Updated:** 2025-11-03
* **Link:** http://arxiv.org/abs/2511.02134v1
* **Abstract:** Creating scalable, reliable, and well-motivated benchmarks for quantum computers is challenging: straightforward approaches to benchmarking suffer from exponential scaling, are insensitive to important errors, or use poorly-motivated performance metrics. Furthermore, curated benchmarking suites cannot include every interesting quantum circuit or algorithm, which necessitates a tool that enables the easy creation of new benchmarks. In this work, we introduce a software tool for creating scalable and reliable benchmarks that measure a well-motivated performance metric (process fidelity) from user-chosen quantum circuits and algorithms. Our software, called $\texttt{scarab}$, enables the creation of efficient and robust benchmarks even from circuits containing thousands or millions of qubits, by employing efficient fidelity estimation techniques, including mirror circuit fidelity estimation and subcircuit volumetric benchmarking. $\texttt{scarab}$ provides a simple interface that enables the creation of reliable benchmarks by users who are not experts in the theory of quantum computer benchmarking or noise. We demonstrate the flexibility and power of $\texttt{scarab}$ by using it to turn existing inefficient benchmarks into efficient benchmarks, to create benchmarks that interrogate hardware and algorithmic trade-offs in Hamiltonian simulation, to quantify the in-situ efficacy of approximate circuit compilation, and to create benchmarks that use subcircuits to measure progress towards executing a circuit of interest.

### Superconducting pairing correlations on a trapped-ion quantum computer
* **Authors:** Etienne Granet et al.
* **Published (v1):** 2025-11-03
* **Updated:** 2025-11-03
* **Link:** http://arxiv.org/abs/2511.02125v1
* **Abstract:** The Fermi-Hubbard model is the starting point for the simulation of many strongly correlated materials, including high-temperature superconductors, whose modelling is a key motivation for the construction of quantum simulation and computing devices. However, the detection of superconducting pairing correlations has so far remained out of reach, both because of their off-diagonal character-which makes them inaccessible to local density measurements-and because of the difficulty of preparing superconducting states. Here, we report measurement of significant pairing correlations in three different regimes of Fermi-Hubbard models simulated on Quantinuum\'s Helios trapped-ion quantum computer. Specifically, we measure non-equilibrium pairing induced by an electromagnetic field in the half-filled square lattice model, d-wave pairing in an approximate ground state of the checkerboard Hubbard model at $1/6$-doping, and s-wave pairing in a bilayer model relevant to nickelate superconductors. These results show that a quantum computer can reliably create and probe physically relevant states with superconducting pairing correlations, opening a path to the exploration of superconductivity with quantum computers.

### Current Cross-Correlation Spectroscopy of Majorana Bound States
* **Authors:** Michael Ridley et al.
* **Published (v1):** 2025-11-03
* **Updated:** 2025-11-03
* **Link:** http://arxiv.org/abs/2511.02085v1
* **Abstract:** The clock speed of topological quantum computers based on Majorana zero mode (MZM)-supporting nanoscale devices is determined by the time taken for electrons to traverse the device. We employ the time-dependent Landauer-B{\"u}ttiker transport theory for current cross-lead correlations in a superconducting nanowire junction hosting MZMs. From the time-dependent quantum noise, we are able to extract traversal times for electrons crossing the system. After demonstrating a linear scaling of traversal times with nanowire length, we present a heuristic formula for the traversal times which accurately captures their behaviour. We then connect our framework to a proposed experimental verification of this discriminant between spurious and genuine MZMs utilizing time-resolved transport measurements.

### MediQ-GAN: Quantum-Inspired GAN for High Resolution Medical Image Generation
* **Authors:** Qingyue Jiao et al.
* **Published (v1):** 2025-06-26
* **Updated:** 2025-11-03
* **Link:** http://arxiv.org/abs/2506.21015v2
* **Abstract:** Machine learning-assisted diagnosis shows promise, yet medical imaging datasets are often scarce, imbalanced, and constrained by privacy, making data augmentation essential. Classical generative models typically demand extensive computational and sample resources. Quantum computing offers a promising alternative, but existing quantum-based image generation methods remain limited in scale and often face barren plateaus. We present MediQ-GAN, a quantum-inspired GAN with prototype-guided skip connections and a dual-stream generator that fuses classical and quantum-inspired branches. Its variational quantum circuits inherently preserve full-rank mappings, avoid rank collapse, and are theory-guided to balance expressivity with trainability. Beyond generation quality, we provide the first latent-geometry and rank-based analysis of quantum-inspired GANs, offering theoretical insight into their performance. Across three medical imaging datasets, MediQ-GAN outperforms state-of-the-art GANs and diffusion models. While validated on IBM hardware for robustness, our contribution is hardware-agnostic, offering a scalable and data-efficient framework for medical image generation and augmentation.

### Towards Continuous-variable Quantum Neural Networks for Biomedical Imaging
* **Authors:** Daniel Alejandro Lopez et al.
* **Published (v1):** 2025-11-03
* **Updated:** 2025-11-03
* **Link:** http://arxiv.org/abs/2511.02051v1
* **Abstract:** Continuous-variable (CV) quantum computing offers a promising framework for scalable quantum machine learning, leveraging optical systems with infinite-dimensional Hilbert spaces. While discrete-variable (DV) quantum neural networks have shown remarkable progress in various computer vision tasks, CV quantum models remain comparatively underexplored. In this work, we present a feasibility study of continuous-variable quantum neural networks (CV-QCNNs) applied to biomedical image classification. Utilizing photonic circuit simulation frameworks, we construct CV quantum circuits composed of Gaussian gates, such as displacement, squeezing, rotation, and beamsplitters to emulate convolutional behavior. Our experiments are conducted on the MedMNIST dataset collection, a set of annotated medical image benchmarks for multiple diagnostic tasks. We evaluate CV-QCNN's performance in terms of classification accuracy, model expressiveness, and resilience to Gaussian noise, comparing against classical CNNs and equivalent DV quantum circuits. This study aims to identify trade-offs between DV and CV paradigms for quantum-enhanced medical imaging. Our results highlight the potential of continuous-variable models and their viability for future computer-aided diagnosis systems.

### Efficient Quantum Implementation of Dynamical Mean Field Theory for Correlated Materials
* **Authors:** Norman Hogan et al.
* **Published (v1):** 2025-08-07
* **Updated:** 2025-11-03
* **Link:** http://arxiv.org/abs/2508.05738v3
* **Abstract:** The accurate theoretical description of materials with strongly correlated electrons is a formidable challenge in condensed matter physics and computational chemistry. Dynamical Mean Field Theory (DMFT) is a successful approach that predicts behaviors of such systems by incorporating some of the correlated behavior using an impurity model, but it is limited by the need to calculate the impurity Green's function. This work proposes a framework for DMFT calculations on quantum computers, focusing on near-term applications. It leverages the structure of the impurity problem, combining a low-rank Gaussian subspace representation of the ground state and a compressed, short-depth quantum circuit that joins state preparation with time evolution to compute Green's functions. We demonstrate the convergence of the DMFT algorithm using the Gaussian subspace in a noise-free setting, and show the hardware viability of circuit compression by extracting the impurity Green's function on IBM quantum processors for a single impurity coupled to three bath orbitals (8 qubits, 1 ancilla). We discuss potential paths toward realizing this quantum computing use case in materials science.

### Unlocking early fault-tolerant quantum computing with mitigated magic dilution
* **Authors:** Surabhi Luthra et al.
* **Published (v1):** 2025-05-15
* **Updated:** 2025-11-03
* **Link:** http://arxiv.org/abs/2505.10513v2
* **Abstract:** As quantum computing progresses towards the early fault-tolerant regime, quantum error correction will play a crucial role in protecting qubits and enabling logical Clifford operations. However, the number of logical qubits will initially remain limited, posing challenges for resource-intensive tasks like magic state distillation. It is therefore essential to develop efficient methods for implementing non-Clifford operations, such as small-angle rotations, to maximise the computational capabilities of devices within these constraints. In this work, we introduce mitigated magic dilution (MMD) as an approach to synthesise small-angle rotations by employing quantum error mitigation techniques to sample logical Clifford circuits given noisy encoded magic states. We explore the utility of our approach for the simulation of the 2D Fermi-Hubbard model. We identify evolution time regimes where MMD outperforms the Ross-Selinger gate synthesis method [Quantum Inf.\ Comp.\ \textbf{16}, 901-953 (2016), arXiv:1403.2975] in the number of noisy encoded magic states required for square lattices up to size $8 \times 8$. Moreover, we demonstrate that our method can provide a practical advantage which is quantified by a better-than-quadratic improvement in the resource requirements for small-angle rotations over classical simulators. This work paves the way for early fault-tolerant demonstrations on devices supporting millions of quantum operations, the so-called MegaQuOp regime.

<!-- LATEST_PAPERS_END -->

## Full Archive

A complete, persistent JSON database of all papers found by this tracker is available in the `data/archive.json` file.