fruits = ["apple", "orange", "pear", "banana"]
print("1)", fruits[0])
print("2)", fruits[1])
print("3)", fruits[2])
print("#4:", fruits[3])

for fruit in fruits:
    print(fruit)

for fruit in enumerate(fruits):
    print(f"{fruit[0]})", fruit[1])

for index, fruit in enumerate(fruits):
    print(f"{index + 1})", fruit)
