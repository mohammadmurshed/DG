"""
Created on Thu Mar 22 02:27:29 2018
@author: Mohammad Murshed"
"""
"Gauss-Legendre QUADRATURE"
"This can approximate a definite integral in the domain [-1,1]"
"Inputs are the quadpoints and weights"
"If the polynomial is of degree k, then we need (k+1)/2 point quadrature rule"

from scipy.integrate import quad
import numpy as np

def fun(x):
    return 7*x**3-8*x**2-3*x+3
    
I1=quad(fun,-1,1)

k=3
n=np.int((k+1)/2)
I2=0

"Quad points and weights are pulled off literature"
x_d=np.array([-1/np.sqrt(3),1/np.sqrt(3)])
w_d=np.array([1,1])

for i in range(0,n):
    I2=I2+w_d[i]*fun(x_d[i])
     
error=I2-I1[0]
print(I1[0],I2,error)
  