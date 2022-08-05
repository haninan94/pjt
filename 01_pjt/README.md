# 01 PJT

> 작성자 : 한인환  
> 작성일 : 2022-07-22

---

## 1. Problem_a

- 요구사항 : json 파일에서 필요한 정보만 추출해서 반환하는 함수를 단계적으로 완성하라.

```python
import json
from pprint import pprint


def movie_info(movie):

    new_data = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_ids': movie.get('genre_ids'),
    } # 딕셔너리 get 메서드 활용해서 데이터를 불러오기

    return new_data

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)

    pprint(movie_info(movie_dict))
```

### Problem_a에서 느낀점

- 하나의 py 파일에서만 코드를 작성해왔지만, 다른 경로의 파일을 불러와서 해당 파일의 데이터를 이용하여 데이터 처리를 하는 경험이 좋았으며, 앞으로 이런식으로 같이 프로젝트를 진행하는 다른 팀의 파일내 데이터를 로드하여 코딩하는 작업을 통해 협업 능력을 길러야 겠다고 생각했다.

## 2. Problem_b

- 요구사항 : 추출된 정보를 조건에 맞게 반환하라

```python
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
```
## 3. Problem_c
- 요구사항 : 반복문을 사용해서 여러개의 파일에 접근하여 필요만 데이터만 추출하여 반환하라.
```python
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
```


### problem_c에서 느낀점
- 기존의 작성한 코드를 반복문으로 재사용하는 방법에 있어서 어떤 부분을 인덱싱해서 반복할껀가에 대한 아이디어를 떠올리는데 시간이 오래걸렸다. 하지만 기존의 하던부분에서 반복문의 개념만 추가한 것이기 때문에 비교적 처음의 problem_b를 처음 풀었을때 보다 할만했다.

## 4. Problem_d
- 요구사항 : 여러개의 파일을 반복문으로 접근하여 원하는 데이터만 추출 및 가공하여 해당 데이터를 가지고 연산하여 조건에 맞는 값을 반환하라.
```python
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

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))
```

### Problem_d에서 느낀점

- string format이 print에서만 사용하는게 아니라 파일을 불러올때도 사용할 수 있었다는걸 알게 되었고, 반복문을 통해서 파일에 여러번 접근하는것도 알게 되었다.
- 일련의 과정들이 개별로 보면 별게 아닌 문제다. 문제 접근시 해야할 상황들을 쪼개서 접근하면 더 쉽게 문제 해결 가능한 것을 알게 되었다.
1. 파일을 반복문으로 오픈하는것
2. 오픈된 파일에 조건에 맞는 인덱스와 자료에 접근하는것
3. 해당 자료를 변수에 저장하는것
4. 저장한 변수를 논리연산자로 계산하는것
- 개별로 보면 문제를 쉽게 접근 할 수 있다.

## 5. Problem_e

- 요구사항 : 여러개의 파일을 반복문으로 접근하여 원하는 데이터만 추출 및 가공하여 해당 데이터를 가지고 연산하여 조건에 맞는 값을 반환하라.
```python  
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
```

### Problem_e에서 느낀점
- problem_d와 유사한 문제여서 어려움은 없었다.
- problem_d에서 겪었던 해결방법을 바로 e에 적용해서 d에서 소요된 시간보다 굉장히 짧은 시간 내로 해결할 수 있었다.


## 6. Problem_f
- 요구사항 : 여러개의 파일에 접근하여 원하는 데이터를 추출 및 가공하여 반환한다.

```python
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
```

### Problem_f에서 느낀점

- 기존에 앞에서 작성한 것들을 재사용 함에 있어서 큰 어려움을 느끼지 못하였다. 재사용성에 대해 다시한번 중요성을 깨달았다.

## 후기

- 어려운 문제를 세분화 하면 해결하기 쉬워진다.
- 앞서 작성한 함수를 재사용하면 코딩 시간을 단축할 수 있다.
- 공부한 것들을 사용해서 문제를 해결함에 있어서 문제 하나하나가 해결될 때마다 좋았다.