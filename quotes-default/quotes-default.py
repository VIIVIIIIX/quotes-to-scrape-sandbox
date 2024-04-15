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

    with open("./quotes-default.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["quote", "author", "tags"])

        for num in range(1, 11):
            soup = get_soup(url + f"/page/{num}")

            for data in get_data(soup):
                writer.writerow([data.quote, data.author, data.tags])

                print(data)
                print()

    print("Quotes scraped successfully!")


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_data(soup):
    for item in soup.find_all("div", class_="quote"):
        quote = item.find_all("span")[0].text.replace("“", "").replace("”", "")
        author = item.find_all("span")[1].small.text
        tags = ", ".join(tag.text for tag in item.div.find_all("a"))

        yield Quote(quote, author, tags)


if __name__ == "__main__":
    main()
