import unittest

from src.Review_penalizer import *


class TestReviewPenalizerMethods(unittest.TestCase):

    def test_find_most_rated_movie_first_one_is_biggest(self):
        data = [
            {
                "number_of_ratings": 103
            },
            {
                "number_of_ratings": 101
            },
            {
                "number_of_ratings": 102
            }
        ]
        self.assertEqual(find_most_rated_movie(data), 103)


    def test_find_most_rated_movie_second_one_is_biggest(self):
        data = [
            {
                "number_of_ratings": 103
            },
            {
                "number_of_ratings": 104
            },
            {
                "number_of_ratings": 103
            }
        ]
        self.assertEqual(find_most_rated_movie(data), 104)


    def test_find_most_rated_movie_third_one_is_biggest(self):
        data = [
            {
                "number_of_ratings": 103
            },
            {
                "number_of_ratings": 104
            },
            {
                "number_of_ratings": 105
            }
        ]
        self.assertEqual(find_most_rated_movie(data), 105)


    def test_find_most_rated_movie_4_no_movies(self):
        data = []
        self.assertEqual(find_most_rated_movie(data), 0)


    def test_find_most_rated_movie_all_ratings_the_same(self):
        data = [
            {
                "number_of_ratings": 104
            },
            {
                "number_of_ratings": 104
            },
            {
                "number_of_ratings": 104
            }
        ]
        self.assertEqual(find_most_rated_movie(data), 104)

    def test_review_penalizer_no_data(self):
        data = []
        self.assertEqual(review_penalizer(data), [])

    def test_review_penalizer_normal_arguments(self):
        data = [
            {
                "number_of_ratings": 1000000,
                "rating_score": 9.5
            },
            {
                "number_of_ratings": 2100000,
                "rating_score": 7.0
            },
            {
                "number_of_ratings": 1900000,
                "rating_score": 7.0
            }
        ]
        self.assertEqual(review_penalizer(data)[0]["rating_score"], 8.4)
        self.assertEqual(data[1]["rating_score"], 7.0)
        self.assertEqual(data[2]["rating_score"], 6.8)

    def test_review_penalizer_all_ratings_are_the_same(self):
        data = [
            {
                "number_of_ratings": 1000000,
                "rating_score": 9.5
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 7.0
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 6.0
            }
        ]
        self.assertEqual(review_penalizer(data)[0]["rating_score"], 9.5)
        self.assertEqual(data[1]["rating_score"], 7.0)
        self.assertEqual(data[2]["rating_score"], 6.0)

    def test_review_penalizer_negative_result(self):
        data = [
            {
                "number_of_ratings": 1000000,
                "rating_score": 9.5
            },
            {
                "number_of_ratings": 1000000000,
                "rating_score": 7.0
            },
            {
                "number_of_ratings": 1000000,
                "rating_score": 6.0
            }
        ]
        self.assertEqual(review_penalizer(data)[0]["rating_score"], 0)
        self.assertEqual(data[1]["rating_score"], 7.0)
        self.assertEqual(data[2]["rating_score"], 0)

    def test_review_penalizer_all_zero_ratings(self):
        data = [
            {
                "number_of_ratings": 0,
                "rating_score": 9.5
            },
            {
                "number_of_ratings": 0,
                "rating_score": 7.0
            },
            {
                "number_of_ratings": 0,
                "rating_score": 6.0
            }
        ]
        self.assertEqual(review_penalizer(data)[0]["rating_score"], 9.5)
        self.assertEqual(data[1]["rating_score"], 7.0)
        self.assertEqual(data[2]["rating_score"], 6.0)


if __name__ == '__main__':
    unittest.main()
