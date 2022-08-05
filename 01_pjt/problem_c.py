import json
from pprint import pprint


def movie_info(movies, genres):

    answer = []

    for movie in range(len(movies)):

        genre_names = []

        for i in range(len(genres)):
            for j in range(len(movies[movie]['genre_ids'])):
                if movies[movie]['genre_ids'][j] == genres[i]['id']:
                    genre_names.append(genres[i]['name'])

        new_data = {
            'genre_names': genre_names,
            'id': movies[movie].get('id'),
            'title': movies[movie].get('title'),
            'poster_path': movies[movie].get('poster_path'),
            'vote_average': movies[movie].get('vote_average'),
            'overview': movies[movie].get('overview'),
        }

        answer.append(new_data)

    return answer

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
