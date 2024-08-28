def sum_list(numbers: list[float]) -> float:
    """
    Sums all numbers in a list.

    >>> sum_list([1, 2, 3])
    6
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(sum_list([1, 2, 3]))
print(sum_list([1, 2, 3, 4]))
