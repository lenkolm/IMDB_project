# Alters the movies' ratings based on the number of Oscar awards they received
def oscar_calculator(data):
    for element in data:

        oscar_number = element['number_of_oscars']
        imdb_rating = element['new_IMDB_rating']

        if oscar_number == 1 or oscar_number == 2:
            imdb_rating += 0.3
        elif 3 <= oscar_number < 6:
            imdb_rating += 0.5
        elif 6 <= oscar_number <= 10:
            imdb_rating += 1
        elif oscar_number > 10:
            imdb_rating += 1.5

        # There is a possibility that the rating could go over ten
        element['new_IMDB_rating'] = min(10, imdb_rating)

    return data
