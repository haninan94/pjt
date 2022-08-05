# open 및 json 모듈 사용예시

import json
from pprint import pprint

movie = open('sample.json', encoding='utf-8')  # 상대경로
movie_detail = json.load(movie)  # json -> dict

print(movie_detail)
pprint(movie_detail)  # 딕셔너리를 가독성 있게 출력
