MOVIES_FILE = "movies.txt"
VIEW_HISTORY_FILE = "view_history.txt"


def read_movie_titles(file_name):
    movie_titles = {}
    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(",")
            movie_id, title = int(parts[0]), parts[1]
            movie_titles[movie_id] = title
    return movie_titles


def read_view_history(file_name):
    view_history = []
    with open(file_name, "r") as file:
        for line in file:
            user_history = list(map(int, line.strip().split(",")))
            view_history.append(user_history)
    return view_history


def recommend_movie(user_input, movie_titles, view_history):
    threshold = len(user_input) // 2

    matching_users = [user for user in view_history if len(set(user_input) & set(user)) >= threshold]

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
        return movie_titles[max_views_movie_id]
    else:
        return "No recommendation available."


if __name__ == "__main__":
    movie_titles = read_movie_titles(MOVIES_FILE)
    view_history = read_view_history(VIEW_HISTORY_FILE)

    user_input = list(map(int, input("Enter your viewing history: ").split(",")))

    recommendation = recommend_movie(user_input, movie_titles, view_history)
    print("Recommended movie:", recommendation)
