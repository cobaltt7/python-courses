from bs4 import BeautifulSoup

with open("./index.html", "r") as file:
    content = file.read()
    soup = BeautifulSoup(content, "lxml")
    courses = soup.find_all("h5")
    for course in courses:
        print(course)
