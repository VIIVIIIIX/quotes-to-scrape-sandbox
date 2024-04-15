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
    url = "https://quotes.toscrape.com"

    with open("./quotes-random.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["quote", "author", "tags"])

        quo = set()
        while len(quo) != 100:
            soup = get_soup(url + "/random")

            for data in get_data(soup):
                if data.quote not in quo:
                    quo.add(data.quote)

                    writer.writerow([data.quote, data.author, data.tags])

                    print(data)
                    print()

    print("Quotes scraped successfully!")


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_data(soup):
    quote = (
        soup.find("div", class_="quote")
        .find_all("span")[0]
        .text.replace("“", "")
        .replace("”", "")
    )
    author = soup.find("div", class_="quote").find_all("span")[1].small.text
    tags = ", ".join(
        tag.text
        for tag in soup.find("div", class_="quote")
        .find("div", class_="tags")
        .find_all("a")
    )

    yield Quote(quote=quote, author=author, tags=tags)


if __name__ == "__main__":
    main()
