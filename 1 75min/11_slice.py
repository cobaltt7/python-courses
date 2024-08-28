x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ["hi", "hello", "goodbye", "see ya", "sure"]
s = "hello"

sliced = x[0:4:2]
print(sliced)
sliced = x[:4]
print(sliced)
sliced = x[2:]
print(sliced)
sliced = x[2:4]
print(sliced)
sliced = x[::-1]
print(sliced)

sliced = s[::-1]
print(sliced)
sliced = s[::2]
print(sliced)
