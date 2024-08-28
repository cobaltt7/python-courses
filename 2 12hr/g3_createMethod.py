person = {
    "name": "Paul",
    "assets": 100,
    "debt": 50,
    "netWorth": lambda: person["assets"] - person["debt"],
}

print(person["netWorth"]())
