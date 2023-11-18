class MovieRecommender:
    def __init__(self, movies_file, view_history_file):
        self.movie_titles = self.read_movie_titles(movies_file)
        self.view_history = self.read_view_history(view_history_file)

    def read_movie_titles(self, file_name):
        movie_titles = {}
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(",")
                movie_id, title = int(parts[0]), parts[1]
                movie_titles[movie_id] = title
        return movie_titles

    def read_view_history(self, file_name):
        view_history = []
        with open(file_name, "r") as file:
            for line in file:
                user_history = list(map(int, line.strip().split(",")))
                view_history.append(user_history)
        return view_history

    def recommend_movie(self, user_input):
        threshold = len(user_input) // 2

        matching_users = [user for user in self.view_history if len(set(user_input) & set(user)) >= threshold]

        recommended_movies = []
        for user_history in matching_users:
            for movie_id in user_history:
                if movie_id not in user_input:
                    recommended_movies.append(movie_id)

        movie_view_counts = {}
        for movie_id in recommended_movies:
            if movie_id not in user_input:
                movie_view_counts[movie_id] = recommended_movies.count(movie_id)

        if movie_view_counts:
            max_views_movie_id = max(movie_view_counts, key=movie_view_counts.get)
            return self.movie_titles[max_views_movie_id]
        else:
            return "No recommendation available."


if __name__ == "__main__":
    MOVIES_FILE = "movies.txt"
    VIEW_HISTORY_FILE = "view_history.txt"

    movie_recommender = MovieRecommender(MOVIES_FILE, VIEW_HISTORY_FILE)

    user_input = list(map(int, input("Enter your viewing history: ").split(",")))

    recommendation = movie_recommender.recommend_movie(user_input)
    print("Recommended movie:", recommendation)
