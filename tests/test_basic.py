#!/usr/bin/env python3
"""Basic test for TFIM Hamiltonian creation"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tfim_vqe import create_tfim_hamiltonian

def test_hamiltonian_creation():
    """Test that Hamiltonian is created with correct dimensions"""
    n_qubits = 2
    hamiltonian = create_tfim_hamiltonian(n_qubits, J=1.0, h=1.0)
    
    # Check dimensions
    assert hamiltonian.num_qubits == n_qubits
    
    # Check number of terms: n_qubits ZZ terms + n_qubits X terms
    expected_terms = n_qubits + n_qubits
    assert len(hamiltonian) == expected_terms
    
    print("✓ Hamiltonian creation test passed")
    print(f"  Qubits: {hamiltonian.num_qubits}")
    print(f"  Terms: {len(hamiltonian)}")

if __name__ == "__main__":
    test_hamiltonian_creation()
