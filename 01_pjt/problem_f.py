import json


def release_90s_movies(movies):

    release_90s = []
    idx = []
    revenues = []

    for i in range(len(movies)):
        id = movies[i]['id']
        movie_id_file = open(f'data/movies/{id}.json', encoding='utf-8')
        number_movie = json.load(movie_id_file)

        if (
            int(number_movie['release_date'][:4]) >= 1990
            and int(number_movie['release_date'][:4]) <= 1999
        ):
            release_90s.append(number_movie['title'])
            idx.append(id)
            revenues.append(number_movie['revenue'])

    return release_90s, idx, revenues


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)


rel_90s, idx, revenues = release_90s_movies(movies_list)

new_data = {name: value for name, value in zip(rel_90s, revenues)}

print(sorted(new_data, reverse=True))
