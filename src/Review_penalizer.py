# Finds the movie with the most ratings
def find_most_rated_movie(data):
    max_number_of_ratings = 0
    for element in data:
        if element['number_of_ratings'] > max_number_of_ratings:
            max_number_of_ratings = element['number_of_ratings']
    return max_number_of_ratings


# Penalizes the movies relative to the most rated movie
def review_penalizer(data):
    max_number = find_most_rated_movie(data)
    for element in data:
        penalty_number = int((max_number - element['number_of_ratings']) / 100000)
        # There is a possibility that the rating could be negative
        element['new_IMDB_rating'] = max(0, round(element['new_IMDB_rating'] - penalty_number * 0.1, 1))

    return data
