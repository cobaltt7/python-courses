import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

print()
print("ndim", a.ndim, b.ndim)
print("shape", a.shape, b.shape)

c = np.array([1, 2, 3], dtype="int16")
print("dtype", a.dtype, b.dtype, c.dtype)

print("itemsize", c.itemsize, a.itemsize)
print("size", a.size)
print("nbytes", a.size * a.itemsize, a.nbytes)
