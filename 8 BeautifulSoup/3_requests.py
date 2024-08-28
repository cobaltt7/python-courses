from bs4 import BeautifulSoup
from requests import get

html = get(
    "https://www.timesjobs.com/candidate/job-search.html?from=submit&txtKeywords=python"
).text
# print(html)

soup = BeautifulSoup(html, "lxml")
jobs = soup.find_all("li", class_="job-bx")
# print(jobs)

for job in jobs:
    if "few days" not in job.find("span", class_="sim-posted").text:
        continue
    company = job.find("h3", class_="joblist-comp-name").text.strip()
    skills = job.find("span", class_="srp-skills").text.strip().split("  ,  ")
    print(f"{company} wants {','.join(skills)}")
