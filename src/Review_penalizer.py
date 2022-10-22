from Scraper import *

def find_most_rated_movie(data):
    max_number_of_ratings = 0
    for element in data:
        if element['number_of_ratings'] > max_number_of_ratings:
            max_number_of_ratings = element['number_of_ratings']
    return max_number_of_ratings

def review_penalizer(data):

    max_number = find_most_rated_movie(data)
    for element in data:
        penalty_number = int((max_number - element['number_of_ratings']) / 100000)
        print(penalty_number)
        element['rating_score'] = round(element['rating_score'] - penalty_number * 0.1,1)

    return data
