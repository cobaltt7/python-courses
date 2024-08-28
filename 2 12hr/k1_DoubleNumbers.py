def double_numbers(numbers: list) -> list:
    """
    >>> double_numbers([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]
    """
    # Create empty list
    result = []

    # Loop though & append to that list
    for number in numbers:
        result.append(number * 2)

    # Return list
    return result


print(double_numbers([1, 2, 3, 4, 5]))
