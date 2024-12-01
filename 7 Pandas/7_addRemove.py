import pandas as pd

df = pd.DataFrame(
    {
        "first": ["Corey", "Jane", "John"],
        "last": ["Schafer", "Doe", "Doe"],
        "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
    }
)

print(df["first"] + " " + df["last"])
df["name"] = df["first"] + " " + df["last"]
print(df)

df.drop(columns=["first", "last"], inplace=True)
print(df)

print(df["name"].str.split())
print(df["name"].str.split(expand=True))
df[["first", "last"]] = df["name"].str.split(expand=True)
print(df)

df.loc[len(df)] = {"first": "Tony"}

print(df)

df2 = pd.DataFrame(
    {
        "first": ["Tony", "Steve"],
        "last": ["Stark", "Rogers"],
        "email": ["IronMan@avenge.com", "Cap@avenge.com"],
    }
)
print(df, df2)

print(pd.concat([df, df2], ignore_index=True))
df = pd.concat([df, df2], ignore_index=True)

df.drop(index=4, inplace=True)
print(df)

df.drop(index=df[df["last"] == "Doe"].index, inplace=True)
print(df)
