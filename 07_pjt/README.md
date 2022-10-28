# 📅 DB 설계를 활용한 REST API 설계

> 작성일 : 2022-10-28

---

## 📢 문제 별 요구사항

## Modeling

- Actor 
  
  - 배우 데이터 조회

- Movie
  
  - 영화 데이터 조회

- Review
  
  - 리뷰 데이터 조회 / 생성 / 수정 / 삭제

- 각 데이터 조회는 JSON 데이터 타입을 따릅니다.

### 📍 Actor

| 필드명  | 데이터 유형       | 역할    |
|:----:| ------------ |:-----:|
| name | varchar(100) | 배우 이름 |

### 📍 Movie

| 필드명          | 데이터 유형       | 역할     |
| ------------ |:------------:| ------ |
| title        | varchar(100) | 영화 제목  |
| overview     | text         | 줄거리    |
| release_date | datetime     | 개봉일    |
| poster_path  | text         | 포스터 주소 |

### 📍 Review

| 필드명      | 데이터 유형       | 역할                 |
| -------- | ------------ |:------------------:|
| title    | varchar(100) | 리뷰 제목              |
| content  | text         | 리뷰 내용              |
| movie_id | integer      | 외래 키(Movie 클래스 참조) |

### 📍 View

| View 함수명      | 역할                               | 허용 HTTP Method     |
| ------------- |:--------------------------------:| ------------------ |
| actor_list    | 전체 배우 목록 제공                      | GET                |
| actor_detail  | 단일 배우 정보 제공 (출연 연화 제목 포함)        | GET                |
| movie_list    | 전체 영화 목록 제공                      | GET                |
| movie_detail  | 단일 영화 정보 제공 (출연 배우 이름과 리뷰 목록 포함) | GET                |
| review_list   | 전체 리뷰 목록 제공                      | GET                |
| review_detail | 단일 리뷰 조회 & 수정 & 삭제 (출연 영화 제목 포함) | GET / PUT / DELETE |
| create_review | 리뷰 생성                            | POST               |

---

## 💡 문제 별 구현 방법

🎯 **list 조회**

- get_list_or_404 함수로 객체를 전달받습니다.

- 해당 객체를 serializer로 변환해서 Response 를 이용해서 serializer.data 를 응답합니다.

🎯 **detail 조회**

- 조회할 객체의 pk값을 request와 함꼐 전달받습니다.

- get_object_or_404를 사용해서 개별 객체를 전달받습니다.

- 해당 객체를 serializer로 변환해서 Response 를 이용해서 serializer.data 를 응답합니다.

🎯 **영화, 배우 항목 생성**

- views.py 내 각 list함수에서 create합니다.

- request.method가 POST일때 생성합니다.

- request.data를 받아 데이터를 serializer합니다.

- 해당 데이터의 유효성 검사를 진행한 후 데이터를 save()로 저장합니다.

🎯 **리뷰 생성**

- 여타 항목과 다른 로직이 필요합니다.

- 영화 게시물에 리뷰가 생성되므로 게시물을 지정해야합니다.

- 댓글 serializer하나를 생성하여 저장할때 지정된 영화 게시물을 인자로 넘겨줍니다.

- serializer.data를 응답합니다.

🎯 **영화, 배우, 리뷰 수정**

- serializer를 통해 각 데이터들을 전달받습니다 (모델과 데이터를 전달받습니다).

- 해당 serializer를 유효성 검사하고 저장합니다.

- serializer.data를 응답합니다.

🎯 **serializer 수정**

- 영화의 detail에 들어가면 영화의 데이터들만 나오는게 아니라 해당 영화의 배우들 정보까지 출력하고자 했습니다.

- 영화와 배우들의 데이터는 N : N  ManyToManyField로 참조됩니다.

- related_name을 이용해서 해당 name_set 으로 역참조를 할 수 있습니다.

- 하지만, 이렇게 할 경우 기존 serializer에 저장된 형식으로 원하고자하는 fields를 수정할 수 없습니다.

- 그래서 영화 목록에서는 배우들의 이름만 필요하기 때문에 아래와 같이 클래스를 하나 더 생성하였습니다.

```python
class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):

    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewNonIdSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path',)
```

- 위와같이 ActorNameSerializer를 생성해서 movie detail에서 해당 영화의 배우정보는 이름만 나올 수 있게 구현하였습니다.

- 마찬가지로 actor detail 에서는 영화들의 title만 나오게 하기 위해 마찬가지로 클래스를 하나 더 추가하여 구현했습니다.

---

## 💻 출력 결과

- **movies**

<img src="https://user-images.githubusercontent.com/109258052/198512174-b6c3e0e3-566d-47cc-b4ce-a1a29fd832bd.png" title="" alt="image" width="446">

- **movies/detail**

<img src="https://user-images.githubusercontent.com/109258052/198512282-ad6c9086-a7ed-491c-8cd6-bb8af97c1821.png" title="" alt="image" width="243">

- **actors**

<img src="https://user-images.githubusercontent.com/109258052/198512465-420040af-da06-4c1c-85c2-2fe3e2de0451.png" title="" alt="image" width="255">

- **actors/detail**

<img src="https://user-images.githubusercontent.com/109258052/198512378-16e433d5-69e9-4bed-a791-95ffb72f0c22.png" title="" alt="image" width="262">

- **reviews**

<img src="https://user-images.githubusercontent.com/109258052/198512527-de23728d-a39a-407b-9f60-ad19dd2a5d82.png" title="" alt="image" width="265">

- **reviews/detail**

![image](https://user-images.githubusercontent.com/109258052/198512613-055cb0b5-05a6-44c6-9867-74b1d28fad6f.png)

---

## 🚨 에러 및 해결법

- dummy data 를 load할때 에러가 발생했습니다. 더미 데이터와 현재 모델의 형식이 맞지 않으면 충돌이 발생해서 더미데이터에 맞게 모델명들을 수정했습니다.

- 역참조나 참조된 데이터들을 가져올때 해당 serializer의 구조를 변경할려면 새 serialzer를 추가하거나 serializer의 메서드를 이용해야합니다.

---

## 🔥 느낀점 및 후기

😮 이제 Django로 database와 modeling에 관해 어느정도 그림이 그려지는것 같습니다.

😮 앞으로 개발자로써 대규모 서비스와 더 큰 프로젝트를 진행할텐데 미니버전을 경험한것 같습니다.

😮 serializer의 편리함으로 Django를 통해 Json을 응답하는 것을 구현해보니 백엔드 역량이 늘어난 것 같습니다.
