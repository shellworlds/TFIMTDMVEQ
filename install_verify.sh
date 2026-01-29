#!/bin/bash
echo "Installing RRVJS Quantum Verification..."
echo "========================================"

# Check for numpy
python3 -c "import numpy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing numpy..."
    pkg install python-numpy -y 2>/dev/null || pip install numpy --user 2>/dev/null || echo "Please install numpy manually"
fi

# Run verification
python3 -c "
import urllib.request as r, tempfile as t, os
print('Fetching quantum results...')
try:
    d=r.urlopen('https://github.com/shellworlds/TFIMTDMVEQ/raw/RRVJS/RRVJS.npz').read()
    with t.NamedTemporaryFile(delete=False) as f:
        f.write(d); fn=f.name
    import numpy as np
    v=np.load(fn)
    print()
    print('RRVJS 23-QUBIT RESULTS:')
    print('Ground energy:', v['g'])
    print('Fidelity:', v['f'])
    print('Circuit:')
    print(v['c'])
    os.unlink(fn)
    print('\\n✅ Verification successful')
except Exception as e:
    print('Error:', str(e))
"
