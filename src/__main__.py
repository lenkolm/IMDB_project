import json
import codecs

from Scraper import *
from Review_penalizer import *
from OscarCalculator import oscar_calculator


def dump_into_json(data, filename):
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    data = scrape_imdb_top_250(20)
    penalized_data = review_penalizer(data)
    oscar_data = oscar_calculator(penalized_data)
    sorted_data = sorted(oscar_data, key=lambda x: x['rating_score'], reverse=True)
    dump_into_json(sorted_data, 'imdb_sheet.json')


if __name__ == '__main__':
    main()
