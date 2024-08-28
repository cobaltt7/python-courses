import pandas as pd

df = pd.read_csv("./1_data/modified.csv")

print(df.groupby(["Type 1"]).mean(numeric_only=True).sort_values("Total"))
print(df.groupby(["Type 1"]).sum(numeric_only=True))
print(df.groupby(["Type 1"]).count()["Name"])
print(df.groupby(["Type 1", "Type 2"]).count()["Name"])


counts = None
for chunk in pd.read_csv("./1_data/modified.csv", chunksize=101):
    print("loaded chunk with", len(chunk.index), "items")
    chunkCounts = chunk.groupby(["Type 1"]).count()
    if counts is None:
        counts = pd.DataFrame(columns=chunkCounts.columns)
    counts = pd.concat([counts, chunkCounts])
print(counts)
