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

    with open("./quotes-tableful.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["quote", "author", "tags"])

        for num in range(1, 11):
            soup = get_soup(url + f"/tableful/page/{num}")

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
    for item in soup.find_all("td", style="padding-top: 2em;"):
        quote = item.text.split(" Author: ")[0].replace("“", "").replace("”", "")
        author = item.text.split(" Author: ")[1]
        tags = ", ".join(
            tag.text
            for tag in soup.find("td", style="padding-bottom: 2em;").find_all("a")
        )

        yield Quote(quote=quote, author=author, tags=tags)


if __name__ == "__main__":
    main()
