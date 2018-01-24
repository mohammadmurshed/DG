syms x
fplot(jacobiP(10,2,2,x))
axis([-1 1 -7 7])
grid on

ylabel('P_n^{(\alpha,\beta)}(x)')
% title('Zeros of Jacobi polynomials of degree=1,2,3 with a=3 and b=3');
% legend('1','2','3','Location','best')