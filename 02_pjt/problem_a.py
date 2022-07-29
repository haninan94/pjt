import requests


def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'a69f4da1b285b37e02bb3fb12539afd3',
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()
    return len(response.get('results'))


if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
