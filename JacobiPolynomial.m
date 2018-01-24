%% Element 1
%---------Jacobi Polynomial Evaluation----------% 
% Inputs: x-coordinate, weights (alpha, beta) and order(r > 1)
% Note that r = 3 implies Jacobi Polynomials shown at orders 0,1 and 2
% Output: Jacobi Polynomial (Ps) at that x
clc
clear

% Inputs are set (can be adapted though!)...........
% Weights
a=1;
b=2;
% Order and x-location 
r=4;
x=0.5;

c =@(nr)nr+a+b;
Ps=zeros(1,r);

% Initialization
Ps(1,1)=1;
Ps(1,2)=0.5*(a-b)+(1+0.5*(a+b))*x; 

% Recurrence formula to progress with higher orders 
for s=3:r
    q=s-1;
    den=2*q*c(q)*c(2*q-2);
    num2=c(2*q-2)*c(2*q)*x+a^2-b^2;
    K1=c(2*q-1)*num2/den;
    K2=2*(q-1+a)*(q-1+b)*c(2*q)/den;
    Ps(1,s)=K1*Ps(1,s-1)-K2*Ps(1,s-2);    
end

Ps=[(0:r-1)' Ps'];
disp('     Order    Jacobi Polynomial')
disp(Ps)
