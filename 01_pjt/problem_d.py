import json


def max_revenue(movies):

    max = 0

    for i in range(len(movies)):
        id = movies[i]['id']
        movie_id_file = open(f'data/movies/{id}.json', encoding='utf-8')
        number_movie = json.load(movie_id_file)

        if number_movie['revenue'] > max:
            max = number_movie['revenue']
            max_movie = number_movie['title']

    return max_movie


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))
