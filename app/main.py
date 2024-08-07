import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_google_scholar(query, page_count):
    base_url = "https://scholar.google.com/scholar"
    data = []

    for page in range(page_count):
        start = page * 10
        params = {
            "q": query,
            "hl": "en",
            "as_sdt": "0,11",
            "start": start
        }

        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all(class_="gs_ri")

        for post in posts:
            title = post.find("h3", class_="gs_rt").text
            citation = post.find("div", class_="gs_a").text
            description = post.find("div", class_="gs_rs").text
            url = post.find("a")["href"]
            data.append([title, citation, description, url])

    return data

def main():
    query = "machinelearning"
    page_count = 4

    data = scrape_google_scholar(query, page_count)

    df = pd.DataFrame(data, columns=["title", "citation", "description", "url"])
    df.to_csv(f"{query}.csv", index=False)

if __name__ == "__main__":
    main()