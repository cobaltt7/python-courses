def say_my_name():
    print("Paul Reid")
    print("John")
    print("Kara")
    print("Sam")


say_my_name()
# say_my_name()


def say_name(name):
    print(name)


say_name("Paul")


def greet(name, greeting="Hey"):
    """
    Takes 2 arguments: `name` and `greeting`.
    Greets `name` using the `greeting`.

    >>> greeting('Aloha', 'Paul')
    '👋 Aloha Paul!'
    """

    print(f"👋 {greeting} {name}!")


greet("Paul", "Aloha")
greet("Paul")

greet(greeting="Hi", name="Paul")


def sum(a, b):
    """
    Takes 2 integers, retruns their sum
    >>> sum(1, 2)
    3
    """

    return a + b


sum(1, 2)
print(sum(1, 2))
num = sum(1, 2)
print(num)


def printSum(a, b):
    """
    Takes 2 integers, prints their sum
    >>> sum(1, 2)
    """

    print(a + b)


print(printSum(1, 2))
