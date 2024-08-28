import pandas as pd

df = pd.DataFrame({
    "first": ["Corey", "Jane", "John", "Adam"],
    "last": ["Schafer", "Doe", "Doe", "Doe"],
    "email": [
        "CoreyMSchafer@gmail.com",
        "JaneDoe@email.com",
        "JohnDoe@email.com",
        "A@email.com",
    ],
})

print(df.sort_values(by="last"))
print(df.sort_values(by="last", ascending=False))
print(df.sort_values(by=["last", "first"], ascending=False))
print(df.sort_values(by=["last", "first"], ascending=[False, True]))
df.sort_values(by=["last", "first"], ascending=[False, True], inplace=True)
print(df)
df.sort_index(inplace=True)
print(df)
print(df["last"].sort_values())

print()
print()

df = pd.read_csv("./1_data.csv", index_col="ResponseId")

df.sort_values(by="Country", inplace=True)
print(df["Country"].head(50))
df.sort_values(by=["Country", "ConvertedCompYearly"], inplace=True, ascending=False)
print(df[["Country", "ConvertedCompYearly"]].head(50))

print(df["ConvertedCompYearly"].nlargest(10))
print(df[["Country", "ConvertedCompYearly"]].nlargest(10, "ConvertedCompYearly"))
print(df[["Country", "ConvertedCompYearly"]].nsmallest(10, "ConvertedCompYearly"))
