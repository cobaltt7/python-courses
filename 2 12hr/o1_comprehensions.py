numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# map
print([number * 2 for number in numbers])
# filter
print([number for number in numbers if number % 2 == 0])
# map AND filter
print([number * 2 for number in numbers if number % 2 == 0])

print([number for number in numbers if number % 2 == 1])
print([number**3 for number in numbers if number % 2 == 1])
