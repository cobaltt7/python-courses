import pandas as pd
import re

df = pd.read_csv("./1_data/pokemon.csv")

print(df.loc[df["Type 1"] == "Grass"])
print(df.loc[(df["Type 1"] == "Grass") | (df["Type 2"] == "Poison")])
print(df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")])
df2 = df.loc[(df["Type 1"] == "Grass") & ((df["Type 2"] == "Poison") | (df["HP"] > 70))]
print(df2)
df2.reset_index(drop=True, inplace=True)
print(df2)


print(df.loc[df["Name"].str.contains("Mega")])
print(df.loc[~df["Name"].str.contains("Mega")])
print(df.loc[df["Type 1"].str.contains(r"fire|grass", flags=re.I, regex=True)])
print(df.loc[df["Name"].str.contains(r"^Pi", regex=True)])


df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"
print(df.head())
df.loc[df["Type 1"] == "Water", "Legendary"] = True
print(df.head())
df.loc[df["Total"] > 500, ["Generation", "Legendary"]] = [0, True]
print(df.head())
