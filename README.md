

# Papers Found on: 2026-01-09

### QNeRF: Neural Radiance Fields on a Simulated Gate-Based Quantum Computer
* **Authors:** Daniele Lizzio Bosco et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.05250v1
* **Abstract:** Recently, Quantum Visual Fields (QVFs) have shown promising improvements in model compactness and convergence speed for learning the provided 2D or 3D signals. Meanwhile, novel-view synthesis has seen major advances with Neural Radiance Fields (NeRFs), where models learn a compact representation from 2D images to render 3D scenes, albeit at the cost of larger models and intensive training. In this work, we extend the approach of QVFs by introducing QNeRF, the first hybrid quantum-classical model designed for novel-view synthesis from 2D images. QNeRF leverages parameterised quantum circuits to encode spatial and view-dependent information via quantum superposition and entanglement, resulting in more compact models compared to the classical counterpart. We present two architectural variants. Full QNeRF maximally exploits all quantum amplitudes to enhance representational capabilities. In contrast, Dual-Branch QNeRF introduces a task-informed inductive bias by branching spatial and view-dependent quantum state preparations, drastically reducing the complexity of this operation and ensuring scalability and potential hardware compatibility. Our experiments demonstrate that -- when trained on images of moderate resolution -- QNeRF matches or outperforms classical NeRF baselines while using less than half the number of parameters. These results suggest that quantum machine learning can serve as a competitive alternative for continuous signal representation in mid-level tasks in computer vision, such as 3D representation learning from 2D observations.

### A new code for computing differentially rotating neutron stars
* **Authors:** Samuel D. Tootle et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.05176v1
* **Abstract:** We present new initial data codes for constructing stationary, axisymmetric equilibrium models of differentially rotating neutron stars in full general relativity within the Frankfurt University/KADATH (FUKA) suite of initial data codes. FUKA leverages the KADATH spectral library to solve the Einstein equations under the assumption of an isentropic fluid without magnetic fields while incorporating GRHayLEOS to support 3D tabulated equations of state in \textit{stellar collapse} format. The two solvers explored in this work include one using quasi-isotropic coordinates (QIC) in Spherical coordinates while the other solves the eXtended Conformal Thin Sandwich (XCTS) decomposition in Cartesian coordinates, enabling the construction of equilibrium configurations with high accuracy and efficiency. In this work we adopt the Komatsu-Eriguchi-Hachisu differential rotation law, however, the code is designed to be extensible to other rotation laws, allowing for exploration of physically relevant sequences and critical rotation thresholds. Furthermore, we perform convergence tests demonstrating the exponential accuracy of the spectral approach, we validate QIC and XCTS solutions against models well-studied in the literature, and we also compare FUKA solutions against the well-known RNS code. Finally, we explore the impact that initial data resolution has on dynamical simulations and recover the convergence order of the evolution scheme, the dominate source of error in this study. The new FUKA codes and results presented here lay the foundation for future extensions to more general configurations, including magnetic fields, removal of isentropic assumptions, and binary systems, and have been made publicly available to support community efforts in modeling differentially rotating relativistic stars.

### On non-Archimedean quantum mathematics and non-Archimedean (quantum) computation
* **Authors:** Nikolaj Glazunov et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.05133v1
* **Abstract:** We consider selected aspects of (non-Archimedean) quantum mathematics and non-Archimedean (quantum) computation.

### Noise tailoring for error mitigation and for diagnozing digital quantum computers
* **Authors:** Thibault Scoquart et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.04830v1
* **Abstract:** Error mitigation (EM) methods are crucial for obtaining reliable results in the realm of noisy intermediate-scale quantum (NISQ) computers, where noise significantly impacts output accuracy. Some EM protocols are particularly efficient for specific types of noise. Yet the noise in the actual hardware may not align with that. In this article, we introduce Noise Tailoring (NT) -- an innovative strategy designed to modify the structure of the noise associated with two-qubit gates through statistical sampling. We perform classical emulation of the protocol behavior and find that the NT+EM results can be up to 5 times more accurate than the results of EM alone for realistic Pauli noise acting on two-qubit gates. At the same time, on actual IBM quantum computers, the NT method falls victim to various small error sources beyond Markovian Pauli noise. We propose to use the NT method for characterizing such error sources on quantum computers in order to inform hardware development.

