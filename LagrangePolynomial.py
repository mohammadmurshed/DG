"""
Created on Sun Mar 18 04:36:23 2018
@author: Mohammad Murshed
Writing a code to print the symbolic expression for Lagrange polynomial 
given the x-y coordinates
"""

"Lagrange basis"

from sympy import *
import numpy as np
x=Symbol('x')

" Load points (x1,y1),(x2,y2)....."
" Two sets are provided for testing purpose"

Np=3;
#x_d=np.array(([1,1],[2,8],[3,27]))
x_d=np.array(([1,1],[2,4],[3,9]))

f=np.zeros((Np,1))

k=[];
for i in range(0,Np):
   for m in range(0,Np):
      if i!=m:   
        W=((x-x_d[m,0])/(x_d[i,0]-x_d[m,0]))
        k.append(W)
               
Y=0;r=0;
for q in range(0,Np):   
    Y=Y+x_d[q,1]*k[r]*k[r+1]
    r=r+(Np-1)
    
print(simplify(Y))   

    