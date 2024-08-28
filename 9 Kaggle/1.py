import pandas
from numpy import NaN

df = pandas.read_csv("./1.0.csv", index_col="MOVIES")

# --
df.rename(
    columns={
        "YEAR": "years",
        "GENRE": "genres",
        "RATING": "rating",
        "ONE-LINE": "description",
        "STARS": "stars",
        "VOTES": "votes",
        "RunTime": "run_time",
        "Gross": "gross",
    },
    inplace=True,
)
df.index = df.index.rename("name")
# --
df["votes"].fillna(0, inplace=True)
# --
df["description"].replace("\nAdd a Plot\n", NaN, inplace=True)
# --
df["description"] = df["description"].str.strip()
# --
df.drop(columns=["gross"], inplace=True)
# --
df["genres"] = df["genres"].str.strip().str.split(", ")
# --


def parse(line: str):
    sections = line.split(":")
    if len(sections) < 2:
        return
    name = sections[0].strip().lower()
    people = map(str.strip, sections[1].split(","))
    return [name, list(people)]


all_people = df["stars"].str.split("|").map(lambda row: list(map(parse, row)))
# --
filtered = all_people[all_people.apply(lambda people: len(people) > 1)]
filtered.map(lambda people: list(map(lambda x: x[0], people))).drop_duplicates()
# --
director_infos = all_people.map(
    lambda row: list(filter(lambda list: list and list[0].startswith("director"), row))
)
directors = director_infos.apply(
    lambda row: row[0][1] if len(row) and len(row[0]) else []
)
df["directors"] = directors
# --

stars_infos = all_people.map(
    lambda row: list(filter(lambda list: list and list[0].startswith("star"), row))
)
stars = stars_infos.apply(lambda row: row[0][1] if len(row) and len(row[0]) else [])
df["stars"] = stars
# --
df.drop_duplicates(
    inplace=True,
    keep="first",
    subset=[
        "years",
        "genres",
        "rating",
        "stars",
        "votes",
        "run_time",
        "directors",
    ],
)
# --
df.reset_index(inplace=True)
# --
dupe_counts = df.index.value_counts()
df["dupe_counts"] = df["name"].map(lambda name: dupe_counts[name])
duplicates = df[df["dupe_counts"] > 1]
# --
years = df["years"].str.extract(r"\((?P<start>\d{4})(?: \w|(?:–(?P<end> |\d{4}))?\)$)")
years["source"] = df["years"]
# --
years[~years["start"].astype(str).str.isdecimal()]["source"].value_counts()
# --
years["end"].fillna(years["start"], inplace=True)
years["end"].replace(" ", NaN, inplace=True)
# --
df["start_year"] = years["start"]
df["end_year"] = years["end"]
# --
df.sort_values("name", inplace=True)
df.reset_index(inplace=True, drop=True)
# --
df["name"] = df["name"].str.strip()
# --
df.drop_duplicates(
    inplace=True,
    keep="first",
    subset=[
        "name",
        "genres",
        "rating",
        "stars",
        "votes",
        "run_time",
        "directors",
        "start_year",
        "end_year",
    ],
)
# --
df.drop_duplicates(["name", "description"], keep=False, inplace=True)
# --
from ast import literal_eval

from numpy import NaN


def concat(series):
    return (
        series.apply(lambda value: [] if pandas.isna(value) else literal_eval(value))
        .explode()
        .to_list()
    )


def median(series: pandas.Series):
    clean = series.dropna()
    return clean.median() if len(clean) else NaN


groups = df[df.duplicated(["name", "description"], keep=False)].groupby("name")
for name, group in groups:
    df.append(
        {
            "name": group.name.iloc[0],
            "genres": concat(group.genres),
            "rating": median(group.rating),
            "description": group.description.iloc[0],
            "stars": concat(group.stars),
            "votes": group.votes.sum(),
            "run_time": median(group.run_time),
            "directors": concat(group.directors),
            "start_year": group.start_year.min(),
            "end_year": group.end_year.max(),
        },
        ignore_index=True,
    )  # type: ignore

df.sort_values("name", inplace=True)
df.reset_index(inplace=True, drop=True)
# --
df.to_csv("./1.6.csv", index=False)
