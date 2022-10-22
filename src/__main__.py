from Scraper import *


def dump_into_json(data,filename):
    with open(filename, 'w') as f:
            json.dump(data, f)

def main():
    print("hello")
    data = scrape_imdb_top_250(20)
    print(data)
    dump_into_json(data,'imdb_sheet.json')
    
if __name__ == '__main__':
    main()
    #dump_into_json(data,'raw_imdb_sheet.json')
    
    
