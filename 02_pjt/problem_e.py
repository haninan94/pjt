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
    for i in range(
        len(response2['cast'])
    ):  # cast 중 cast_id 가 10 미만인 사람들 cast_member 에 추가
        if response2['cast'][i]['cast_id'] < 10:
            cast_member.append(response2['cast'][i]['name'])

    for i in range(
        len(response2['crew'])
    ):  # crew중 department 가 Directing인 사람들을 directing_member 에 추가
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
