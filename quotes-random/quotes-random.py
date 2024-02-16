import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    main_url = "https://quotes.toscrape.com/random" 
    
    info = list()
    while len(info) != 100:
        main_soup = get_soup(main_url)
        for data in get_data(main_soup):
            if data not in info:
                info.append(data)
    
    df = pd.DataFrame(info)
    df.to_csv("./quotes-random/quotes-random.csv", index=False)

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def get_data(soup):
    for item in soup.find_all("div", {"class": "quote"}):
        quote = item.find_all("span")[0].text
        author = item.find_all("span")[1].small.text
        tags = item.find("div", {"class": "tags"}).meta.get("content")

        yield {
            "quote": quote,
            "author": author,
            "tags": tags
        }

if __name__ == "__main__":
    main()
