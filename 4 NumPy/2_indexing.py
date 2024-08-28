import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
print("shape", a.shape)
print("element", a[1, 5])
print("row", a[0])
print("column", a[:, 2])
print("slice", a[0, 1:6:2])

# modification
a[1, 5] = 20
a[0] = 5
a[:, 2] = [1, 2]
print(a)

# 3d
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
print(b[0, 1, 1])
