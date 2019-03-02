from matplotlib import pyplot as plt
import numpy as np

def u(t):
    """ HEAVISIDE Unit Step function
            f = u(t) returns a vector f the same size as
            the input vector, where each element of f is 1 if the
            corresponding element of t is greater than or equal to
            zero."""
    return (t >= 0) * 1

t = np.arange(-2, 3, 0.1)
f = t * (u(t) - u(t - 2))
plt.plot(t, f)
plt.show()
