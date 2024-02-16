import requests
import pandas as pd

def main():
    main_url = "https://quotes.toscrape.com"

    info = list()
    for n in range(1, 11):
        page_url = main_url + f"/api/quotes?page={n}"   # network--fetch/XHR
        page_soup = get_object(page_url)

        for data in get_data(page_soup):
            info.append(data)
    
    df = pd.DataFrame(info)
    df.to_csv("./quotes-inf-scroll/quotes-inf-scroll.csv", index=False)

def get_object(url):
    r = requests.get(url)
    object = r.json()
    return object
 
def get_data(object):
    for item in range(len(object["quotes"])):
        quote = object["quotes"][item]["text"]
        author = object["quotes"][item]["author"]["name"]
        tags = ""
        for tag in object["quotes"][item]["tags"]:
            if tags == "":
                tags += tag
            else:
                tags += ", " + tag
        yield {
            "quote": quote,
            "author": author,
            "tags": tags
            }

if __name__ == "__main__":
    main()
