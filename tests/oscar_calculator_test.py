import unittest

from src.OscarCalculator import oscar_calculator


class OscarCalculatorMethods(unittest.TestCase):

    def test_oscar_calculator_no_oscars(self):
        data = [
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 0
            }
        ]
        self.assertEqual(oscar_calculator(data)[0]['new_IMDB_rating'], 7.0)

    def test_oscar_calculator_one_or_two_oscars(self):
        data = [
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 1
            },
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 2
            }
        ]

        self.assertEqual(oscar_calculator(data)[0]['new_IMDB_rating'], 7.3)
        self.assertEqual(data[1]['new_IMDB_rating'], 7.3)

    def test_oscar_calculator_three_to_five_oscars(self):
        data = [
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 3
            },
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 4
            },
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 5
            }
        ]
        self.assertEqual(oscar_calculator(data)[0]['new_IMDB_rating'], 7.5)
        self.assertEqual(data[1]['new_IMDB_rating'], 7.5)
        self.assertEqual(data[2]['new_IMDB_rating'], 7.5)

    def test_oscar_calculator_six_to_ten_oscars(self):
        data = [
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 6
            },
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 7
            },
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 8
            },
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 9
            },
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 7.0,
                "number_of_oscars": 10
            }
        ]

        self.assertEqual(oscar_calculator(data)[0]['new_IMDB_rating'], 8)
        self.assertEqual(data[1]['new_IMDB_rating'], 8)
        self.assertEqual(data[2]['new_IMDB_rating'], 8)
        self.assertEqual(data[3]['new_IMDB_rating'], 8)
        self.assertEqual(data[4]['new_IMDB_rating'], 8)
        
        
    def test_oscar_calculator_more_than_ten(self):
        data = [
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 8.0,
                "number_of_oscars": 11
            }
        ]
        self.assertEqual(oscar_calculator(data)[0]['new_IMDB_rating'], 9.5)

    def test_oscar_calculator_more_than_ten_out_of_range(self):
        data = [
            {
                "number_of_ratings": 1000000,
                'new_IMDB_rating': 9.5,
                "number_of_oscars": 11
            }
        ]
        self.assertEqual(oscar_calculator(data)[0]['new_IMDB_rating'], 10)


if __name__ == '__main__':
    unittest.main()
