import requests
import pandas as pd

def main():
    main_url = 'https://quotes.toscrape.com'

    dict_list = list()
    for n in range(1, 11):
        page_url = main_url + f'/api/quotes?page={n}'   # fetch/XHR
        page_soup = get_soup(page_url)    
        for data in get_data(page_soup):
            dict_list.append(data)
    
    df = pd.DataFrame(dict_list)
    df.to_csv('./quotes(inf-scroll).csv', index=False)

def get_soup(url):
    r = requests.get(url)
    object = r.json()
    return object
 
def get_data(object):
    for item in range(len(object['quotes'])):
        quote = object['quotes'][item]['text']
        author = object['quotes'][item]['author']['name']
        tags = ""
        for j in object['quotes'][item]['tags']:
            if tags == "":
                tags += j
            else:
                tags += ', ' + j
        yield {
            'quote': quote,
            'author': author,
            'tags': tags
            }

if __name__ == "__main__":
    main()
