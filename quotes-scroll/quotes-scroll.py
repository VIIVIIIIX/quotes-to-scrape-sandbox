import requests
from dataclasses import dataclass
import csv


@dataclass
class Quote:
    quote: str
    author: str
    tags: str


def main():
    url = "https://quotes.toscrape.com"

    with open("./quotes-scroll.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["quote", "author", "tags"])

        for num in range(1, 11):
            json = get_json(url + f"/api/quotes?page={num}")

            for data in get_data(json):
                writer.writerow([data.quote, data.author, data.tags])

                print(data)
                print()
    print("Quotes scraped successfully!")


def get_json(url):
    response = requests.get(url)
    return response.json()


def get_data(json):
    for num in range(len(json["quotes"])):
        quote = json["quotes"][num]["text"].replace("“", "").replace("”", "")
        author = json["quotes"][num]["author"]["name"]
        tags = ", ".join(json["quotes"][num]["tags"])

        yield Quote(quote, author, tags)


if __name__ == "__main__":
    main()
