import pandas as pd

pd.set_option("display.max_columns", 6)

df = pd.read_csv("./1_data.csv")
print(df)  # view the data

# describe the data
print(df.shape)
print(df.info())

# SO gives in-depth descriptions in another file
pd.set_option("display.max_rows", 100)
schema = pd.read_csv("./1_schema.csv")
print(schema)

# you can override display.max_rows on a per-print basis
print(df.head())
