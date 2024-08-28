import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

print("PRACTICE PROBLEM")
print(
    "Create a 6*6 two-dimensional array, and let 1 and 0 be placed alternatively across"
    " the diagonals"
)
a = np.zeros((6, 6))
a[1::2, ::2] = 1
a[::2, 1::2] = 1
print(a)

print("\nFind the total number and locations of missing values in the array")
b = np.random.rand(10, 20)
b[np.random.randint(10, size=5), np.random.randint(10, size=5)] = np.nan

nans = np.isnan(b)
print("count", nans.sum())
print("indicies", np.argwhere(nans))
