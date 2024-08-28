# x = lambda i: i+5
def x(i):
    return i + 5


print(x(2))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(list(map(x, a)))
