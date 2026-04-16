

# Papers Found on: 2026-04-16

### Simulating the dynamics of an SU(2) matrix model on a trapped-ion quantum computer
* **Authors:** Gavin S. Hartnett et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.14094v1
* **Abstract:** Matrix models are an important class of systems in string theory and theoretical physics, with applications to random matrix theory, quantum chaos, and black holes. Hamiltonian Monte Carlo simulations and gauge/gravity duality have been used to study these systems at thermal equilibrium, and the bootstrap program has been used to efficiently determine operator expectation values by imposing positivity constraints. However, simulating real-time, non-equilibrium dynamics remains a fundamental challenge. In this work, we present the first digital quantum simulation of a bosonic matrix model, executed on the Quantinuum System Model H2 trapped-ion quantum computer. We focus on an $\mathrm{SU}(2)$ gauge theory with a quartic potential as it is simple enough to validate against exact classical solutions and yet complex enough to reflect the non-local structure of larger theories. Using the Loschmidt echo as our primary dynamical observable, we systematically decompose simulation errors into three distinct sources: Hilbert space truncation, Trotterization, and hardware noise. We demonstrate a new post-selection scheme that detects and discards gauge-symmetry violations in the Fock basis and show that at small scales it, along with zero-noise extrapolation, can give modest improvements in fidelity. These approaches struggle to scale to larger system sizes in their current implementations, emphasizing the need to move beyond them and to focus on depth reduction through improved compilation and unitary synthesis, and run-time error handling such as additional error suppression, error detection, as well as error correction approaches. This work establishes a foundation for extending digital quantum simulation to more complex matrix models -- revealing that fundamental challenges in qubit resources and circuit depth remain formidable obstacles for scaling to holographically interesting regimes.

### dqc_simulator: an easy-to-use distributed quantum computing simulator
* **Authors:** Kenny Campbell et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.13909v1
* **Abstract:** Distributed quantum computing (DQC) is a promising proposal for overcoming the scalability challenges of quantum computing. However, the evaluation of DQC hardware and software is difficult due to the relative dearth of classical simulation tools available for DQC devices. In this work, we introduce dqc_simulator, a novel simulation toolkit, written in Python, which automates many of the most challenging aspects of the DQC simulation workflow. dqc_simulator enables the easy simulation of both hardware and software, making it easy to create realistic and robust tests and benchmarks for the full DQC stack.

### Critical point search and linear response theory for computing electronic excitation energies of molecular systems. Part II. CASSCF
* **Authors:** Laura Grazioli et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.13753v1
* **Abstract:** The computation of excited states within the Complete Active Space Self-Consistent Field (CASSCF) framework remains a significant challenge in quantum chemistry, both theoretically and algorithmically. In this work, we extend the Kähler manifold formalism introduced in Part I of this series to the CASSCF theory, and draw a geometrical connection from the time-dependent CASSCF equations to state-specific and linear response methodologies for excited states. This is achieved by first investigating the underlying CASSCF manifold and identifying its Kähler structure, which is complicated by the nontrivial coupling of CI and orbital degrees of freedom. Building on these theoretical findings, we derive the CASSCF linear response equations in a straightforward manner, and develop a robust state-specific method that relies solely on first-order derivatives of the CASSCF energy functional. Numerical results on representative molecular systems-water, formaldehyde, and ethylene-demonstrate the effectiveness of the proposed state-specific method, while revealing the difficulty of reliable identification of excited states due to nonlinearity induced by the CASSCF theory.

### Quantum computing for effective nuclear lattice model
* **Authors:** Zhushuo Liu et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.13430v1
* **Abstract:** Nuclear lattice effective field theory has become an important framework for quantum many-body calculations in nuclear physics, yet its classical implementation remains increasingly challenging for more general interactions and larger systems. In this work, we develop a quantum-computing framework for a three-dimensional nuclear lattice model. We construct a variational quantum eigensolver framework and systematically compare the Jordan-Wigner and Gray code encodings. Our analysis shows that for the few-body systems considered here, Gray code combined with symmetry reduction yields a substantially more compact qubit representation. Based on this framework, we perform numerical studies for $^{2}\mathrm{H}$, $^{3}\mathrm{H}$, and $^{4}\mathrm{He}$ on finite lattices. The calculated ground-state energies exhibit a clear approach toward the corresponding experimental binding energies as the lattice size increases. These results provide a proof-of-principle foundation for future quantum simulations of nuclear many-body problems.

