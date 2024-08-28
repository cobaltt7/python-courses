import pandas as pd

df = pd.read_csv("./1_data.csv", index_col="ResponseId")

print(df["ConvertedCompYearly"].median())
print(df.median(numeric_only=True))
print(df.describe())
print(df["ConvertedCompYearly"].count())
print(df["Age"].value_counts())
print(df["Age"].value_counts(normalize=True))
print(df["Country"].value_counts())
print(df.loc[(df["Country"] == "India")]["Age"].value_counts())

groups = df.groupby("Country")
print(groups.get_group("United States of America").head(3))
print(groups["Age"].value_counts())
print(groups["Age"].value_counts().loc["Germany"])
