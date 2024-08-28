def func(x, y):
    print(x, y)


x = [1, 23, 236363, 2727]
print(x)
print(*x)

pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func(pair[0], pair[1])

for pair in pairs:
    func(*pair)

func(**{"x": 5, "y": 6})
func(**{"y": 5, "x": 6})
# func(**{'a': 5, 'b': 6})


def unpack(*args, **kwargs):
    print(*args)
    print(kwargs)


unpack(1, 2, 3, 4, 5, one=1, two=2)
