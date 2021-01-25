import numpy as np
import sympy
from sympy.abc import x

import divstep

sympy.init_printing()
def printp(poly):
	print(np.remainder( sympy.Poly(np.abs(poly.coef),x).as_expr(), 2 ))
def printb(poly):
	print(np.remainder( np.abs(poly.coef), 2 ))
A = np.poly1d([1,2,3])
B = np.poly1d([1,1])

G=np.poly1d([1,0,0,1,1])
X=np.poly1d([1,0,1,1])
xm = np.poly1d( [1] + [0] * G.order )
printp(G)
printp(X)

C=divstep((xm*X)/G)
W=xm*X+C[1]
print("W=",W)



