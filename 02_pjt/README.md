# 02 PJT
> 작성자 : 한인환  
> 작성일 : 2022-07-29
---
## 1.Problem_a
- 요구사항 : requests 라이브러리를 사용하여 현재 인기가 있는 영화 목록의 데이터를 요청하여 응답 받은 데이터의 영화 개수를 반환하라.

```python
import requests

def popular_count():

    BASE_URL = 'https://api.themoviedb.org/3' # 주소지정
    path = '/movie/popular' # 경로지정
    params = { # 파라미터들 지정
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json() # 데이터 요청해서 response 에 받아오기
    return len(response.get('results')) # 원하는 조건에 맞는 값 반환

if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
  ```
### Problem_a 해결 방법
&#9989; 서버로 부터 데이터를 요청한다.  
&#9989; 요청받은 데이터를 response변수에 할당한다  
&#9989; response데이터 중 results의 길이를 반환한다.

### Problem_a 에서 느낀점
- 서버에서 가져온 데이터가 어떤 형식인지 확인하지 않고 코드를 작성해서 값을 반환 받았더니 기대와 다른값이 나왔다. 반환받은 데이터가 어떤 구조인지 확인하고 접근할 필요가 있다.

## 2. Problem_b
- 요구사항 : 서버에서 불러온 데이터를 조건화 하여 원하는 값만 반환하라

```python
import requests
from pprint import pprint


def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json() # 데이터 요청해서 response 에 받아오기
    vote_average_eight = [] # 8점이 넘는 영화들이 들어갈 리스트 생성
    for i in range(len(response['results'])): # 조건에 맞는 영화들을 골라서 vote_average_eight 에 넣는 반복문
        if response['results'][i].get('vote_average') >= 8:
            vote_average_eight.append(response['results'][i])
    pprint(vote_average_eight)


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """
```

### Problem_b 해결방법
&#9989; 서버로 부터 데이터를 요청한다.  
&#9989; 요청받은 데이터를 response변수에 할당한다  
&#9989; 요청받은 데이터중 vote_average를 반복문과 if문을 활용하여 8점 넘는 영화만 빈 리스트에 할당해서 새로 리스트를 만든후 해당 리스트를 반환한다. 

    
### Problem_b 에서 느낀점
- 서버에서 불러온 데이터를 조건에 맞게 반환하는 걸 이미 이전에 경험했었기 때문에 이번에는 무난하게 해결하였다.

## 2. Problem_c
- 요구사항 : 서버에서 불러온 데이터를 받아 원하는 값으로 정렬하라

```python
import requests
from pprint import pprint


def ranking():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json() #  데이터 요청헤서 response 에 저장
    movie_information = response['results'] # 요청한 데이터중 일부만 할당
    data = sorted(  # 데이터 정렬
        movie_information, key=lambda score: score['vote_average'], reverse=True
    )
    return data

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
```

### Problem_c 해결방법
&#9989; 서버로 부터 데이터를 요청한다.  
&#9989; 요청받은 response 변수에 할당한다.  
&#9989; response 변수를 sorted() 함수를 이용해서 response변수 내 vote_average키의 value값으로 내림차순 정렬한다.

### Problem_c 에서 느낀점
- 불러온 데이터가 리스트 안에 여러개의 리스트를 가진 구조로 되어있어서 sorted()함수 내 특정 파라미터들을 이용하는 경험이 없었기 때문에 이 부분에서 lambda 함수를 이용해서 리스트 내 vote_average 변수를 지정해줘서 해결하였다.

## 2. Problem_d
- 요구사항 : 서버에서 불러온 데이터를 받아 원하는 해당 값을 참고하여 다른 데이터를 요구하여 요구한 데이터를 가공하여 조건에 맞게 반환한다.

```python
import requests
from pprint import pprint


def recommendation(title):
    if title == '검색할 수 없는 영화':
        return None

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
        'query': title,
    }
    response = requests.get(BASE_URL + path, params=params).json()
    id = response['results'][0].get('id')  # 요청받은 데이터들중 첫번째 영화 id를  id에 저장

    BASE_URL = 'https://api.themoviedb.org/3'  # 해당 id를 서버에 전달하여 데이터 요청
    path = f'/movie/{id}/recommendations'
    params = {
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
    }

    response2 = requests.get(BASE_URL + path, params=params).json()
    recommendation_movie = []
    for i in range(len(response2['results'])):  # 추천영화 목록에 조건에 맞는 영화들 추가
        recommendation_movie.append(response2['results'][i].get('title'))

    return recommendation_movie


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
```

