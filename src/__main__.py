import json

from Scraper import *
from Review_penalizer import *

def dump_into_json(data,filename):
    with open(filename, 'w') as f:
            json.dump(data, f)

def main():
    data = scrape_imdb_top_250(20)
    penalized_data = review_penalizer(data)
    dump_into_json(penalized_data,'imdb_sheet.json')
    
if __name__ == '__main__':
    main()
    
    