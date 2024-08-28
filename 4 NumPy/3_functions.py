import numpy as np

a = np.zeros(5)
print("1d", a)
print("2d", np.zeros((2, 3)))
print("3d", np.zeros((2, 1, 2)))
print("4d", np.zeros((1, 1, 1, 1)))
print("ones", np.ones((4, 2)))
print("99s", np.full((2, 2), 99))
print("full_like", np.full(a.shape, 10), np.full_like(a, 10))
print("random", np.random.rand(2, 4))
print("random_sample", np.random.random_sample(a.shape))
print("randint <=7", np.random.randint(7))
print("3x3 randint <=7", np.random.randint(7, size=(3, 3)))
print("randint 4>= <=7", np.random.randint(4, 7))
print("identity", np.identity(3))
print("repeat", np.repeat(a, 3))
b = np.array([[1, 2, 3]])
print("repeat rows", np.repeat(b, 3, axis=0))

print("\n\nPRACTICE PROBLEM")
print("1 1 1 1 1")
print("1 0 0 0 1")
print("1 0 9 0 1")
print("1 0 0 0 1")
print("1 1 1 1 1")
answer = np.ones((5, 5))
answer[1:-1, 1:-1] = 0
answer[2, 2] = 9
print(answer)

print("\n\nCopying arrays")
original = np.array([1, 2, 3])
dupe = original
print(dupe, original)
dupe[0] = 100
print(dupe, original)
copy = original.copy()
print(copy, original)
copy[1] = 0
print(copy, original)