### Quantum computational displacement sensing
* **Authors:** Sridhar Prabhu et al.
* **Published (v1):** 2026-04-14
* **Updated:** 2026-04-14
* **Link:** http://arxiv.org/abs/2604.13177v1
* **Abstract:** Quantum computational sensing (QCS) combines quantum sensing with quantum computing to extract task-relevant information from the physical world. QCS can in principle achieve an accuracy advantage for specific tasks versus the alternative of raw-signal estimation using conventional quantum sensing followed by task-specific classical postprocessing. Here we report the experimental demonstration of quantum computational displacement sensing (QCDS) with a superconducting circuit comprising a qubit coupled to an oscillator. We consider binary classification sensing tasks, where the goal is to predict the class label of a single complex-valued displacement sensed once by the oscillator. Rather than estimating the displacement, our computational-sensing protocol -- using parameterized quantum circuits before and after sensing -- attempts to determine the binary class label using quantum processing and map it onto the ground or excited state of the qubit. A single measurement of the qubit directly outputs the prediction. We implemented circuits with up to 24 entangling gates and 38 free parameters, which were trained in silico. We show that increasing the circuit depth systematically improves expressivity and classification accuracy. We experimentally obtained an accuracy advantage over a suite of protocols that first use conventional quantum sensing to estimate the displacement before using classical postprocessing to perform prediction. For certain tasks, our protocol achieves a 15-percentage-points higher classification accuracy than the best conventional approach considered. Our results establish the feasibility of quantum computational sensing with noisy superconducting hardware and illustrate how integrating quantum computation with quantum sensing can enhance performance when the goal is to estimate a property or function of a signal rather than to estimate the signal.

### Entanglement in a molecular Lieb-lattice quantum computing circuit: A tensor network study
* **Authors:** Wei Wu et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.13093v1
* **Abstract:** Here a finite-Lieb-lattice quantum computing circuit consisting of spin-1/2 quantum bits (qubits) and triplet couplers is designed. Important gradient - quantum entanglement - is analysed. This type of design could be realised in a vast range of molecules containing multiple radicals, in which the communications among qubits are controlled by the optically driven triplets. The von Neumann entanglement entropy, reduced density matrices, and spin-spin correlations were computed using tensor-network methods by varying the magnetic anisotropy and external magnetic field. This work uncovers the rich entanglement patterns, quantum phase transitions, and tunable spin coherence in this mixed spin system, designed for molecular spin-based quantum computing. These findings have important implications for triplet-mediated molecular self-assembly quantum computing circuit, especially for the entangling gate based on molecules. This work would provide a theoretical cornerstone for the experimental realisation of scalable molecule-based quantum computing circuits.



# Papers Found on: 2026-04-16

### Simulating the dynamics of an SU(2) matrix model on a trapped-ion quantum computer
* **Authors:** Gavin S. Hartnett et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.14094v1
* **Abstract:** Matrix models are an important class of systems in string theory and theoretical physics, with applications to random matrix theory, quantum chaos, and black holes. Hamiltonian Monte Carlo simulations and gauge/gravity duality have been used to study these systems at thermal equilibrium, and the bootstrap program has been used to efficiently determine operator expectation values by imposing positivity constraints. However, simulating real-time, non-equilibrium dynamics remains a fundamental challenge. In this work, we present the first digital quantum simulation of a bosonic matrix model, executed on the Quantinuum System Model H2 trapped-ion quantum computer. We focus on an $\mathrm{SU}(2)$ gauge theory with a quartic potential as it is simple enough to validate against exact classical solutions and yet complex enough to reflect the non-local structure of larger theories. Using the Loschmidt echo as our primary dynamical observable, we systematically decompose simulation errors into three distinct sources: Hilbert space truncation, Trotterization, and hardware noise. We demonstrate a new post-selection scheme that detects and discards gauge-symmetry violations in the Fock basis and show that at small scales it, along with zero-noise extrapolation, can give modest improvements in fidelity. These approaches struggle to scale to larger system sizes in their current implementations, emphasizing the need to move beyond them and to focus on depth reduction through improved compilation and unitary synthesis, and run-time error handling such as additional error suppression, error detection, as well as error correction approaches. This work establishes a foundation for extending digital quantum simulation to more complex matrix models -- revealing that fundamental challenges in qubit resources and circuit depth remain formidable obstacles for scaling to holographically interesting regimes.

### dqc_simulator: an easy-to-use distributed quantum computing simulator
* **Authors:** Kenny Campbell et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.13909v1
* **Abstract:** Distributed quantum computing (DQC) is a promising proposal for overcoming the scalability challenges of quantum computing. However, the evaluation of DQC hardware and software is difficult due to the relative dearth of classical simulation tools available for DQC devices. In this work, we introduce dqc_simulator, a novel simulation toolkit, written in Python, which automates many of the most challenging aspects of the DQC simulation workflow. dqc_simulator enables the easy simulation of both hardware and software, making it easy to create realistic and robust tests and benchmarks for the full DQC stack.

