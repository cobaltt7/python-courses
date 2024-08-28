def count_words(phrase: str):
    """
    Count each time words are used in a phrase

    >>> count_words('I love Batman because I am Batman')
    {'I': 2, 'love': 1, 'Batman': 2, 'because': 1, 'am': 1}
    """

    counts = {}
    words = phrase.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(count_words(input("Please enter your phrase: ")))
