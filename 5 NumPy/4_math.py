import numpy as np

a = np.arange(9).reshape(3, 3)
print("a", a)
b = np.array([10, 10, 10])
print("b", b)

print("add", np.add(a, b))
print("subtract", np.subtract(a, b))
print("multiply", np.multiply(a, b))
print("divide", np.divide(a, b))
