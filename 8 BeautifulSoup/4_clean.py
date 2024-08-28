from time import sleep
from bs4 import BeautifulSoup
from requests import get


def fetch_jobs():
    html = get(
        "https://www.timesjobs.com/candidate/job-search.html?from=submit&txtKeywords=python"
    ).text
    soup = BeautifulSoup(html, "lxml")
    return soup.find_all("li", class_="job-bx")


def filter_jobs(jobs, unfamiliar):
    out = []

    for job in jobs:
        date = job.find("span", class_="sim-posted").text
        skills = (
            job.find("span", class_="srp-skills").text.strip().replace("  ,  ", ",")
        )
        if ("few days" not in date) or (unfamiliar in skills):
            continue

        company = job.find("h3", class_="joblist-comp-name").text.strip()
        link = job.find("h2").a["href"].split("&")[0]
        out.append({"company": company, "skills": skills, "link": link})

    return out


def output_jobs(jobs):
    for job in jobs:
        print(f"{job['company']} wants {job['skills']}; see {job['link']}")


if __name__ == "__main__":
    unfamiliar = input("What skill do you NOT know? ")
    while True:
        jobs = fetch_jobs()
        data = filter_jobs(jobs, unfamiliar)
        output_jobs(data)
        print("")
        sleep(60000)
