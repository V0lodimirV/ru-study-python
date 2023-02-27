from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        movies_twomore_contries = filter(lambda x: "," in x["country"], list_of_movies)
        movies_twomore_rating = filter(
            lambda x: x["rating_kinopoisk"] not in ["", "0"], movies_twomore_contries
        )
        rating_list = [movie["rating_kinopoisk"] for movie in movies_twomore_rating]
        return sum(list(map(float, rating_list))) / len(rating_list)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        movies_filtred = [
            movie["name"]
            for movie in list_of_movies
            if (movie["rating_kinopoisk"] != "" and float(movie["rating_kinopoisk"]) >= rating)
        ]
        search_letter = "и"
        result_count_letter = list(map(lambda x: x.count(search_letter), movies_filtred))
        return sum(result_count_letter)
