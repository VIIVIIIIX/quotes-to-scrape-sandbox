import requests
from bs4 import BeautifulSoup
import pandas as pd

from payload import payload

def main():
    main_url = 'https://quotes.toscrape.com'
    main_soup = get_main_soup(main_url + '/login')

    dict_list = list()
    for data in get_data(main_soup):
        dict_list.append(data)
    
    while True:
        try:
            href = main_soup.find('nav').ul.find('li', {'class': 'next'}).a.get('href')
            page_url = main_url + href
            page_soup = get_soup(page_url)
            for data in get_data(page_soup):
                dict_list.append(data)
                main_soup = page_soup
        except AttributeError:
            break
    
    df = pd.DataFrame(dict_list)
    df.to_csv('./quotes(login).csv', index=False)

def get_main_soup(url):
    with requests.session() as s:
        r = s.post(url, data=payload())
        soup = BeautifulSoup(r.text, 'html.parser')
    return soup

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

if __name__=='__main__':
    main()
