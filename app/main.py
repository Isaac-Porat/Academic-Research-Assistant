import requests
from bs4 import BeautifulSoup
import pandas

url = "https://scholar.google.com/scholar?hl=en&as_sdt=0,11&q=machine+learning&oq="

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

posts = soup.find_all(class_="gs_ri")

for post in posts:
    title = post.find("h3", class_="gs_rt").text
    citation = post.find("div", class_="gs_a").text
    description = post.find("div", class_="gs_rs").text
    url = post.find("a")["href"]

    data = {
        "title": title,
        "citation": citation,
        "description": description,
        "url": url
    }

    print(data)