### PACOX: A FPGA-based Pauli Composer Accelerator for Pauli String Computation
* **Authors:** Tran Xuan Hieu Le et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.04827v1
* **Abstract:** Pauli strings are a fundamental computational primitive in hybrid quantum-classical algorithms. However, classical computation of Pauli strings suffers from exponential complexity and quickly becomes a performance bottleneck as the number of qubits increases. To address this challenge, this paper proposes the Pauli Composer Accelerator (PACOX), the first dedicated FPGA-based accelerator for Pauli string computation. PACOX employs a compact binary encoding with XOR-based index permutation and phase accumulation. Based on this formulation, we design a parallel and pipelined processing element (PE) cluster architecture that efficiently exploits data-level parallelism on FPGA. Experimental results on a Xilinx ZCU102 FPGA show that PACOX operates at 250 MHz with a dynamic power consumption of 0.33 W, using 8,052 LUTs, 10,934 FFs, and 324 BRAMs. For Pauli strings of up to 19 qubits, PACOX achieves speedups of up to 100 times compared with state-of-the-art CPU-based methods, while requiring significantly less memory and achieving a much lower power-delay product. These results demonstrate that PACOX delivers high computational speed with superior energy efficiency for Pauli-based workloads in hybrid quantum-classical systems.

### Quantum Wiener architecture for quantum reservoir computing
* **Authors:** Alessio Benavoli et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.04812v1
* **Abstract:** This work focuses on quantum reservoir computing and, in particular, on quantum Wiener architectures (qWiener), consisting of quantum linear dynamic networks with weak continuous measurements and classical nonlinear static readouts. We provide the first rigorous proof that qWiener systems retain the fading-memory property and universality of classical Wiener architectures, despite quantum constraints on linear dynamics and measurement back-action. Furthermore, we develop a kernel-theoretic interpretation showing that qWiener reservoirs naturally induce deep kernels, providing a principled framework for analysing their expressiveness. We further characterise the simplest qWiener instantiation, consisting of concatenated quantum harmonic oscillators, and show the difference with respect to the classical case. Finally, we empirically evaluate the architecture on standard reservoir computing benchmarks, demonstrating systematic performance gains over prior classical and quantum reservoir computing models.

### Solving nonlinear differential equations on noisy $156$-qubit quantum computers
* **Authors:** Karla Baumann et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04439v1
* **Abstract:** In this paper, we report on the resolution of nonlinear differential equations using IBM's quantum platform. More specifically, we demonstrate that the hybrid classical-quantum algorithm H-DES successfully solves a one-dimensional material deformation problem and the inviscid Burgers' equation on IBM's 156-qubit quantum computers. These results constitute a step toward performing physically relevant simulations on present-day Noisy Intermediate-Scale Quantum (NISQ) devices.

### A Comprehensive Computational Framework for Materials Design, Ab Initio Modeling, and Molecular Docking
* **Authors:** Md Rakibul Karim Akanda et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04186v1
* **Abstract:** To facilitate rational molecular and materials design, this research proposes an integrated computational framework that combines stochastic simulation, ab initio quantum chemistry, and molecular docking. The suggested workflow allows systematic investigation of structural stability, binding affinity, and electronic properties across biological and materials science domains by utilizing complementary tools like Avogadro for molecular construction and visualization, AutoDock for docking and interaction analysis, and ORCA for high-level electronic structure computations. Uncertainty, configurational sampling, and optimization in high-dimensional chemical spaces are addressed by combining Monte Carlo-based and annealing-inspired techniques. The work shows how materials science ideas such as polymer design, thin films, crystalline lattices, and bioelectronic systems can be applied to drug development. On-device, open-source computational methods are viable, scalable, and economical, as demonstrated by comparative platform analysis. All things considered, the findings highlight the need of an integrated, repeatable computational pipeline for speeding up de novo molecule assembly and materials architecture while lowering experimental risk and expense.

