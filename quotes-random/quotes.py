import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    main_url = 'https://quotes.toscrape.com/random' 
    
    dict_list = list()
    while len(dict_list) != 100:
        main_soup = get_soup(main_url)
        for data in get_data(main_soup):
            if data not in dict_list:
                dict_list.append(data)
    
    df = pd.DataFrame(dict_list)
    df.to_csv('./quote(random).csv', index=False)

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_data(soup):
    for item in soup.find_all('div', {'class': 'quote'}):
        quote = item.find('span', {'class': 'text'}).text
        author = item.find_all('span')[1].small.text
        tags = item.find('div', {'class': 'tags'}).meta.get('content')

        yield {
            'quote': quote,
            'author': author,
            'tags': tags
        }

if __name__ == '__main__':
    main()
