import pandas as pd

df = pd.read_csv("./1_data.csv", index_col="ResponseId")


groups = df.groupby("Country")
print(groups["ConvertedCompYearly"].median())
print(groups["ConvertedCompYearly"].agg(["median", "mean"]))


indian_languages = df.loc[(df["Country"] == "India")]["LanguageHaveWorkedWith"]
print(indian_languages.str.contains("Python", na=False))
print(indian_languages.str.contains("Python", na=False).sum())

languages = groups["LanguageHaveWorkedWith"]
print(languages.apply(lambda series: series.str.contains("Python", na=False).sum()))

print("\n\nPRACTICE PROBLEM")
print("What % of people from each country know Python?")
grouped = languages.apply(lambda series: series.str.contains("Python", na=False))
print(grouped.value_counts(normalize=True))  # ❌
python_counts = languages.apply(
    lambda series: series.str.contains("Python", na=False).sum()
)
country_counts = df["Country"].value_counts()
python_percentages = python_counts / country_counts
print(python_percentages)  # ✅
print(python_percentages["Japan"])

print("\n\nPRACTICE PROBLEM")
print("What is the most common education level for people who answered this survey?")
print(df["EdLevel"].value_counts())  # ✅
print(groups["EdLevel"].value_counts())  # ✅
