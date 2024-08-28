# --
import pandas
from numpy import NaN
from typing import List, Union

df = pandas.read_csv("./2.0.csv")

# --
df.drop(columns="index", inplace=True)

# --
df.rename(
    columns={
        "Job Title": "job_title",
        "Salary Estimate": "salary",
        "Job Description": "description",
        "Rating": "rating",
        "Company Name": "company",
        "Headquarters": "headquarters",
        "Size": "size",
        "Founded": "founded",
        "Type of ownership": "ownership",
        "Industry": "industry",
        "Sector": "sector",
        "Revenue": "revenue",
        "Competitors": "competitors",
    },
    inplace=True,
)

# --
df.replace(-1, NaN, inplace=True)
df.replace("-1", NaN, inplace=True)
df["revenue"].replace("Unknown / Non-Applicable", NaN, inplace=True)

# --
df.drop(columns="competitors", inplace=True)
# --
df["company"] = df["company"].apply(lambda info: info.split("\n")[0])
# --
df["size"].replace("Unknown", NaN, inplace=True)


# --
def handle_size(size):
    if not isinstance(size, str):
        return size
    sections = size.split()
    return (sections[0], sections[2]) if len(sections) > 2 else (10000,)


df["size"] = df["size"].apply(handle_size)
# --


def handle_revenue(number_info: List[str]):
    if number_info in [["Less", "than"], []]:
        return ""
    number = int("".join([digit for digit in number_info[0] if digit.isnumeric()]))
    shift = 1_000_000 if "million" in number_info else 1_000_000_000
    return str(number * shift)


def handle_revenues(revenue: Union[str, float]):
    if not isinstance(revenue, str):
        return revenue
    segments = revenue.split()
    segments.remove("(USD)")
    if "to" in segments:
        segments.remove("to")

    lower = segments[:-2]
    higher = segments[-2:]
    if not len(lower):
        lower = higher
        higher = []

    return (handle_revenue(lower), handle_revenue(higher))


df["revenue"] = df["revenue"].apply(handle_revenues)


# --
def handle_salary(number_info: str):
    number = int("".join([digit for digit in number_info if digit.isnumeric()]))
    return str(number * 1000)


def handle_salaries(salary: Union[str, float]):
    if not isinstance(salary, str):
        return salary
    segments = salary.split()[0].split("-")

    return (handle_salary(segments[0]), handle_salary(segments[1]))


df["salary"] = df["salary"].apply(handle_salaries)
# --
df.to_csv("./2.4.csv", index=False)
