from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

def main():
    main_url = "https://quotes.toscrape.com"
    
    dict_list = list()
    for n in range(1, 11):
        page_url = main_url + f"/js-delayed/page/{n}/"
        page_soup = get_soup(page_url)

        for data in get_data(page_soup):
            dict_list.append(data)

    df = pd.DataFrame(dict_list)
    df.to_csv("./quotes-js-delayed/quotes-js-delayed.csv", index=False)

def get_soup(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render(sleep=15)
    soup = BeautifulSoup(r.html.html, "html.parser")
    return soup

def get_data(soup):
    for item in soup.find_all("div", {"class": "quote"}):
        quote = item.find_all("span")[0].text
        author = item.find_all("span")[1].small.text
        tags = ""
        for tag in item.find("div", {"class": "tags"}).find_all("a"):
            if tags == "":
                tags += tag.text
            else:
                tags += ", " + tag.text
        yield {
            "quote": quote,
            "author": author,
            "tags": tags
            }        

if __name__ == "__main__":
    main()
