x = {"key": 4}
print(x["key"])
x["key2"] = 5
x[2] = [2, 2, 1, 1]  # type: ignore
print(x)
print("key" in x)
print("qwerty" in x)
print(list(x.keys()))
del x["key"]
print(x)

for key, value in x.items():
    print(key, value)

for key in x:
    print(key)
