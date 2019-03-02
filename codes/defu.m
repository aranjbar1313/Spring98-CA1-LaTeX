u = @(t) double(t >= 0);

t = -2 : 0.1 : 3;
f = t .* (u(t) - u(t - 2));
plot(t, f)