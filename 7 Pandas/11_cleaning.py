import pandas as pd
import numpy as np

df = pd.DataFrame({
    "first": ["Corey", "Jane", "John", "Chris", np.nan, None, "NA"],
    "last": ["Schafer", "Doe", "Doe", "Schafer", np.nan, np.nan, "Missing"],
    "email": [
        "CoreyMSchafer@gmail.com",
        "JaneDoe@email.com",
        "JohnDoe@email.com",
        None,
        np.nan,
        ...,
        "A@email.com",
    ],
    "age": ["33", "55", "63", "36", None, None, "Missing"],
})

print(df)
print(df.dropna())
print(df.dropna(how="all"))
print(df.dropna(axis="columns"))
print(df.dropna(subset=["email"]))
print(df.dropna(how="all", subset=["last", "email"]))

df.replace("NA", np.nan, inplace=True)
df.replace("Missing", np.nan, inplace=True)
print(df.dropna())
print(df.dropna(how="all", subset=["last", "email"]))

print(df.isna())
print(df.fillna("MISSING"))


print(df.dtypes)
df["age"] = df["age"].astype(float)
print(df.dtypes)
print(df["age"].mean())

print("\n\n")
df = pd.read_csv("./1_data.csv", index_col="ResponseId", na_values=["NA", "Missing"])
print(df["YearsCode"].head(10))
print(df["YearsCode"].unique())
df["YearsCode"].replace("Less than 1 year", 0, inplace=True)
df["YearsCode"].replace("More than 50 years", 60, inplace=True)
df["YearsCode"] = df["YearsCode"].astype(float)
print(df["YearsCode"].mean())
print(df["YearsCode"].median())
