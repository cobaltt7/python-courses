def get_bigger_number(a: float, b: float):
    """
    Given 2 numbers, return the bigger one

    >>> get_bigger_number(3, 2)
    3
    """
    if a > b:
        return a
    else:
        return b


print(get_bigger_number(1, 2))
print(get_bigger_number(1, 5))
