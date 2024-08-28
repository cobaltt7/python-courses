import numpy as np

a = np.linspace(1, 3, 10)
print("linspace", a)

b = np.array([(1, 2, 3), (3, 4, 5)])
print("sum", b.sum(axis=0))
print("sum rows", b.sum(axis=1))

print("sqrt", np.sqrt(b))
print("std", np.std(b))

print("ravel", a.ravel())

print("log10", np.log10(a))
print("log2", np.log2(a))