### From Penrose to Melrose: Computing Scattering Amplitudes at Infinity for Unbounded Media
* **Authors:** Anıl Zenginoğlu et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04167v1
* **Abstract:** We develop a method to compute scattering amplitudes for the Helmholtz equation in variable, unbounded media with possibly long-range asymptotics. Combining Penrose's conformal compactification and Melrose's geometric scattering theory, we formulate the time-harmonic scattering problem on a compactified manifold with boundary and construct a two-step solver for scattering amplitudes at infinity. The construction is asymptotic: it treats a neighborhood of infinity, and is meant to couple to interior solvers via domain decomposition. The method provides far-field data without relying on explicit solutions or Green's function representation. Scattering in variable media is treated in a unified framework where both the incident and scattered fields solve the same background Helmholtz operator. Numerical experiments for constant, short-range, and long-range media with single-mode and Gaussian beam incidence demonstrate spectral convergence of the computed scattering amplitudes in all cases.

### Extracting scattering phase shift in quantum mechanics on quantum computers
* **Authors:** Peng Guo et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04092v1
* **Abstract:** We investigate the feasibility of extracting infinite volume scattering phase shift on quantum computers in a simple one-dimensional quantum mechanical model, using the formalism established in Ref.~\cite{Guo:2023ecc} that relates the integrated correlation functions (ICF) for a trapped system to the infinite volume scattering phase shifts through a weighted integral. The system is first discretized in a finite box with periodic boundary conditions, and the formalism in real time is verified by employing a contact interaction potential with exact solutions. Quantum circuits are then designed and constructed to implement the formalism on current quantum computing architectures. To overcome the fast oscillatory behavior of the integrated correlation functions in real-time simulation, different methods of post-data analysis are proposed and discussed. Test results on IBM hardware show that good agreement can be achieved with two qubits, but complete failure ensues with three qubits due to two-qubit gate operation errors and thermal relaxation errors.

### Quantum computing for multidimensional option pricing: End-to-end pipeline
* **Authors:** Julien Hok et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04049v1
* **Abstract:** This work introduces an end-to-end framework for multi-asset option pricing that combines market-consistent risk-neutral density recovery with quantum-accelerated numerical integration. We first calibrate arbitrage-free marginal distributions from European option quotes using the Normal Inverse Gaussian (NIG) model, leveraging its analytical tractability and ability to capture skewness and fat tails. Marginals are coupled via a Gaussian copula to construct joint distributions. To address the computational bottleneck of the high-dimensional integration required to solve the option pricing formula, we employ Quantum Accelerated Monte Carlo (QAMC) techniques based on Quantum Amplitude Estimation (QAE), achieving quadratic convergence improvements over classical Monte Carlo (CMC) methods. Theoretical results establish accuracy bounds and query complexity for both marginal density estimation (via cosine-series expansions) and multidimensional pricing. Empirical tests on liquid equity entities (Credit Agricole, AXA, Michelin) confirm high calibration accuracy and demonstrate that QAMC requires 10-100 times fewer queries than classical methods for comparable precision. This study provides a practical route to integrate arbitrage-aware modelling with quantum computing, highlighting implications for scalability and future extensions to complex derivatives.

### Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers
* **Authors:** Shiro Kawabata et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.03922v1
* **Abstract:** Scaling superconducting quantum computers to the fault-tolerant regime calls for a commensurate scaling of the classical control and readout stack. Today's systems largely rely on room-temperature, rack-based instrumentation connected to dilution-refrigerator cryostats through many coaxial cables. Looking ahead, superconducting fault-tolerant quantum computers (FTQCs) will likely adopt a heterogeneous quantum-classical architecture that places selected electronics at cryogenic stages -- for example, cryo-CMOS at 4~K and superconducting digital logic at 4~K and/or mK stages -- to curb wiring and thermal-load overheads. This review distills key requirements, surveys representative room-temperature and cryogenic approaches, and provides a transparent first-order accounting framework for cryoelectronics. Using an RSA-2048-scale benchmark as a concrete reference point, we illustrate how scaling targets motivate constraints on multiplexing and stage-wise cryogenic power, and discuss implications for functional partitioning across room-temperature electronics, cryo-CMOS, and superconducting logic.

### Computational hardness of estimating quantum entropies via binary entropy bounds
* **Authors:** Yupan Liu et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.03734v1
* **Abstract:** We investigate the computational hardness of estimating the quantum $α$-Rényi entropy ${\rm S}^{\tt R}_α(ρ) = \frac{\ln {\rm Tr}(ρ^α)}{1-α}$ and the quantum $q$-Tsallis entropy ${\rm S}^{\tt T}_q(ρ) = \frac{1-{\rm Tr}(ρ^q)}{q-1}$, both converging to the von Neumann entropy as the order approaches $1$. The promise problems Quantum $α$-Rényi Entropy Approximation (RényiQEA$_α$) and Quantum $q$-Tsallis Entropy Approximation (TsallisQEA$_q$) ask whether $ {\rm S}^ {\tt R}_α(ρ)$ or ${\rm S}^{\tt T}_q(ρ)$, respectively, is at least $τ_{\tt Y}$ or at most $τ_{\tt N}$, where $τ_{\tt Y} - τ_{\tt N}$ is typically a positive constant. Previous hardness results cover only the von Neumann entropy (order $1$) and some cases of the quantum $q$-Tsallis entropy, while existing approaches do not readily extend to other orders.   We establish that for all positive real orders, the rank-$2$ variants Rank2RényiQEA$_α$ and Rank2TsallisQEA$_q$ are ${\sf BQP}$-hard. Combined with prior (rank-dependent) quantum query algorithms in Wang, Guan, Liu, Zhang, and Ying (TIT 2024), Wang, Zhang, and Li (TIT 2024), and Liu and Wang (SODA 2025), our results imply:   - For all real orders $α> 0$ and $0 < q \leq 1$, LowRankRényiQEA$_α$ and LowRankTsallisQEA$_q$ are ${\sf BQP}$-complete, where both are restricted versions of RényiQEA$_α$ and TsallisQEA$_q$ with $ρ$ of polynomial rank.   - For all real order $q>1$, TsallisQEA$_q$ is ${\sf BQP}$-complete.   Our hardness results stem from reductions based on new inequalities relating the $α$-Rényi or $q$-Tsallis binary entropies of different orders, where the reductions differ substantially from previous approaches, and the inequalities are also of independent interest.

### Testing measurement-based computational phases of quantum matter on a quantum processor
* **Authors:** Ryohei Weil et al.
* **Published (v1):** 2026-01-06
* **Updated:** 2026-01-06
* **Link:** http://arxiv.org/abs/2601.03426v1
* **Abstract:** Many symmetry protected or symmetry enriched phases of quantum matter have the property that every ground state in a given such phase endows measurement based quantum computation with the same computational power. Such phases are called computational phases of quantum matter. Here, we experimentally verify four theoretical predictions for them on an IBM superconducting quantum device. We comprehensively investigate how symmetric imperfections of the resource states translate into logical decoherence, and how this decoherence is mitigated. In particular, the central experiment probes the scaling law from which the uniformity of computational power follows. We also analyze the correlated regime, where local measurements give rise to logical operations collectively. We test the prediction that densest packing of a measurement-based algorithms remains the most efficient, in spite of the correlations. Our experiments corroborate the operational stability of measurement based quantum computation in quantum phases of matter with symmetry.



# Papers Found on: 2026-01-09

