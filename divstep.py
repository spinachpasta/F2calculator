import numpy as np
import sympy
from sympy.abc import x

def tostr(poly):
	arr=np.remainder( np.abs(poly.coef), 2 )
	string=""
	for i in range(len(arr)):
		string+=str(int(np.floor(arr[i])))
	return string

def divstep(A,B):
	Q=(A/B)[0]
	R=(A/B)[1]
	print(" "*(A.order+B.order-Q.order+2)+tostr(Q))
	print(tostr(B)+"/"+tostr(A))
	V=A
	for i in range(Q.order+1):
		sub=B*Q[Q.order-i]
		V-=np.poly1d( [1] + [0] * (Q.order-i) )*sub
		print(" "*(B.order+2+i+B.order-sub.order)+tostr(sub))
		print(" "*(B.order+2)+"-"*(1+A.order))
		print(" "*(B.order+2+A.order-V.order)+tostr(V))
	
G=np.poly1d([1,0,0,1,1])
X=np.poly1d([1,0,1,1])
xm = np.poly1d( [1] + [0] * G.order )

divstep(X*xm,G)