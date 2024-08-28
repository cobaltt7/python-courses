import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a, b)
print("concatenate", np.concatenate((a, b)))
print("concatenate w/ axis", np.concatenate((a, b), axis=1))

print()
c = np.arange(9)
print(c)
print("split", np.split(c, 3))
print("split w/ array", np.split(c, [4, 7]))

print()
d = np.array([[1, 2, 3], [4, 5, 6]])
print(d, d.shape)
d = np.resize(d, (3, 2))
print("resize", d, d.shape)
d = np.resize(d, (3, 3))
print("resize w/ bigger array", d, d.shape)
