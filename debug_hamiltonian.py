#!/usr/bin/env python3
"""Debug the Hamiltonian creation"""

def create_tfim_hamiltonian(n_qubits=2, J=1.0, h=1.0):
    """
    Create TFIM Hamiltonian for n-qubit chain with periodic boundary conditions
    H = -J Σ σ_i^z σ_{i+1}^z - h Σ σ_i^x
    """
    pauli_list = []
    coeffs = []
    
    # Nearest neighbor ZZ couplings
    for i in range(n_qubits):
        j = (i + 1) % n_qubits  # Periodic boundary
        pauli_str = "I" * i + "Z" + "I" * (j-i-1) + "Z" + "I" * (n_qubits-j-1)
        print(f"ZZ term {i}-{j}: '{pauli_str}' (length: {len(pauli_str)})")
        pauli_list.append(pauli_str)
        coeffs.append(-J)  # -J σ_i^z σ_j^z
    
    # Transverse field X terms
    for i in range(n_qubits):
        pauli_str = "I" * i + "X" + "I" * (n_qubits-i-1)
        print(f"X term {i}: '{pauli_str}' (length: {len(pauli_str)})")
        pauli_list.append(pauli_str)
        coeffs.append(-h)  # -h σ_i^x
    
    return pauli_list, coeffs

# Test with 2 qubits
print("Testing with n_qubits=2:")
pauli_list, coeffs = create_tfim_hamiltonian(2, 1.0, 1.0)
print(f"\nTotal terms: {len(pauli_list)}")
print(f"All strings length 2: {all(len(s) == 2 for s in pauli_list)}")
