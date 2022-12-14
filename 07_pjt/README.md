# ๐ย DB ์ค๊ณ๋ฅผ ํ์ฉํ REST API ์ค๊ณ

> ์์ฑ์ผ : 2022-10-28

---

## ๐ขย ๋ฌธ์  ๋ณ ์๊ตฌ์ฌํญ

## Modeling

- Actor 
  
  - ๋ฐฐ์ฐ ๋ฐ์ดํฐ ์กฐํ

- Movie
  
  - ์ํ ๋ฐ์ดํฐ ์กฐํ

- Review
  
  - ๋ฆฌ๋ทฐ ๋ฐ์ดํฐ ์กฐํ / ์์ฑ / ์์  / ์ญ์ 

- ๊ฐ ๋ฐ์ดํฐ ์กฐํ๋ JSON ๋ฐ์ดํฐ ํ์์ ๋ฐ๋ฆ๋๋ค.

### ๐ Actor

| ํ๋๋ช  | ๋ฐ์ดํฐ ์ ํ       | ์ญํ     |
|:----:| ------------ |:-----:|
| name | varchar(100) | ๋ฐฐ์ฐ ์ด๋ฆ |

### ๐ Movie

| ํ๋๋ช          | ๋ฐ์ดํฐ ์ ํ       | ์ญํ      |
| ------------ |:------------:| ------ |
| title        | varchar(100) | ์ํ ์ ๋ชฉ  |
| overview     | text         | ์ค๊ฑฐ๋ฆฌ    |
| release_date | datetime     | ๊ฐ๋ด์ผ    |
| poster_path  | text         | ํฌ์คํฐ ์ฃผ์ |

### ๐ Review

| ํ๋๋ช      | ๋ฐ์ดํฐ ์ ํ       | ์ญํ                  |
| -------- | ------------ |:------------------:|
| title    | varchar(100) | ๋ฆฌ๋ทฐ ์ ๋ชฉ              |
| content  | text         | ๋ฆฌ๋ทฐ ๋ด์ฉ              |
| movie_id | integer      | ์ธ๋ ํค(Movie ํด๋์ค ์ฐธ์กฐ) |

### ๐ View

| View ํจ์๋ช      | ์ญํ                                | ํ์ฉ HTTP Method     |
| ------------- |:--------------------------------:| ------------------ |
| actor_list    | ์ ์ฒด ๋ฐฐ์ฐ ๋ชฉ๋ก ์ ๊ณต                      | GET                |
| actor_detail  | ๋จ์ผ ๋ฐฐ์ฐ ์ ๋ณด ์ ๊ณต (์ถ์ฐ ์ฐํ ์ ๋ชฉ ํฌํจ)        | GET                |
| movie_list    | ์ ์ฒด ์ํ ๋ชฉ๋ก ์ ๊ณต                      | GET                |
| movie_detail  | ๋จ์ผ ์ํ ์ ๋ณด ์ ๊ณต (์ถ์ฐ ๋ฐฐ์ฐ ์ด๋ฆ๊ณผ ๋ฆฌ๋ทฐ ๋ชฉ๋ก ํฌํจ) | GET                |
| review_list   | ์ ์ฒด ๋ฆฌ๋ทฐ ๋ชฉ๋ก ์ ๊ณต                      | GET                |
| review_detail | ๋จ์ผ ๋ฆฌ๋ทฐ ์กฐํ & ์์  & ์ญ์  (์ถ์ฐ ์ํ ์ ๋ชฉ ํฌํจ) | GET / PUT / DELETE |
| create_review | ๋ฆฌ๋ทฐ ์์ฑ                            | POST               |

---

## ๐ก ๋ฌธ์  ๋ณ ๊ตฌํ ๋ฐฉ๋ฒ

๐ฏ **list ์กฐํ**

- get_list_or_404 ํจ์๋ก ๊ฐ์ฒด๋ฅผ ์ ๋ฌ๋ฐ์ต๋๋ค.

