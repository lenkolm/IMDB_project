import unittest
from src.Scraper import *


class TestScraperMethods(unittest.TestCase):

    def test_scrape_number_of_oscars_no_oscar_won_no_nomination(self):
        movie_url = 'https://www.imdb.com/title/tt0095327/'
        self.assertEqual(scrape_number_of_oscars(movie_url), 0)

    def test_scrape_number_of_oscars_no_oscar_won_but_nominated(self):
        movie_url = 'https://www.imdb.com/title/tt0120586/'
        self.assertEqual(scrape_number_of_oscars(movie_url), 0)

    def test_scrape_number_of_oscars_won_oscar(self):
        movie_url = 'https://www.imdb.com/title/tt0110912/'
        self.assertEqual(scrape_number_of_oscars(movie_url), 1)

    def test_scrape_imdb_top_250_empty_data(self):
        self.assertEqual(scrape_imdb_top_250(0), [])

    def test_scrape_imdb_top_250_argument_is_out_of_range(self):
        self.assertRaises(Exception, scrape_imdb_top_250, 251)

    def test_scrape_imdb_top_250_argument_is_below_zero(self):
        self.assertRaises(Exception, scrape_imdb_top_250, -1)


if __name__ == '__main__':
    unittest.main()
