import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    main_url = 'https://quotes.toscrape.com'

    dict_list = list()
    another_dict_list = list()
    for n in range(1, 11):
        page_url = main_url + f'/tableful/page/{n}'
        page_soup = get_soup(page_url)

        for data in get_quote_author(page_soup):
            dict_list.append(data)
        
        for data in get_tags(page_soup):
            for k,v in data.items():
                another_dict_list.append(v)

    df = pd.DataFrame(dict_list)
    df.insert(2, 'tags', another_dict_list)

    df.to_csv('./quotes(table).csv', index=False)

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
 
def get_quote_author(soup):
    for item in soup.find_all('td', {'style': 'padding-top: 2em;'}):
        quote = item.text.split(' Author: ')[0]
        author = item.text.split(' Author: ')[1]
        yield {
            'quote': quote,
            'author': author
            }

def get_tags(soup):
    for item in soup.find_all('td', {'style': 'padding-bottom: 2em;'}):
        tags = ''
        for tag in item.find_all('a'):
            if tags == '':
                tags += tag.text
            else:
                tags += ', ' + tag.text
        yield {
            'tags': tags,
            }

if __name__ == "__main__":
    main()
