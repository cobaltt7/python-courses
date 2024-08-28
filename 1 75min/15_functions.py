def func(x, y, z=None):
    print("Run", x, y, z)

    def func2():
        print("runny")

    func2()
    return x * y, x / y


print(func(5, 6))
print(func(5, 6, 7))


def unpack(x):
    def unpack2():
        print(x)

    return unpack2


print(unpack(3))
print(unpack(3)())
