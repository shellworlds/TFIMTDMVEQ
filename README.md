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
