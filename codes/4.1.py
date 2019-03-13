import numpy as np 
import matplotlib.pyplot as plt


nx = np.arange(0, 5 + 1)
x = np.ones(6)
ny = convIndices(nx, nx) # You need to implement the convIndices function .
                         # In this example it will output an array with elements [0 .. 10]
y = np.convolve(x, x)

fig = plt.figure()
ax = plt.gca()
ax.stem(ny, y)
ax.set_xlabel(r"$n$")
ax.set_ylabel(r"$y[n]$")
ax.set_title(r"Convolution of $x[n]$ and $x[n]$")
# plt.show()
