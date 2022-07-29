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
