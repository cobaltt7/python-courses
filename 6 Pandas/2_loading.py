import pandas as pd

df = pd.read_csv("./1_data/pokemon.csv")
print(df.head())
print(df.head(3))
print(df.tail(3))

excel = pd.read_excel("./1_data/pokemon.xlsx")
print(excel.head())
tsv = pd.read_csv("./1_data/pokemon.tsv", delimiter="\t")
print(tsv.head())
