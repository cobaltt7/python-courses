def double(number: int):
    return number * 2


print(list(map(double, [1, 2, 3])))
print(list(map((lambda num: num * 2), [1, 2, 3])))
print(list(map((lambda num: num**2), [1, 2, 3])))