### QNeRF: Neural Radiance Fields on a Simulated Gate-Based Quantum Computer
* **Authors:** Daniele Lizzio Bosco et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.05250v1
* **Abstract:** Recently, Quantum Visual Fields (QVFs) have shown promising improvements in model compactness and convergence speed for learning the provided 2D or 3D signals. Meanwhile, novel-view synthesis has seen major advances with Neural Radiance Fields (NeRFs), where models learn a compact representation from 2D images to render 3D scenes, albeit at the cost of larger models and intensive training. In this work, we extend the approach of QVFs by introducing QNeRF, the first hybrid quantum-classical model designed for novel-view synthesis from 2D images. QNeRF leverages parameterised quantum circuits to encode spatial and view-dependent information via quantum superposition and entanglement, resulting in more compact models compared to the classical counterpart. We present two architectural variants. Full QNeRF maximally exploits all quantum amplitudes to enhance representational capabilities. In contrast, Dual-Branch QNeRF introduces a task-informed inductive bias by branching spatial and view-dependent quantum state preparations, drastically reducing the complexity of this operation and ensuring scalability and potential hardware compatibility. Our experiments demonstrate that -- when trained on images of moderate resolution -- QNeRF matches or outperforms classical NeRF baselines while using less than half the number of parameters. These results suggest that quantum machine learning can serve as a competitive alternative for continuous signal representation in mid-level tasks in computer vision, such as 3D representation learning from 2D observations.

### A new code for computing differentially rotating neutron stars
* **Authors:** Samuel D. Tootle et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.05176v1
* **Abstract:** We present new initial data codes for constructing stationary, axisymmetric equilibrium models of differentially rotating neutron stars in full general relativity within the Frankfurt University/KADATH (FUKA) suite of initial data codes. FUKA leverages the KADATH spectral library to solve the Einstein equations under the assumption of an isentropic fluid without magnetic fields while incorporating GRHayLEOS to support 3D tabulated equations of state in \textit{stellar collapse} format. The two solvers explored in this work include one using quasi-isotropic coordinates (QIC) in Spherical coordinates while the other solves the eXtended Conformal Thin Sandwich (XCTS) decomposition in Cartesian coordinates, enabling the construction of equilibrium configurations with high accuracy and efficiency. In this work we adopt the Komatsu-Eriguchi-Hachisu differential rotation law, however, the code is designed to be extensible to other rotation laws, allowing for exploration of physically relevant sequences and critical rotation thresholds. Furthermore, we perform convergence tests demonstrating the exponential accuracy of the spectral approach, we validate QIC and XCTS solutions against models well-studied in the literature, and we also compare FUKA solutions against the well-known RNS code. Finally, we explore the impact that initial data resolution has on dynamical simulations and recover the convergence order of the evolution scheme, the dominate source of error in this study. The new FUKA codes and results presented here lay the foundation for future extensions to more general configurations, including magnetic fields, removal of isentropic assumptions, and binary systems, and have been made publicly available to support community efforts in modeling differentially rotating relativistic stars.

### On non-Archimedean quantum mathematics and non-Archimedean (quantum) computation
* **Authors:** Nikolaj Glazunov et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.05133v1
* **Abstract:** We consider selected aspects of (non-Archimedean) quantum mathematics and non-Archimedean (quantum) computation.

### Noise tailoring for error mitigation and for diagnozing digital quantum computers
* **Authors:** Thibault Scoquart et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.04830v1
* **Abstract:** Error mitigation (EM) methods are crucial for obtaining reliable results in the realm of noisy intermediate-scale quantum (NISQ) computers, where noise significantly impacts output accuracy. Some EM protocols are particularly efficient for specific types of noise. Yet the noise in the actual hardware may not align with that. In this article, we introduce Noise Tailoring (NT) -- an innovative strategy designed to modify the structure of the noise associated with two-qubit gates through statistical sampling. We perform classical emulation of the protocol behavior and find that the NT+EM results can be up to 5 times more accurate than the results of EM alone for realistic Pauli noise acting on two-qubit gates. At the same time, on actual IBM quantum computers, the NT method falls victim to various small error sources beyond Markovian Pauli noise. We propose to use the NT method for characterizing such error sources on quantum computers in order to inform hardware development.

