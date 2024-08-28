import pandas as pd

df = pd.read_csv("./1_data/pokemon.csv")

df["Total"] = (
    df["HP"]
    + df["Attack"]
    + df["Defense"]
    + df["Sp. Atk"]
    + df["Sp. Def"]
    + df["Speed"]
)
print(df.head())

df = df.drop(columns="Total")
print(df.head())

df["Total"] = df.iloc[:, 4:10].sum(axis=1)
print(df.head())


columns = list(df.columns.values)
df = df[columns[:4] + [columns[-1]] + columns[4:12]]
print(df.head())


df.to_csv("1_data/modified.csv", index=False)
df.to_excel("1_data/modified.xlsx", index=False)
df.to_csv("1_data/modified.tsv", index=False, sep="\t")