### Problem_d 해결방법
&#9989; 서버로 부터 데이터를 요청한다.  
&#9989; 요청받은 response 변수에 할당한다.  
&#9989; recommendation 에서 인자로 받은 '기생충'을 검색하여 최상단 영화의 'id'를 id 변수에 할당한다.  
&#9989; 해당 id 변수를 이용해서 다시 서버에 추천 영화 목록 데이터를 요청한다.  
&#9989; 해당 데이터를 response2 변수에 할당한다.  
&#9989; response2 변수에서 추천 영화목록들을 recommendation_move리스트에 추가한 후 반환한다.  

### Problem_d 에서 느낀점
- 서버에 요청한 데이터를 참고하여 다시 서버에 재 요청하여 데이터를 조건에 맞게 반환하는 과정이 있었는데, 데이터를 재요청하는 방식을 적용해서 해결하였다.


## 2. Problem_e
- 요구사항 : 서버에서 불러온 데이터를 받아 원하는 해당 값을 참고하여 다시 서버에 다른 데이터를 요구하여 요구한 데이터를 가공하여 조건에 맞는 값만 반환하라.

```python
import requests
from pprint import pprint


def credits(title):
    if title == '검색할 수 없는 영화':
        return None

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
        'query': title,
    }
    response = requests.get(BASE_URL + path, params=params).json()
    id = response['results'][0].get('id')  # 요청받은 데이터들중 첫번째 영화 id를  id에 저장

    BASE_URL = 'https://api.themoviedb.org/3'  # 해당 id를 서버에 전달하여 데이터 요청
    path = f'/movie/{id}/credits'
    params = {
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
    }
    response2 = requests.get(BASE_URL + path, params=params).json()
    cast_member = [] 
    directing_member = []
    for i in range(len(response2['cast'])): # cast 중 cast_id 가 10 미만인 사람들 cast_member 에 추가
        if response2['cast'][i]['cast_id'] < 10:
            cast_member.append(response2['cast'][i]['name'])

    for i in range(len(response2['crew'])): # crew중 department 가 Directing인 사람들을 directing_member 에 추가 
        if response2['crew'][i]['department'] == 'Directing':
            directing_member.append(response2['crew'][i]['name'])

    return {'cast': cast_member, 'directing': directing_member}


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
```

### Problem_d 해결방법
&#9989; 서버로 부터 데이터를 요청한다.  
&#9989; 요청받은 response 변수에 할당한다.  
&#9989; recommendation 에서 인자로 받은 '기생충'을 검색하여 최상단 영화의 'id'를 id 변수에 할당한다.  
&#9989; 해당 id 변수를 이용해서 다시 서버에 영화 관계자 정보를 요청한다.  
&#9989; cast_member에 반복문과 조건문을 이용하여 cast_id가 10 미만인 사람들을 추가한다.  
&#9989; directing_member에 반복문과 조건문을 이용하여 department가 Directing인 사람들을 추가한다  
&#9989; cast_member와 directing_member를 양식에 맞게 반환한다.

### Problem_e 에서 느낀점
- 서버에 요청한 데이터를 참고하여 다시 서버에 재 요청하여 데이터를 조건에 맞게 반환하는 과정이 problem.d 에 있어서 해당 부분을 재사용하여 e에 적용하고 문제를 풀었기 때문에 수월하게 문제를 해결한 감이 있었다.
> **총평**  

&#128578; 이미 외부 데이터를 불러와서 이용하는 경험을 해봤기 때문에 저번 01_pjt 보다 난이도가 쉽게 느껴졌다.  
&#128578; 웹에 처음으로 url과 path 파라미터를 전달해서 데이터를 요청하고 해당 데이터를 json으로 반환받아 처리하는 과정을 경험했기에 색다른 경험이었다.  
&#128531; json 자료가 커지면서 visual studio code 에서는 가독성이 떨어지는 부분이 있었다.