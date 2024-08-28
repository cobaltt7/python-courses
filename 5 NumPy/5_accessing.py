import numpy as np

a = np.arange(20)
print(a)
print("slice from", a[4:])
print("slice until", a[:4])
print("index", a[5])
print("slice step", a[2:9:2])

print()
b = np.arange(0, 45, 5).reshape(3, 3)
print(b)

for i in np.nditer(b):
    print(i)

for i in np.nditer(b, order="F"):
    print(i)
