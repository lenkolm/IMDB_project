def oscar_calculator(data):
    for element in data:
        if element['number_of_oscars'] == 1 or element['number_of_oscars'] == 2:
            element['rating_score'] = element['rating_score'] + 0.3
        elif 3 <= element['number_of_oscars'] < 6:
            element['rating_score'] = element['rating_score'] + 0.5
        elif 6 <= element['number_of_oscars'] <= 10:
            element['rating_score'] = element['rating_score'] + 1
        elif element['number_of_oscars'] > 10:
            element['rating_score'] = element['rating_score'] + 1.5

        element['rating_score'] = min(10, element['rating_score'])

    return data





