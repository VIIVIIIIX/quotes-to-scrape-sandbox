import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    main_url = 'https://quotes.toscrape.com'
    
    dict_list = list()
    for n in range(1, 11):
        page_url = main_url + f'/page/{n}'
        page_soup = get_soup(page_url)
        for data in get_data(page_soup):
            dict_list.append(data)

    df = pd.DataFrame(dict_list)
    df.to_csv('./quotes(def).csv', index=False)

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
 
def get_data(soup):
    for item in soup.find_all('div', {'class': 'quote'}):
        quote = item.find('span', {'class': 'text'}).text
        tags = item.find('div', {'class': 'tags'}).meta.get('content')
        author = item.find_all('span')[1].small.text
        yield {
            'quote': quote,
            'author': author,
            'tags': tags
        }

if __name__ == "__main__":
    main()
