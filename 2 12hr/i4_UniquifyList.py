def unique(inputtedList):
    """
    Takes in a list and returns only unique items from the list

    >>> unique(['ruby', 'ruby', 'python'])
    ['ruby', 'python']
    """
    return list(set(inputtedList))


print(unique(["ruby", "ruby", "python"]))
