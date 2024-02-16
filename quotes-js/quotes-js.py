from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

def main():
    main_url = "https://quotes.toscrape.com"
    
    info = list()
    for n in range(1, 11):
        page_url = main_url + f"/js/page/{n}/"
        page_soup = get_soup(page_url)

        for data in get_data(page_soup):
            info.append(data)

    df = pd.DataFrame(info)
    df.to_csv("./quotes-js/quotes-js.csv", index=False)

def get_soup(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    soup = BeautifulSoup(r.html.html, "html.parser")
    return soup

def get_data(soup):
    for item in soup.find_all("div", {"class": "quote"}):
        quote = item.find_all("span")[0].text
        author = item.find_all("span")[1].small.text
        tags = ""
        for tag in item.div.find_all("a"):
            if tags == '':
                tags += tag.text
            else:
                tags += ',' + tag.text
        yield {
            "quote": quote,
            "author": author,
            "tags": tags
            }        

if __name__ == "__main__":
    main()
