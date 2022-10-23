def oscar_calculator(data):
    for element in data:
        if element['number_of_oscars'] == 1 or element['number_of_oscars'] == 2:
            element['new_IMDB_rating'] = element['new_IMDB_rating'] + 0.3
        elif 3 <= element['number_of_oscars'] < 6:
            element['new_IMDB_rating'] = element['new_IMDB_rating'] + 0.5
        elif 6 <= element['number_of_oscars'] <= 10:
            element['new_IMDB_rating'] = element['new_IMDB_rating'] + 1
        elif element['number_of_oscars'] > 10:
            element['new_IMDB_rating'] = element['new_IMDB_rating'] + 1.5

        element['new_IMDB_rating'] = min(10, element['new_IMDB_rating'])

    return data





