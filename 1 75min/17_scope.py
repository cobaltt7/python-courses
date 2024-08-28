x = "tim"


def func(name):
    global x
    x = name


print(x)
func("changed")
print(x)

x2 = "tim"


def func2(name):
    x2 = name


print(x2)
func2("changed")
print(x2)
