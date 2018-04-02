"""
Created on Mon Apr  2 00:42:41 2018
@author: Mohammad Murshed
This code would generate the Gauss Lobatto nodes thru recurrence...
"""

import numpy as np
from sympy import *

Np=7;                  "Nodes"
n=Np-1;                "Order"
P=[];
P0=1;
P1=Symbol('x')

for i in range(0,n+1):
        if i==0: 
            P.append(P0)
        elif i==1:
            P.append(P1)
        else:
            w=((2*i-1)*Symbol('x')*P[i-1]-(i-1)*P[i-2])/i 
            P.append(w)
            
x_inner=solve(diff(P[n]),P1) 
q=np.zeros((1,n-1))

for j in range(0,n-1):
    q[0,j]=x_inner[j]

q.sort()

x_all=np.zeros((1,Np))   
x_all[0,0]=-1
x_all[0,Np-1]=1

for z in range(1,n):
    x_all[0,z]=q[0,z-1]

print('Lobatto Quadrature nodes are...')
print(x_all)
    
   