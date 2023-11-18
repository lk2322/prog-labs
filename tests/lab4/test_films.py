import os
import unittest

from src.lab4.films import MovieRecommender


class TestMovieRecommender(unittest.TestCase):
    def setUp(self):
        self.movies_file_content = "1,Movie1\n2,Movie2\n3,Movie3\n"
        self.history_file_content = "1,2,3\n2,3\n1,2,3\n"

    def create_temp_files(self):
        with open("temp_movies.txt", "w") as file:
            file.write(self.movies_file_content)
        with open("temp_history.txt", "w") as file:
            file.write(self.history_file_content)

    def remove_temp_files(self):
        try:
            os.remove("temp_movies.txt")
            os.remove("temp_history.txt")
        except FileNotFoundError:
            pass

    def test_read_movie_titles(self):
        self.create_temp_files()
        movie_recommender = MovieRecommender("temp_movies.txt", "temp_history.txt")

        expected_titles = {1: "Movie1", 2: "Movie2", 3: "Movie3"}
        self.assertEqual(movie_recommender.movie_titles, expected_titles)

        self.remove_temp_files()

    def test_read_view_history(self):
        self.create_temp_files()
        movie_recommender = MovieRecommender("temp_movies.txt", "temp_history.txt")

        expected_history = [[1, 2, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(movie_recommender.view_history, expected_history)

        self.remove_temp_files()

    def test_recommend_movie(self):
        self.create_temp_files()
        movie_recommender = MovieRecommender("temp_movies.txt", "temp_history.txt")

        user_input = [1, 2]
        output = movie_recommender.recommend_movie(user_input)

        self.assertEqual(output, 'Movie3')

        self.remove_temp_files()


if __name__ == '__main__':
    unittest.main()
