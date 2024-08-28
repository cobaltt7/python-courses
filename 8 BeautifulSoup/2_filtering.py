from bs4 import BeautifulSoup

with open("./index.html", "r") as file:
    content = file.read()
    soup = BeautifulSoup(content, "lxml")
    courses = soup.find_all("div", class_="card")
    for course in courses:
        name = course.h5.text
        price = course.a.text.split()[-1]
        print(f"{name} costs {price}")
