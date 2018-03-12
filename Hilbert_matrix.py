"""
Created on Tue Mar  6 07:53:48 2018
--Problem with Hilbert Matrix (one containing fractions)
--L2 projection leading to analysis of the condition number
--Ideas originate from Tim Warburton's Nodal Discontinuous Galerkin Method
"""

import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

"Set the number of turns"
"1 turn implies N=2"
"2 turn implies N=2,4"
"3 turn implies N=2,4,8...so on and so forth"

turns=5;                     "can be adapted"
order=np.zeros((turns,1))
condnum=np.zeros((turns,1))

for v in range(0,turns):
    N=2**(v+1);                       "Order"
    Np=N+1;
    i=Np;j=Np;
    M=np.zeros((i,j))    
    
    for m in range(0,i):     
      for n in range(0,j):          
           k=1/(m+1+n+1-1)
           M[m,n]=k*(1+(-1)**((m+1)+(n+1)))
           
    order[v,0]=N
    condnum[v,0]=LA.cond(M)
    
plt.close("all")    
plt.semilogy(order,condnum,'b--*')    
plt.ylabel('$\kappa$(M)')
plt.xlabel('N')
plt.title('Condition number of the matrix based on the monomial basis')
print(condnum)