### PACOX: A FPGA-based Pauli Composer Accelerator for Pauli String Computation
* **Authors:** Tran Xuan Hieu Le et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.04827v1
* **Abstract:** Pauli strings are a fundamental computational primitive in hybrid quantum-classical algorithms. However, classical computation of Pauli strings suffers from exponential complexity and quickly becomes a performance bottleneck as the number of qubits increases. To address this challenge, this paper proposes the Pauli Composer Accelerator (PACOX), the first dedicated FPGA-based accelerator for Pauli string computation. PACOX employs a compact binary encoding with XOR-based index permutation and phase accumulation. Based on this formulation, we design a parallel and pipelined processing element (PE) cluster architecture that efficiently exploits data-level parallelism on FPGA. Experimental results on a Xilinx ZCU102 FPGA show that PACOX operates at 250 MHz with a dynamic power consumption of 0.33 W, using 8,052 LUTs, 10,934 FFs, and 324 BRAMs. For Pauli strings of up to 19 qubits, PACOX achieves speedups of up to 100 times compared with state-of-the-art CPU-based methods, while requiring significantly less memory and achieving a much lower power-delay product. These results demonstrate that PACOX delivers high computational speed with superior energy efficiency for Pauli-based workloads in hybrid quantum-classical systems.

### Quantum Wiener architecture for quantum reservoir computing
* **Authors:** Alessio Benavoli et al.
* **Published (v1):** 2026-01-08
* **Updated:** 2026-01-08
* **Link:** http://arxiv.org/abs/2601.04812v1
* **Abstract:** This work focuses on quantum reservoir computing and, in particular, on quantum Wiener architectures (qWiener), consisting of quantum linear dynamic networks with weak continuous measurements and classical nonlinear static readouts. We provide the first rigorous proof that qWiener systems retain the fading-memory property and universality of classical Wiener architectures, despite quantum constraints on linear dynamics and measurement back-action. Furthermore, we develop a kernel-theoretic interpretation showing that qWiener reservoirs naturally induce deep kernels, providing a principled framework for analysing their expressiveness. We further characterise the simplest qWiener instantiation, consisting of concatenated quantum harmonic oscillators, and show the difference with respect to the classical case. Finally, we empirically evaluate the architecture on standard reservoir computing benchmarks, demonstrating systematic performance gains over prior classical and quantum reservoir computing models.

### Solving nonlinear differential equations on noisy $156$-qubit quantum computers
* **Authors:** Karla Baumann et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04439v1
* **Abstract:** In this paper, we report on the resolution of nonlinear differential equations using IBM's quantum platform. More specifically, we demonstrate that the hybrid classical-quantum algorithm H-DES successfully solves a one-dimensional material deformation problem and the inviscid Burgers' equation on IBM's 156-qubit quantum computers. These results constitute a step toward performing physically relevant simulations on present-day Noisy Intermediate-Scale Quantum (NISQ) devices.

### A Comprehensive Computational Framework for Materials Design, Ab Initio Modeling, and Molecular Docking
* **Authors:** Md Rakibul Karim Akanda et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04186v1
* **Abstract:** To facilitate rational molecular and materials design, this research proposes an integrated computational framework that combines stochastic simulation, ab initio quantum chemistry, and molecular docking. The suggested workflow allows systematic investigation of structural stability, binding affinity, and electronic properties across biological and materials science domains by utilizing complementary tools like Avogadro for molecular construction and visualization, AutoDock for docking and interaction analysis, and ORCA for high-level electronic structure computations. Uncertainty, configurational sampling, and optimization in high-dimensional chemical spaces are addressed by combining Monte Carlo-based and annealing-inspired techniques. The work shows how materials science ideas such as polymer design, thin films, crystalline lattices, and bioelectronic systems can be applied to drug development. On-device, open-source computational methods are viable, scalable, and economical, as demonstrated by comparative platform analysis. All things considered, the findings highlight the need of an integrated, repeatable computational pipeline for speeding up de novo molecule assembly and materials architecture while lowering experimental risk and expense.

