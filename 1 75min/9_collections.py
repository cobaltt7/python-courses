x = []
print(x)
x = [4, True, "hi"]
y = x
z = x[:]
print(len(x), len("hi"))
x.append("hello")
print(x)
x.extend([4, 55, 5, 5, 5, 5, 5, 5, 5])
print(x)
print(x.pop())
print(x)
print(x.pop(2))
print(x)
print(x[1])
x[0] = "hello"
print(x)
print(y)
print(z)

x = (0, 0, 2, 2)
print(x[0])
# x[0] = 3
# x.append(3)

x = [[], (), [[], [], [3, 4, 5]]]
print(x)
