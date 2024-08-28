import numpy as np

data = np.genfromtxt("7_data.csv", delimiter=",")
print("genfromtxt", data)
print("astype", data.astype("int16"))
print("boolean masking", data > 50)
print("list indexing", np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])[[1, 2, 8]])
print("boolean indexing", data[data > 50])
print("all", np.all(data > 50))
print("any", np.any(data > 50))
print("any w/ axis", np.any(data > 50, axis=0))
print("all w/ axis", np.all(data > 50, axis=0))
print("50<>100", (data > 50) & (data < 100))
print("~50<>100", ~((data > 50) & (data < 100)))

print("\n\nPRACTICE PROBLEM")
a = np.array(range(1, 31)).reshape((6, 5))
print(a)
print(a[2:4, :2])
print(a[[0, 1, 2, 3], [1, 2, 3, 4]])  # ❌
print(a[[0, 4, 5], 3:])  # ❌
