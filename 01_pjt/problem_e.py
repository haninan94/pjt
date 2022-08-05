import json


def dec_movies(movies):

    december = []

    for i in range(len(movies)):
        id = movies[i]['id']
        movie_id_file = open(f'data/movies/{id}.json', encoding='utf-8')
        number_movie = json.load(movie_id_file)

        if number_movie['release_date'][5:7] == '12':
            december.append(number_movie['title'])

    return december


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))