### From Penrose to Melrose: Computing Scattering Amplitudes at Infinity for Unbounded Media
* **Authors:** Anıl Zenginoğlu et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04167v1
* **Abstract:** We develop a method to compute scattering amplitudes for the Helmholtz equation in variable, unbounded media with possibly long-range asymptotics. Combining Penrose's conformal compactification and Melrose's geometric scattering theory, we formulate the time-harmonic scattering problem on a compactified manifold with boundary and construct a two-step solver for scattering amplitudes at infinity. The construction is asymptotic: it treats a neighborhood of infinity, and is meant to couple to interior solvers via domain decomposition. The method provides far-field data without relying on explicit solutions or Green's function representation. Scattering in variable media is treated in a unified framework where both the incident and scattered fields solve the same background Helmholtz operator. Numerical experiments for constant, short-range, and long-range media with single-mode and Gaussian beam incidence demonstrate spectral convergence of the computed scattering amplitudes in all cases.

### Extracting scattering phase shift in quantum mechanics on quantum computers
* **Authors:** Peng Guo et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04092v1
* **Abstract:** We investigate the feasibility of extracting infinite volume scattering phase shift on quantum computers in a simple one-dimensional quantum mechanical model, using the formalism established in Ref.~\cite{Guo:2023ecc} that relates the integrated correlation functions (ICF) for a trapped system to the infinite volume scattering phase shifts through a weighted integral. The system is first discretized in a finite box with periodic boundary conditions, and the formalism in real time is verified by employing a contact interaction potential with exact solutions. Quantum circuits are then designed and constructed to implement the formalism on current quantum computing architectures. To overcome the fast oscillatory behavior of the integrated correlation functions in real-time simulation, different methods of post-data analysis are proposed and discussed. Test results on IBM hardware show that good agreement can be achieved with two qubits, but complete failure ensues with three qubits due to two-qubit gate operation errors and thermal relaxation errors.

### Quantum computing for multidimensional option pricing: End-to-end pipeline
* **Authors:** Julien Hok et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.04049v1
* **Abstract:** This work introduces an end-to-end framework for multi-asset option pricing that combines market-consistent risk-neutral density recovery with quantum-accelerated numerical integration. We first calibrate arbitrage-free marginal distributions from European option quotes using the Normal Inverse Gaussian (NIG) model, leveraging its analytical tractability and ability to capture skewness and fat tails. Marginals are coupled via a Gaussian copula to construct joint distributions. To address the computational bottleneck of the high-dimensional integration required to solve the option pricing formula, we employ Quantum Accelerated Monte Carlo (QAMC) techniques based on Quantum Amplitude Estimation (QAE), achieving quadratic convergence improvements over classical Monte Carlo (CMC) methods. Theoretical results establish accuracy bounds and query complexity for both marginal density estimation (via cosine-series expansions) and multidimensional pricing. Empirical tests on liquid equity entities (Credit Agricole, AXA, Michelin) confirm high calibration accuracy and demonstrate that QAMC requires 10-100 times fewer queries than classical methods for comparable precision. This study provides a practical route to integrate arbitrage-aware modelling with quantum computing, highlighting implications for scalability and future extensions to complex derivatives.

### Integration and Resource Estimation of Cryoelectronics for Superconducting Fault-Tolerant Quantum Computers
* **Authors:** Shiro Kawabata et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.03922v1
* **Abstract:** Scaling superconducting quantum computers to the fault-tolerant regime calls for a commensurate scaling of the classical control and readout stack. Today's systems largely rely on room-temperature, rack-based instrumentation connected to dilution-refrigerator cryostats through many coaxial cables. Looking ahead, superconducting fault-tolerant quantum computers (FTQCs) will likely adopt a heterogeneous quantum-classical architecture that places selected electronics at cryogenic stages -- for example, cryo-CMOS at 4~K and superconducting digital logic at 4~K and/or mK stages -- to curb wiring and thermal-load overheads. This review distills key requirements, surveys representative room-temperature and cryogenic approaches, and provides a transparent first-order accounting framework for cryoelectronics. Using an RSA-2048-scale benchmark as a concrete reference point, we illustrate how scaling targets motivate constraints on multiplexing and stage-wise cryogenic power, and discuss implications for functional partitioning across room-temperature electronics, cryo-CMOS, and superconducting logic.

