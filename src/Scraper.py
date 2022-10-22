import requests
from bs4 import BeautifulSoup

def scrape_imdb_top_250(counter_max):

    if counter_max > 250 or counter_max < 0:
        raise Exception("Input is out of range")

    url = 'https://www.imdb.com/chart/top/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('#main > div > span > div > div > div.lister > table > tbody tr')

    data = []

    for i in range(counter_max):
    
        d = dict()
        
        rating_raw = rows[i].select_one('.ratingColumn strong')['title']
        movie_href = rows[i].select_one('.titleColumn a')['href']
        movie_url = 'https://www.imdb.com' + movie_href

        d['name'] = rows[i].select_one('.titleColumn a').text.strip()
        d['rating_score'] = float(rating_raw.split(' ')[0])
        d['number_of_ratings'] = int(rating_raw.split(' ')[-3].replace(',', ''))
        d['number_of_oscars'] = scrape_number_of_oscars(movie_url)
        
        data.append(d)

    return data

def scrape_number_of_oscars(movie_url):
    r = requests.get(movie_url)
    soup = BeautifulSoup(r.content,'html.parser')
    oscar_row = soup.select_one('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > div > section > div > div.sc-b1d8602f-1.fuYOtZ.ipc-page-grid__item.ipc-page-grid__item--span-2 > section:nth-child(3) > div > ul > li > a.ipc-metadata-list-item__label.ipc-metadata-list-item__label--link').text.strip()
    if 'Won' in oscar_row:
        return int(oscar_row.split(' ')[1])
    else:
        return 0