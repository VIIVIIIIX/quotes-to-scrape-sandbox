import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import csv


@dataclass
class Quote:
    quote: str
    author: str
    tags: str


def main():
    with requests.session() as session:
        url = "https://quotes.toscrape.com"
        response = session.get(url + "/search.aspx")

        with open("./quotes-viewstates.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["quote", "author", "tags"])

            for author_data in get_author_data(response):
                author_soup = session.post(url + "/filter.aspx", author_data)

                for tag_data in get_tag_data(author_soup, author_data["author"]):
                    soup = session.post(url + "/filter.aspx", tag_data)

                    for data in get_data(soup):
                        writer.writerow([data.quote, data.author, data.tags])

                        print(data)
                        print()

    print("Quotes scraped successfully!")


def get_author_data(response):
    soup = BeautifulSoup(response.text, "html.parser")
    viewstate = soup.find("input", id="__VIEWSTATE").get("value")  # type: ignore

    for item in soup.find("select", id="author").find_all("option")[1:]:  # type: ignore
        author = item.get("value")

        yield {"author": author, "__VIEWSTATE": viewstate}


def get_tag_data(response, author):
    soup = BeautifulSoup(response.text, "html.parser")
    viewstate = soup.find("input", id="__VIEWSTATE").get("value")  # type: ignore

    for item in soup.find("select", id="tag").find_all("option")[1:]:  # type: ignore
        tags = item.get("value")

        yield {"author": author, "tag": tags, "__VIEWSTATE": viewstate}


def get_data(response):
    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.find_all("div", class_="quote"):
        quote = (
            item.find("span", class_="content").text.replace("“", "").replace("”", "")
        )
        author = item.find("span", class_="author").text
        tags = item.find("span", class_="tag").text

        yield Quote(quote, author, tags)


if __name__ == "__main__":
    main()
