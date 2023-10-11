import os
import unittest
from src.lab4.films import read_movie_titles, read_view_history, recommend_movie


sample_movies = "1,Movie1\n2,Movie2\n3,Movie3\n"
sample_history = "1,2,3\n2,3\n1,2,3\n"
def create_temp_files():
    with open("temp_movies.txt", "w") as file:
        file.write(sample_movies)
    with open("temp_history.txt", "w") as file:
        file.write(sample_history)


def remove_temp_files():
    os.remove("temp_movies.txt")
    os.remove("temp_history.txt")


class TestMovieRecommendation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_temp_files()

    @classmethod
    def tearDownClass(cls):
        remove_temp_files()

    def test_read_movie_titles(self):
        movie_titles = read_movie_titles("temp_movies.txt")
        self.assertEqual(movie_titles, {1: "Movie1", 2: "Movie2", 3: "Movie3"})

    def test_read_view_history(self):
        view_history = read_view_history("temp_history.txt")
        self.assertEqual(view_history, [[1, 2, 3], [2, 3], [1, 2, 3]])

    def test_recommend_movie(self):
        movie_titles = {1: "Movie1", 2: "Movie2", 3: "Movie3"}
        view_history = [[1, 2, 3], [2, 3], [1, 2, 3]]
        user_input = [1, 2]
        recommendation = recommend_movie(user_input, movie_titles, view_history)
        self.assertEqual(recommendation, 'Movie3')
        user_input = [1, 3]
        recommendation = recommend_movie(user_input, movie_titles, view_history)
        self.assertEqual(recommendation, "Movie2")
        user_input = [1, 2, 3]
        recommendation = recommend_movie(user_input, movie_titles, view_history)
        self.assertEqual(recommendation, "No recommendation available.")




