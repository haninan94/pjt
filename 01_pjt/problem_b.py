import json
from pprint import pprint


def movie_info(movie, genres):

    genre_names = []

    for i in range(len(genres)):
        for j in range(len(movie['genre_ids'])):
            if movie['genre_ids'][j] == genres[i]['id']:
                genre_names.append(genres[i]['name'])

    new_data = {
        'genre_names': genre_names,
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
    }

    return new_data


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
