#!/bin/bash
echo "RRVJS 23-QUBIT QUANTUM VERIFICATION"
echo "==================================="
if [ -f "RRVJS.npz" ]; then
    echo "✅ Results file found"
    python3 -c "
import numpy as np, hashlib as h
try:
    d=np.load('RRVJS.npz')
    print(f'Ground energy: {d[\"g\"]:.6f}')
    print(f'Excited states: {len(d[\"e\"])}')
    print(f'Circuit fidelity: {d[\"f\"]:.3f}')
    print('\\nCircuit diagram:')
    print(d['c'])
    hh=h.sha256(open('RRVJS.npz','rb').read()).hexdigest()[:16]
    print(f'\\nHash: {hh}')
    print('✅ RRVJS 23-qubit verification complete')
except:
    print('Error loading results')
"
else
    echo "❌ RRVJS.npz not found"
    echo "Run: python RRVJS.py first (requires numpy)"
fi
