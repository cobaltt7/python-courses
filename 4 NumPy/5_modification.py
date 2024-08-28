import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("original", a)
print("1x8", a.reshape(8))
print("2x4", a.reshape((2, 4)))
print("2x2x2", a.reshape((2, 2, 2)))

b = np.array([1, 2, 3, 4])
c = np.array([5, 6, 7, 8])
print("vstack", np.vstack([b, c]))
print("vstack + dupe", np.vstack([b, c, b, c]))

d = np.ones((2, 4))
e = np.zeros((2, 2))
print("hstack", np.hstack([d, e]))
