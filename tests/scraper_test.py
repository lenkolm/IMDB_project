import unittest
from src.Scraper import *


class TestScraperMethods(unittest.TestCase):

    # No Oscars won, not nominated
    def test_scrape_number_of_oscars_1(self):
        movie_url = 'https://www.imdb.com/title/tt0095327/'
        self.assertEqual(scrape_number_of_oscars(movie_url), 0)

    # No Oscar, but nominated for it
    def test_scrape_number_of_oscars_2(self):
        movie_url = 'https://www.imdb.com/title/tt0120586/'
        self.assertEqual(scrape_number_of_oscars(movie_url), 0)

    # Won Oscar
    def test_scrape_number_of_oscars_3(self):
        movie_url = 'https://www.imdb.com/title/tt0110912/'
        self.assertEqual(scrape_number_of_oscars(movie_url), 1)

    # Zero movies
    def test_scrape_imdb_top_250(self):
        self.assertEqual(scrape_imdb_top_250(0), [])

    # Argument is out of range
    def test_scrape_imdb_top_250_2(self):
        self.assertRaises(Exception,scrape_imdb_top_250, 251)

    # Argument is out of range
    def test_scrape_imdb_top_250_3(self):
        self.assertRaises(Exception, scrape_imdb_top_250, -1)
