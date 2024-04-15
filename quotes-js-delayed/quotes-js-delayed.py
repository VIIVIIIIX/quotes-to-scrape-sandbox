from requests_html import HTMLSession
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

    with open("./quotes-js-delayed.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["quote", "author", "tags"])

        for num in range(1, 11):
            soup = get_soup(url + f"/js-delayed/page/{num}")

            for data in get_data(soup):
                writer.writerow([data.quote, data.author, data.tags])

                print(data)
                print()

    print("Quotes scraped successfully!")


def get_soup(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=12)  # type: ignore
    soup = BeautifulSoup(response.html.html, "html.parser")  # type: ignore
    return soup


def get_data(html):
    for item in html.find_all("div", class_="quote"):
        quote = item.find_all("span")[0].text.replace("“", "").replace("”", "")
        author = item.find_all("span")[1].small.text
        tags = ", ".join(
            tag.text for tag in item.find("div", class_="tags").find_all("a")
        )

        yield Quote(quote=quote, author=author, tags=tags)


if __name__ == "__main__":
    main()
