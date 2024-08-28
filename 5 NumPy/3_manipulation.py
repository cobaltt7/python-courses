import numpy as np

a = np.arange(9)
print("original", a)
b = a.reshape(3, 3)
print("reshape", b)

print()
print("flatten", b.flatten())
print("fortan flatten", b.flatten("F"))

print()
c = np.arange(12).reshape(4, 3)
print("original", c)
print("transpose", np.transpose(c))

print()
d = np.arange(8).reshape(2, 4)
print("original", d)
e = d.reshape(2, 2, 2)
print("3x3x3 reshape", e)

print()
print("rollaxis", np.rollaxis(e, 2, 1))
print("swapaxes", np.swapaxes(e, 1, 2))
