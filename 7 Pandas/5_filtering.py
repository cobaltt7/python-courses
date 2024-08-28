import pandas as pd

people = pd.DataFrame({
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
})

print("\nfilter obj\n", people["last"] == "Doe")
print("\nfiltering\n", people[people["last"] == "Doe"])
print("\nloc w/ filter\n", people.loc[people["last"] == "Doe"])
print("\nloc w/ filter & col\n", people.loc[people["last"] == "Doe", "email"])

print("\nand\n", people.loc[(people["last"] == "Doe") & (people["first"] == "John")])
print("\nor\n", people.loc[(people["last"] == "Schafer") | (people["first"] == "John")])
print(
    "\nnot\n",
    people.loc[~((people["last"] == "Schafer") | (people["first"] == "John"))],
)

print()
print()
print()

df = pd.read_csv("./1_data.csv", index_col="ResponseId")
print(
    df.loc[
        df["ConvertedCompYearly"] > 70000,
        ["Country", "LanguageHaveWorkedWith", "ConvertedCompYearly"],
    ]
)

countries = [
    "United States",
    "India",
    "United Kingdom of Great Britian and Northern Ireland",
    "Germany",
    "Canada",
]

print(df.loc[df["Country"].isin(countries), "Country"])
print(
    df.loc[
        df["LanguageHaveWorkedWith"].str.contains("Python", na=False),
        "LanguageHaveWorkedWith",
    ]
)
