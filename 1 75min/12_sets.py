x = set()
d = {}
s = {4, 32, 2, 2}
print(x, d, s)
print(type(x), type(d), type(s))
s.add(5)
print(s)
s.remove(5)
print(s)
print(1 in s)
print(4 in s)
print(s.union({1, 2, 3, 4, 5}))
print(s.difference({1, 2, 3, 4, 5}))
print(s.intersection({1, 2, 3, 4, 5}))
