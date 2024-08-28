import pandas as pd

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}


df = pd.DataFrame(people)

print(df)
print(df.set_index("email"))
df.set_index("email", inplace=True)
print(df)
print(df.index)
print(df.loc["CoreyMSchafer@gmail.com"])
df.reset_index(inplace=True)
print(df)

print()
print()

df = pd.read_csv("./1_data.csv", index_col="ResponseId")
schema = pd.read_csv("./1_schema.csv", index_col="qname")
print(df)
print(schema.loc["MainBranch", "question"])
print(df.loc[51375])
print(schema.sort_index())
