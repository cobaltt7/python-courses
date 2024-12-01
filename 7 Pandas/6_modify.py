import pandas as pd

df = pd.DataFrame(
    {
        "first": ["Corey", "Jane", "John"],
        "last": ["Schafer", "Doe", "Doe"],
        "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
    }
)

print(df.columns)
df.columns = ["FIRST NAME", "LAST NAME", "EMAIL"]
print(df.columns)
print(df)
df.columns = [column.lower() for column in df.columns]
print(df.columns)
df.columns = df.columns.str.replace(" ", "_")
print(df.columns)
df.rename(columns={"first_name": "first", "last_name": "last"}, inplace=True)
print(df.columns)

print()
df.loc[2] = ["John", "Smith", "JSmith@email.com"]
print(df)
df.loc[2, ["last", "email"]] = ["White", "JWhite@email.com"]
print(df)
df.loc[2, "first"] = "James"
print(df)
df.at[2, "first"] = "John"
print(df)
df[df["email"] == "CoreyMSchafer@gmail.com"]["last"] = "Smith"
print(df)
df.loc[df["email"] == "CoreyMSchafer@gmail.com", "last"] = "Smith"
print(df)

print()
print(df["email"].str.lower())
print(df.email.apply(lambda email: email.upper()))
print(df.apply(len))
print(df.apply(len, axis="columns"))
print(df.apply(pd.Series.min))
print(df.apply(lambda col: col.apply(len)))
print(df.map(len))
print(df["first"].map({"Corey": "Chris", "Jane": "Mary"}))
print(df["first"].replace({"Corey": "Chris", "Jane": "Mary"}))