### Critical point search and linear response theory for computing electronic excitation energies of molecular systems. Part II. CASSCF
* **Authors:** Laura Grazioli et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.13753v1
* **Abstract:** The computation of excited states within the Complete Active Space Self-Consistent Field (CASSCF) framework remains a significant challenge in quantum chemistry, both theoretically and algorithmically. In this work, we extend the Kähler manifold formalism introduced in Part I of this series to the CASSCF theory, and draw a geometrical connection from the time-dependent CASSCF equations to state-specific and linear response methodologies for excited states. This is achieved by first investigating the underlying CASSCF manifold and identifying its Kähler structure, which is complicated by the nontrivial coupling of CI and orbital degrees of freedom. Building on these theoretical findings, we derive the CASSCF linear response equations in a straightforward manner, and develop a robust state-specific method that relies solely on first-order derivatives of the CASSCF energy functional. Numerical results on representative molecular systems-water, formaldehyde, and ethylene-demonstrate the effectiveness of the proposed state-specific method, while revealing the difficulty of reliable identification of excited states due to nonlinearity induced by the CASSCF theory.

### Quantum computing for effective nuclear lattice model
* **Authors:** Zhushuo Liu et al.
* **Published (v1):** 2026-04-15
* **Updated:** 2026-04-15
* **Link:** http://arxiv.org/abs/2604.13430v1
* **Abstract:** Nuclear lattice effective field theory has become an important framework for quantum many-body calculations in nuclear physics, yet its classical implementation remains increasingly challenging for more general interactions and larger systems. In this work, we develop a quantum-computing framework for a three-dimensional nuclear lattice model. We construct a variational quantum eigensolver framework and systematically compare the Jordan-Wigner and Gray code encodings. Our analysis shows that for the few-body systems considered here, Gray code combined with symmetry reduction yields a substantially more compact qubit representation. Based on this framework, we perform numerical studies for $^{2}\mathrm{H}$, $^{3}\mathrm{H}$, and $^{4}\mathrm{He}$ on finite lattices. The calculated ground-state energies exhibit a clear approach toward the corresponding experimental binding energies as the lattice size increases. These results provide a proof-of-principle foundation for future quantum simulations of nuclear many-body problems.

### Quantum computational displacement sensing
* **Authors:** Sridhar Prabhu et al.
* **Published (v1):** 2026-04-14
* **Updated:** 2026-04-14
* **Link:** http://arxiv.org/abs/2604.13177v1
* **Abstract:** Quantum computational sensing (QCS) combines quantum sensing with quantum computing to extract task-relevant information from the physical world. QCS can in principle achieve an accuracy advantage for specific tasks versus the alternative of raw-signal estimation using conventional quantum sensing followed by task-specific classical postprocessing. Here we report the experimental demonstration of quantum computational displacement sensing (QCDS) with a superconducting circuit comprising a qubit coupled to an oscillator. We consider binary classification sensing tasks, where the goal is to predict the class label of a single complex-valued displacement sensed once by the oscillator. Rather than estimating the displacement, our computational-sensing protocol -- using parameterized quantum circuits before and after sensing -- attempts to determine the binary class label using quantum processing and map it onto the ground or excited state of the qubit. A single measurement of the qubit directly outputs the prediction. We implemented circuits with up to 24 entangling gates and 38 free parameters, which were trained in silico. We show that increasing the circuit depth systematically improves expressivity and classification accuracy. We experimentally obtained an accuracy advantage over a suite of protocols that first use conventional quantum sensing to estimate the displacement before using classical postprocessing to perform prediction. For certain tasks, our protocol achieves a 15-percentage-points higher classification accuracy than the best conventional approach considered. Our results establish the feasibility of quantum computational sensing with noisy superconducting hardware and illustrate how integrating quantum computation with quantum sensing can enhance performance when the goal is to estimate a property or function of a signal rather than to estimate the signal.

### Entanglement in a molecular Lieb-lattice quantum computing circuit: A tensor network study
* **Authors:** Wei Wu et al.
* **Published (v1):** 2026-04-08
* **Updated:** 2026-04-08
* **Link:** http://arxiv.org/abs/2604.13093v1
* **Abstract:** Here a finite-Lieb-lattice quantum computing circuit consisting of spin-1/2 quantum bits (qubits) and triplet couplers is designed. Important gradient - quantum entanglement - is analysed. This type of design could be realised in a vast range of molecules containing multiple radicals, in which the communications among qubits are controlled by the optically driven triplets. The von Neumann entanglement entropy, reduced density matrices, and spin-spin correlations were computed using tensor-network methods by varying the magnetic anisotropy and external magnetic field. This work uncovers the rich entanglement patterns, quantum phase transitions, and tunable spin coherence in this mixed spin system, designed for molecular spin-based quantum computing. These findings have important implications for triplet-mediated molecular self-assembly quantum computing circuit, especially for the entangling gate based on molecules. This work would provide a theoretical cornerstone for the experimental realisation of scalable molecule-based quantum computing circuits.

