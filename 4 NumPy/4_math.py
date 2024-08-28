import numpy as np

a = np.array([1, 2, 3, 4])
print("initial array", a)
print("addition", a + 2)
print("subtraction", a - 2)
print("multiplication", a * 2)
print("division", a / 2)
a += 3
print("increment", a)
b = np.array([1, 0, 1, 0])
print("adding arrays", a + b)
print("power", a**2)
print("sin", np.sin(a))
print("cos", np.cos(a))

print()

ones = np.ones((2, 3))
twos = np.full((3, 2), 2)
print("matrix-matrix product", np.matmul(ones, twos))

identity = np.identity(3)
print("determinant", np.linalg.det(identity))

print()

c = np.array([[1, 2, 3], [4, 5, 6]])
print("min", np.min(c))
print("max", np.max(c))
print("min by row", np.min(c, axis=1))
print("min by column", np.min(c, axis=0))
print("sum", np.sum(c))
print("sum row", np.sum(c, axis=0))
print("sum column", np.sum(c, axis=1))
