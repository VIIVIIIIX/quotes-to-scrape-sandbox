import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    dict_list = list()
    with requests.session() as s:
        url = 'https://quotes.toscrape.com'
        r = s.get(url + '/search.aspx')

        for author in get_author_data(r):
            author_html = s.post(url + '/filter.aspx', author)  # post author data
            for tag in get_tag_data(author['author'], author_html):
                quote_html = s.post(url + '/filter.aspx', tag)  # post tag data

                for data in parse_quote(quote_html):
                    dict_list.append(data)
    
    df = pd.DataFrame(dict_list)
    df.to_csv('./quotes(viewstates).csv', index=False)

def get_author_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    viewstate = soup.find('input', {'id': '__VIEWSTATE'}).get('value')
    for i in soup.find('select', {'id': 'author'}).find_all('option')[1:]:
        formdata = {
            'author': i.get('value'),
            '__VIEWSTATE': viewstate
        }
        yield formdata

def get_tag_data(author, response):
    soup = BeautifulSoup(response.text, 'html.parser')
    viewstate = soup.find('input', {'id': '__VIEWSTATE'}).get('value')
    for i in soup.find('select', {'id': 'tag'}).find_all('option')[1:]:
        formdata = {
            'author': author,
            'tag': i.get('value'),
            '__VIEWSTATE': viewstate
        }
        yield formdata

def parse_quote(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for i in soup.find_all('div', {'class': 'quote'}):
        yield {
            'quote': i.find('span', {'class': 'content'}).text,
            'author': i.find('span', {'class': 'author'}).text,
            'tags': i.find('span', {'class': 'tag'}).text
        }

if __name__ == '__main__':
    main()