- ํด๋น ๊ฐ์ฒด๋ฅผ serializer๋ก ๋ณํํด์ Response ๋ฅผ ์ด์ฉํด์ serializer.data ๋ฅผ ์๋ตํฉ๋๋ค.

๐ฏ **detail ์กฐํ**

- ์กฐํํ  ๊ฐ์ฒด์ pk๊ฐ์ request์ ํจ๊ผ ์ ๋ฌ๋ฐ์ต๋๋ค.

- get_object_or_404๋ฅผ ์ฌ์ฉํด์ ๊ฐ๋ณ ๊ฐ์ฒด๋ฅผ ์ ๋ฌ๋ฐ์ต๋๋ค.

- ํด๋น ๊ฐ์ฒด๋ฅผ serializer๋ก ๋ณํํด์ Response ๋ฅผ ์ด์ฉํด์ serializer.data ๋ฅผ ์๋ตํฉ๋๋ค.

๐ฏ **์ํ, ๋ฐฐ์ฐ ํญ๋ชฉ ์์ฑ**

- views.py ๋ด ๊ฐ listํจ์์์ createํฉ๋๋ค.

- request.method๊ฐ POST์ผ๋ ์์ฑํฉ๋๋ค.

- request.data๋ฅผ ๋ฐ์ ๋ฐ์ดํฐ๋ฅผ serializerํฉ๋๋ค.

- ํด๋น ๋ฐ์ดํฐ์ ์ ํจ์ฑ ๊ฒ์ฌ๋ฅผ ์งํํ ํ ๋ฐ์ดํฐ๋ฅผ save()๋ก ์ ์ฅํฉ๋๋ค.

๐ฏ **๋ฆฌ๋ทฐ ์์ฑ**

- ์ฌํ ํญ๋ชฉ๊ณผ ๋ค๋ฅธ ๋ก์ง์ด ํ์ํฉ๋๋ค.

- ์ํ ๊ฒ์๋ฌผ์ ๋ฆฌ๋ทฐ๊ฐ ์์ฑ๋๋ฏ๋ก ๊ฒ์๋ฌผ์ ์ง์ ํด์ผํฉ๋๋ค.

- ๋๊ธ serializerํ๋๋ฅผ ์์ฑํ์ฌ ์ ์ฅํ ๋ ์ง์ ๋ ์ํ ๊ฒ์๋ฌผ์ ์ธ์๋ก ๋๊ฒจ์ค๋๋ค.

- serializer.data๋ฅผ ์๋ตํฉ๋๋ค.

๐ฏ **์ํ, ๋ฐฐ์ฐ, ๋ฆฌ๋ทฐ ์์ **

- serializer๋ฅผ ํตํด ๊ฐ ๋ฐ์ดํฐ๋ค์ ์ ๋ฌ๋ฐ์ต๋๋ค (๋ชจ๋ธ๊ณผ ๋ฐ์ดํฐ๋ฅผ ์ ๋ฌ๋ฐ์ต๋๋ค).

- ํด๋น serializer๋ฅผ ์ ํจ์ฑ ๊ฒ์ฌํ๊ณ  ์ ์ฅํฉ๋๋ค.

- serializer.data๋ฅผ ์๋ตํฉ๋๋ค.

๐ฏ **serializer ์์ **

- ์ํ์ detail์ ๋ค์ด๊ฐ๋ฉด ์ํ์ ๋ฐ์ดํฐ๋ค๋ง ๋์ค๋๊ฒ ์๋๋ผ ํด๋น ์ํ์ ๋ฐฐ์ฐ๋ค ์ ๋ณด๊น์ง ์ถ๋ ฅํ๊ณ ์ ํ์ต๋๋ค.

- ์ํ์ ๋ฐฐ์ฐ๋ค์ ๋ฐ์ดํฐ๋ N : N  ManyToManyField๋ก ์ฐธ์กฐ๋ฉ๋๋ค.

- related_name์ ์ด์ฉํด์ ํด๋น name_set ์ผ๋ก ์ญ์ฐธ์กฐ๋ฅผ ํ  ์ ์์ต๋๋ค.

