# TFIM Thermodynamics via VQE

Proof of Concept: Calculating ground state energy of the Transverse Field Ising Model using Variational Quantum Eigensolver.

## Project Structure
- `src/tfim_vqe.py`: Main implementation
- `tests/`: Test files
- `data/`: Output data and plots

## Physics Background
The Transverse Field Ising Model Hamiltonian:
H = -J Σ σ_i^z σ_{i+1}^z - h Σ σ_i^x

Where:
- J: Coupling constant (set to 1.0)
- h: Transverse field strength
- σ_i^z, σ_i^x: Pauli matrices

## Quantum Algorithm
Uses Variational Quantum Eigensolver (VQE) to find ground state energy.

## Installation
```bash
python -m venv qenv
source qenv/bin/activate
pip install -r requirements.txt

## Results & Findings

### Ground State Energy Calculation
- **2-qubit systems**: Perfect agreement between VQE and exact diagonalization
- **3-4 qubit systems**: Small errors emerge (0.16), highlighting research challenges
- **Scaling**: Hilbert space grows exponentially (2^N), classical methods become impractical

### Generated Outputs
1. `data/tfim_ground_state.png`: Ground state energy vs transverse field
2. `data/tfim_results.npz`: Numerical results for analysis
3. `data/funding_demo.png`: Demonstration plot for proposals

## Next Steps for Research & Funding

### Immediate Technical Goals
1. Extend to 8+ qubit systems (beyond classical simulation)
2. Implement finite temperature algorithms
3. Add error mitigation techniques
4. Deploy on real quantum hardware (q-bit.eu partnership)

### Funding Opportunities
- EU Quantum Flagship programs
- National quantum initiatives
- Industry partnerships for materials science
- q-bit.eu hardware access proposals

## How to Cite This Work
If using this code in research, please cite:
Quantum Thermodynamics POC: TFIM via VQE
https://github.com/shellworlds/TFIMTDMVEQ
Repository containing quantum algorithm implementation for thermodynamic property calculation.

text

## Contact
For collaboration or funding discussions: [rr@q-bit.space]
