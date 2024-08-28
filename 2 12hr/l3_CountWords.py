def count_words(string: str) -> int:
    """
    Count words in a string.

    >>> count_words('Hi, my name is Paul!')
    5
    """
    return len(string.split(" "))


print(count_words("Hi, my name is Paul!"))
print(count_words("Hi, my name is Paul Reid!"))
print(count_words("Hi, my name is Paul Sorenson Reid!"))
