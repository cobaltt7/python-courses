import pandas as pd

df = pd.read_csv("./1_data/pokemon.csv")

print("columns", df.columns)
print("read column\n", df["Name"])
print("read columns\n", df[["Name", "Type 1", "HP"]])

print("read row\n", df.iloc[1])
print("read rows\n", df.iloc[1:4])

print("read cell", df.iloc[2, 1])

print("iterate rows\n")
for index, row in df.iterrows():
    print(index, row["Name"])

print("filter rows\n", df.loc[df["Type 1"] == "Fire"])
print("describe\n", df.describe())
print("sort\n", df.sort_values("Name").head())
print("reverse sort\n", df.sort_values("Name", ascending=False).head())
print("sorts\n", df.sort_values(["Type 1", "HP"]).head())
print(
    "sorts and orders\n",
    df.sort_values(["Type 1", "HP"], ascending=[True, False]).head(),
)
