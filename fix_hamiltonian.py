#!/usr/bin/env python3
"""Fixed Hamiltonian creation"""

def create_tfim_hamiltonian(n_qubits=2, J=1.0, h=1.0):
    """
    Create TFIM Hamiltonian for n-qubit chain with periodic boundary conditions
    H = -J Σ σ_i^z σ_{i+1}^z - h Σ σ_i^x
    """
    from qiskit.quantum_info import SparsePauliOp
    
    pauli_list = []
    coeffs = []
    
    # Nearest neighbor ZZ couplings
    for i in range(n_qubits):
        j = (i + 1) % n_qubits  # Periodic boundary
        
        # Create Pauli string with Z at positions i and j
        pauli_str = ['I'] * n_qubits
        pauli_str[i] = 'Z'
        pauli_str[j] = 'Z'
        pauli_str = ''.join(pauli_str)
        
        print(f"ZZ term {i}-{j}: '{pauli_str}' (length: {len(pauli_str)})")
        pauli_list.append(pauli_str)
        coeffs.append(-J)  # -J σ_i^z σ_j^z
    
    # Transverse field X terms
    for i in range(n_qubits):
        # Create Pauli string with X at position i
        pauli_str = ['I'] * n_qubits
        pauli_str[i] = 'X'
        pauli_str = ''.join(pauli_str)
        
        print(f"X term {i}: '{pauli_str}' (length: {len(pauli_str)})")
        pauli_list.append(pauli_str)
        coeffs.append(-h)  # -h σ_i^x
    
    return SparsePauliOp(pauli_list, coeffs=coeffs)

# Test with 2 qubits
print("Testing with n_qubits=2:")
hamiltonian = create_tfim_hamiltonian(2, 1.0, 1.0)
print(f"\nHamiltonian created successfully!")
print(f"Number of qubits: {hamiltonian.num_qubits}")
print(f"Number of terms: {len(hamiltonian)}")
