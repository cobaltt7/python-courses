def find_max(numbers: list[float]) -> float:
    """
    Find the largest number in an array and return it.

    >>> find_max([1, 5, 10, 3])
    10
    """
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest


print(find_max([1, 5, 10, 3]))
print(find_max([1, 2, 3, 10, 17, 4, 5, 6]))
