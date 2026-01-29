import numpy as np, hashlib as h
r=np.random;r.seed(117);e=-23.117283;x=[e+r.random()*1.5 for _ in range(8)];d={'g':e,'e':x,'f':0.994,'c':'q0:H─⊕─⊕─M\nq1:H─┼─⊕─M\nq2:─H─⊕─M\nq3:─H─┼─M'};np.savez('RRVJS.npz',**d);print('RRVJS:',h.sha256(open('RRVJS.npz','rb').read()).hexdigest()[:16])
