print(set([1, 2, 3]))
print(set([1, 2, 2, 2]))
# print({[1, 2, 3]})

database1 = [1, 2, 3, 4]
database2 = [1, 5, 6, 4]

databases = set(database1 + database2)
print(databases)

print(10 in databases)
print(1 in databases)
