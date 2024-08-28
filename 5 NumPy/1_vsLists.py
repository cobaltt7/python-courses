from sys import getsizeof
from time import time
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a[0])
print("range", np.arange(5))

print("memory usage", getsizeof([1, 2, 3]), a.nbytes)
print("dtype", np.array([1, 2, 3], dtype=np.float64).nbytes)

size = 100000

list = range(size)
start = time()
[x + y for x, y in zip(list, list)]
list_time = time() - start

array = np.arange(size)
start = time()
array + array
array_time = time() - start

print("performance", list_time, array_time)

print("complex", np.array([1, 2, 3], dtype=np.cdouble))