### Computational hardness of estimating quantum entropies via binary entropy bounds
* **Authors:** Yupan Liu et al.
* **Published (v1):** 2026-01-07
* **Updated:** 2026-01-07
* **Link:** http://arxiv.org/abs/2601.03734v1
* **Abstract:** We investigate the computational hardness of estimating the quantum $α$-Rényi entropy ${\rm S}^{\tt R}_α(ρ) = \frac{\ln {\rm Tr}(ρ^α)}{1-α}$ and the quantum $q$-Tsallis entropy ${\rm S}^{\tt T}_q(ρ) = \frac{1-{\rm Tr}(ρ^q)}{q-1}$, both converging to the von Neumann entropy as the order approaches $1$. The promise problems Quantum $α$-Rényi Entropy Approximation (RényiQEA$_α$) and Quantum $q$-Tsallis Entropy Approximation (TsallisQEA$_q$) ask whether $ {\rm S}^ {\tt R}_α(ρ)$ or ${\rm S}^{\tt T}_q(ρ)$, respectively, is at least $τ_{\tt Y}$ or at most $τ_{\tt N}$, where $τ_{\tt Y} - τ_{\tt N}$ is typically a positive constant. Previous hardness results cover only the von Neumann entropy (order $1$) and some cases of the quantum $q$-Tsallis entropy, while existing approaches do not readily extend to other orders.   We establish that for all positive real orders, the rank-$2$ variants Rank2RényiQEA$_α$ and Rank2TsallisQEA$_q$ are ${\sf BQP}$-hard. Combined with prior (rank-dependent) quantum query algorithms in Wang, Guan, Liu, Zhang, and Ying (TIT 2024), Wang, Zhang, and Li (TIT 2024), and Liu and Wang (SODA 2025), our results imply:   - For all real orders $α> 0$ and $0 < q \leq 1$, LowRankRényiQEA$_α$ and LowRankTsallisQEA$_q$ are ${\sf BQP}$-complete, where both are restricted versions of RényiQEA$_α$ and TsallisQEA$_q$ with $ρ$ of polynomial rank.   - For all real order $q>1$, TsallisQEA$_q$ is ${\sf BQP}$-complete.   Our hardness results stem from reductions based on new inequalities relating the $α$-Rényi or $q$-Tsallis binary entropies of different orders, where the reductions differ substantially from previous approaches, and the inequalities are also of independent interest.

### Testing measurement-based computational phases of quantum matter on a quantum processor
* **Authors:** Ryohei Weil et al.
* **Published (v1):** 2026-01-06
* **Updated:** 2026-01-06
* **Link:** http://arxiv.org/abs/2601.03426v1
* **Abstract:** Many symmetry protected or symmetry enriched phases of quantum matter have the property that every ground state in a given such phase endows measurement based quantum computation with the same computational power. Such phases are called computational phases of quantum matter. Here, we experimentally verify four theoretical predictions for them on an IBM superconducting quantum device. We comprehensively investigate how symmetric imperfections of the resource states translate into logical decoherence, and how this decoherence is mitigated. In particular, the central experiment probes the scaling law from which the uniformity of computational power follows. We also analyze the correlated regime, where local measurements give rise to logical operations collectively. We test the prediction that densest packing of a measurement-based algorithms remains the most efficient, in spite of the correlations. Our experiments corroborate the operational stability of measurement based quantum computation in quantum phases of matter with symmetry.