- ํ์ง๋ง, ์ด๋ ๊ฒ ํ  ๊ฒฝ์ฐ ๊ธฐ์กด serializer์ ์ ์ฅ๋ ํ์์ผ๋ก ์ํ๊ณ ์ํ๋ fields๋ฅผ ์์ ํ  ์ ์์ต๋๋ค.

- ๊ทธ๋์ ์ํ ๋ชฉ๋ก์์๋ ๋ฐฐ์ฐ๋ค์ ์ด๋ฆ๋ง ํ์ํ๊ธฐ ๋๋ฌธ์ ์๋์ ๊ฐ์ด ํด๋์ค๋ฅผ ํ๋ ๋ ์์ฑํ์์ต๋๋ค.

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

- ์์๊ฐ์ด ActorNameSerializer๋ฅผ ์์ฑํด์ movie detail์์ ํด๋น ์ํ์ ๋ฐฐ์ฐ์ ๋ณด๋ ์ด๋ฆ๋ง ๋์ฌ ์ ์๊ฒ ๊ตฌํํ์์ต๋๋ค.

- ๋ง์ฐฌ๊ฐ์ง๋ก actor detail ์์๋ ์ํ๋ค์ title๋ง ๋์ค๊ฒ ํ๊ธฐ ์ํด ๋ง์ฐฌ๊ฐ์ง๋ก ํด๋์ค๋ฅผ ํ๋ ๋ ์ถ๊ฐํ์ฌ ๊ตฌํํ์ต๋๋ค.

---

## ๐ปย ์ถ๋ ฅ ๊ฒฐ๊ณผ

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

## ๐จ ์๋ฌ ๋ฐ ํด๊ฒฐ๋ฒ

- dummy data ๋ฅผ loadํ ๋ ์๋ฌ๊ฐ ๋ฐ์ํ์ต๋๋ค. ๋๋ฏธ ๋ฐ์ดํฐ์ ํ์ฌ ๋ชจ๋ธ์ ํ์์ด ๋ง์ง ์์ผ๋ฉด ์ถฉ๋์ด ๋ฐ์ํด์ ๋๋ฏธ๋ฐ์ดํฐ์ ๋ง๊ฒ ๋ชจ๋ธ๋ช๋ค์ ์์ ํ์ต๋๋ค.

- ์ญ์ฐธ์กฐ๋ ์ฐธ์กฐ๋ ๋ฐ์ดํฐ๋ค์ ๊ฐ์ ธ์ฌ๋ ํด๋น serializer์ ๊ตฌ์กฐ๋ฅผ ๋ณ๊ฒฝํ ๋ ค๋ฉด ์ serialzer๋ฅผ ์ถ๊ฐํ๊ฑฐ๋ serializer์ ๋ฉ์๋๋ฅผ ์ด์ฉํด์ผํฉ๋๋ค.

---

## ๐ฅย ๋๋์  ๋ฐ ํ๊ธฐ

๐ฎ ์ด์  Django๋ก database์ modeling์ ๊ดํด ์ด๋์ ๋ ๊ทธ๋ฆผ์ด ๊ทธ๋ ค์ง๋๊ฒ ๊ฐ์ต๋๋ค.

๐ฎ ์์ผ๋ก ๊ฐ๋ฐ์๋ก์จ ๋๊ท๋ชจ ์๋น์ค์ ๋ ํฐ ํ๋ก์ ํธ๋ฅผ ์งํํ ํ๋ฐ ๋ฏธ๋๋ฒ์ ์ ๊ฒฝํํ๊ฒ ๊ฐ์ต๋๋ค.

๐ฎ serializer์ ํธ๋ฆฌํจ์ผ๋ก Django๋ฅผ ํตํด Json์ ์๋ตํ๋ ๊ฒ์ ๊ตฌํํด๋ณด๋ ๋ฐฑ์๋ ์ญ๋์ด ๋์ด๋ ๊ฒ ๊ฐ์ต๋๋ค.
