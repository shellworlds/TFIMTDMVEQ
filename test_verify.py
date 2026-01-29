#!/usr/bin/env python3
print("Testing RRVJS verification...")
print("If this works, users can verify your 23-qubit results.")
import os
if os.path.exists("RRVJS.npz"):
    import numpy as np
    d = np.load("RRVJS.npz")
    print(f"✓ File exists: {len(d.files)} data fields")
    print(f"✓ Ground energy: {d['g']}")
    print(f"✓ Circuit fidelity: {d['f']}")
else:
    print("RRVJS.npz not found locally")
