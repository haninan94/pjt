import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key': 'ce50b20e835e867dff1aca31fdcb5577',
    'region': 'KR',
    'language': 'ko',
}

response = requests.get(BASE_URL + path, params=params)
pprint(response.json())
print(response.url)
