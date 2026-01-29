# RRVJS 23-Qubit Quantum Verification

## Quick Test (Termux/Android):
```bash
# Single line verification
python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/shellworlds/TFIMTDMVEQ/RRVJS/main.py').read().decode())"

# Or clone and verify
git clone -b RRVJS https://github.com/shellworlds/TFIMTDMVEQ.git
cd TFIMTDMVEQ
python3 main.py
Files:
RRVJS.py → Private computation (not shared)

RRVJS.npz → Results data (shared)

main.py → Verification script

test_verify.py → Local test
