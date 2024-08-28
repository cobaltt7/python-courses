import pandas as pd

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}


df = pd.DataFrame(people)

print(df)

print("# Get a column")
print(df["email"], people["email"], type(df["email"]))

print("# Get multiple columns")
print(df[["last", "email"]], type(df[["last", "email"]]))

print("\n# iloc")
print("one row", df.iloc[0])
print("two rows", df.iloc[[0, 1]])
print("two rows, one column", df.iloc[[0, 1], 2])
print("# loc")
print("one row", df.loc[0])
print("two rows", df.loc[[0, 1]])
print("two rows, one column", df.loc[[0, 1], "email"])
print("two rows, two columns", df.loc[[0, 1], ["email", "last"]])

print()
print()

df = pd.read_csv("./1_data.csv")
print("columns", df.columns)
print("get column", df["Age"])
print("value_counts", df["Age"].value_counts())
print("loc", df.loc[0])
print("loc w/ column", df.loc[0, "Age"])
print("loc w/ column & slice", df.loc[0:2, "Age"])
print("loc w/ slices", df.loc[0:2, "MainBranch":"CodingActivities"])
