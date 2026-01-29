# Research Challenges Identified in POC

## Current Limitations & Opportunities

### 1. Scaling Challenges (3-4 qubits)
- **2 qubits**: Perfect VQE results (error: 0.000000)
- **3 qubits**: Small error emerges (error: 0.164024)
- **4 qubits**: Error persists (error: 0.166422)

**Implication**: Ansatz expressibility or optimization becomes limiting.
**Solution needed**: Better variational forms, adaptive ansatzes, or error mitigation.

### 2. Thermodynamic Property Extension
Current POC calculates only ground state energy (T=0).
**Next step**: Finite temperature properties require:
- Excited state calculations
- Partition function estimation
- Free energy, entropy, specific heat

### 3. Hardware Deployment Readiness
**Qiskit compatibility**: ✓ Ready for q-bit.eu hardware
**Validation suite**: ✓ Classical benchmarks available
**Scaling tests**: ✓ Up to 4 qubits demonstrated

### 4. Funding Justification Points
1. **Algorithm improvement needed** for >4 qubits
2. **Thermodynamic extension** requires new quantum algorithms
3. **Hardware validation** needs real quantum processor access
4. **Industry applications** require specific material models

## Proposed Research Questions
1. Can adaptive ansatzes reduce VQE error for 8+ qubit systems?
2. How do we efficiently compute finite-temperature properties on NISQ devices?
3. What error mitigation strategies work best for thermodynamic observables?
4. Which material systems show earliest quantum advantage?
