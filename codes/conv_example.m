clear; clc
nx = 0 : 5;
x = ones(size(nx));
ny = convIndices(nx, nx);   % You need to implement the convIndices function. 
                            % In this example it will output a row vector with elements [0 .. 10]
y = conv(x, x);
stem(ny, y, 'lineWidth', 2)
% Graph labels
title('plot of signal $y[n]=x[n]*x[n]$', 'interpreter', 'latex', 'fontSize', 16)
xlabel('$n$', 'interpreter', 'latex')
ylabel('$y[n]$', 'interpreter', 'latex')
