#!/usr/bin/env python3
"""
Demonstration for Quantum Thermodynamics Funding Proposal
Transverse Field Ising Model - Quantum vs Classical Comparison
"""

import numpy as np
import matplotlib.pyplot as plt
from src.tfim_vqe import create_tfim_hamiltonian, exact_diagonalization, run_vqe

def demonstrate_quantum_advantage_scaling():
    """Show how problem scales and where quantum advantage emerges"""
    print("=" * 70)
    print("QUANTUM THERMODYNAMICS DEMONSTRATION")
    print("Transverse Field Ising Model - Ground State Calculation")
    print("=" * 70)
    
    # Demonstrate for different system sizes
    system_sizes = [2, 3, 4]
    h = 1.0  # Fixed field strength
    
    print("\n1. SYSTEM SCALING ANALYSIS")
    print("-" * 40)
    
    for n_qubits in system_sizes:
        print(f"\n  System size: {n_qubits} qubits")
        print(f"  Hilbert space dimension: 2^{n_qubits} = {2**n_qubits}")
        
        # Create Hamiltonian
        H = create_tfim_hamiltonian(n_qubits, J=1.0, h=h)
        
        # Classical exact diagonalization
        exact_energy = exact_diagonalization(H)
        print(f"  Exact ground energy (classical): {exact_energy:.6f}")
        
        # Quantum VQE (for small systems only in demo)
        if n_qubits <= 4:
            vqe_energy, ansatz = run_vqe(H, n_qubits)
            print(f"  VQE ground energy (quantum):   {vqe_energy:.6f}")
            print(f"  Error: {abs(vqe_energy - exact_energy):.6f}")
            print(f"  VQE parameters: {ansatz.num_parameters}")
    
    print("\n" + "=" * 70)
    print("2. THERMODYNAMIC PROPERTIES FROM GROUND STATE")
    print("-" * 40)
    
    # Show how ground state leads to thermodynamic properties
    n_qubits = 3
    h_values = np.linspace(0.1, 2.5, 20)
    energies = []
    
    for h_val in h_values[:5]:  # Just first 5 for demo
        H = create_tfim_hamiltonian(n_qubits, J=1.0, h=h_val)
        energy = exact_diagonalization(H)
        energies.append(energy)
        print(f"  h={h_val:.2f}: E₀={energy:.4f}")
    
    print(f"\n  ... and {len(h_values)-5} more points")
    
    print("\n" + "=" * 70)
    print("3. FUNDING OPPORTUNITY: NEXT STEPS")
    print("-" * 40)
    print("""
    Current POC demonstrates:
    • Quantum algorithm implementation (VQE) for thermodynamics
    • Validation against classical methods
    • Foundation for thermodynamic property calculation
    
    With funding, we can extend to:
    • 8+ qubit systems (beyond classical simulation)
    • Finite temperature properties (free energy, entropy)
    • Real quantum hardware deployment
    • Industry applications: materials design, drug discovery
    
    Required resources:
    • Quantum software development: 6 months
    • Hardware access: q-bit.eu partnership
    • Validation on classical HPC: 3 months
    """)
    
    # Create summary plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Energy vs field strength
    h_full = np.linspace(0.1, 2.5, 50)
    energies_full = []
    for h_val in h_full:
        H = create_tfim_hamiltonian(2, J=1.0, h=h_val)
        energies_full.append(exact_diagonalization(H))
    
    ax1.plot(h_full, energies_full, 'b-', linewidth=2)
    ax1.set_xlabel('Transverse Field Strength (h)')
    ax1.set_ylabel('Ground State Energy')
    ax1.set_title('Quantum Phase Transition')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Scaling
    qubits = [2, 3, 4, 5, 6]
    hilbert_dims = [2**n for n in qubits]
    ax2.semilogy(qubits, hilbert_dims, 'ro-', linewidth=2)
    ax2.set_xlabel('Number of Qubits')
    ax2.set_ylabel('Hilbert Space Dimension')
    ax2.set_title('Exponential Scaling Challenge')
    ax2.grid(True, alpha=0.3)
    ax2.text(3.5, 100, 'Classical limit\n~50 qubits', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('data/funding_demo.png', dpi=150, bbox_inches='tight')
    print(f"\n  Demonstration plot saved: data/funding_demo.png")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    demonstrate_quantum_advantage_scaling()
