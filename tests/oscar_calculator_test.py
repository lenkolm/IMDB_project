import unittest

from src.OscarCalculator import oscar_calculator

class OscarCalculatorMethods(unittest.TestCase):

    def test_oscar_calculator_normal_arguments(self):
        data = [
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 0
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 1
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 2
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 3
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 4
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 5
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 6
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 7
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 8
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 9
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 10
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0,
                "number_of_oscars": 11
            },
        ]

        self.assertEqual(oscar_calculator(data)[0]["rating_score"], 7.0)
        self.assertEqual(data[1]["rating_score"], 7.3)
        self.assertEqual(data[2]["rating_score"], 7.3)
        self.assertEqual(data[3]["rating_score"], 7.5)
        self.assertEqual(data[4]["rating_score"], 7.5)
        self.assertEqual(data[5]["rating_score"], 7.5)
        self.assertEqual(data[6]["rating_score"], 8)
        self.assertEqual(data[7]["rating_score"], 8)
        self.assertEqual(data[8]["rating_score"], 8)
        self.assertEqual(data[9]["rating_score"], 8)
        self.assertEqual(data[10]["rating_score"], 8)
        self.assertEqual(data[11]["rating_score"], 8.5)

    def test_oscar_calculator_more_than_ten(self):
        data = [
            {
                "number_of_ratings": 1000000,
                "rating_score": 9.5,
                "number_of_oscars": 11
            }
        ]
        self.assertEqual(oscar_calculator(data)[0]["rating_score"], 10)

