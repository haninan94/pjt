# 📅 알고리즘을 적용한 서버 구성



> 작성일 : 2022-11-04



## 📢 문제 별 요구사항

> **A. 유저 팔로우 기능**

- 팔로우 버튼을 클릭하는 경우, **AJAX 통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성**합니다.



> **B. 리뷰 좋아요 기능**

- 좋아요 버튼을 클릭하는 경우, **AJAX통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성합니다.**



> **C. Movies 앱 기능**

1. 전체 영화 목록 조회 (index)
   
   - 사용자의 인증 여부와 관계없이 **전체 영화 목록 조회 페이지**에서 적절한 UI를 활용하여 영화 목록을 제공합니다. (사용자에게 제공할 HTML은 **index.html**)



2. 단일 영화 상세 조회 (detail)
   
   - 사용자의 인증 여부와 관계없이 **단일 영화 목록 조회 페이지**에서 적절한 UI를 활용하여 영화 목록을 제공합니다. (사용자에게 제공할 HTML은 **index.html**)

---

## 💡 문제 별 구현 방법



🎯 **유저 팔로우 기능**

- 자바스크립트를 이용하였습니다.

- 팔로우 언팔로우 제출 폼을 query selector로 설정하여 csrf는 header로 전달합니다.

- 팔로우나 언팔로우 버튼이 submit될 때 addEventListener가 호출됩니다.

- 해당 함수가 호출되면 폼에 적용될 속성들을 axios로 설정합니다.

- views.py 에서 follow시 is_followed 변수를 boolean값으로 설정합니다.

- profile.html script태그에서 isFollowed를 선언해서 해당 변수가 True일때와 False일때를 분기처리 해줍니다.

- 분기 처리에 따라서 followButton.value를 이용해서 버튼의 값이 토글되게 설정합니다.



🎯 **리뷰 좋아요 기능**

- 유저 팔로우 기능과 마찬가지입니다.

- 하지만, 리뷰는 해당 페이지에 리뷰가 여러개이기 때문에 어떤 리뷰에 좋아요를 누를 것인지 생각해야합니다.

- body 부분에서 review를 for문을 통해 반복합니다.

- script부분에서는 forEach로 모든 반복되는 폼들이 ${reviewPk} 를 통해 각 리뷰마다 각각 접근하도록 합니다.

- 좋아요나 좋아요 취소 버튼이 submit될 때 addEventListener가 호출됩니다.

- 해당 함수가 호출되면 폼에 적용될 속성들으 axios로 설정합니다.

- views.py 에서 like할시 is_liked 변수를 boolean값으로 설정합니다.

- index.html script태그에서 isLiked를 선언해서 해당 변수가 True일때와 False일때를 분기처리 해줍니다.

- 분기 처리에 따라서 likeButton.innerHTML을 통해 하트가 채워졌다 비워졌다 할 수 있게 설정합니다.



🎯 **Movies 앱 기능**

- index
  
  - views.py에서 Movie.objects.all() 로 모든 영화를 context로 전달합니다.
  
  - index.html에서 movies들을 for문으로 반복적으로 접근해서 영화정보를 보여줍니다.

- detail
  
  - views.py에서 movie_pk 정보를 받아 detail하게 보여줄 영화 하나를 context로 전달합니다.
  
  - detail.html 에서 전달받은 movie_pk 에 해당하는 movie하나에 대한 영화정보를 보여줍니다.



---

## 💻 출력 결과

- **유저 팔로우 기능**

![팔로우_언팔로우](https://user-images.githubusercontent.com/109258052/199891771-16c24163-3130-4302-8122-2ab5dc9de216.gif)



- **리뷰 좋아요 기능**

<img src="https://user-images.githubusercontent.com/109258052/199892375-b7a77301-ada4-4210-a6e5-42f8fe067777.gif" title="" alt="like_unlike" width="258">



- **Movies Index**

<img src="https://user-images.githubusercontent.com/109258052/199893080-63dbb8e1-4fa7-463c-995a-7e1559c72cbf.gif" title="" alt="movies_index" width="265">



- **Movie Detail**

<img src="https://user-images.githubusercontent.com/109258052/199893818-048c0c2b-74c3-41e0-aa21-f44c4c3823e8.gif" title="" alt="Movie_Detail" width="325">

---

## 🚨 에러 및 해결법

- base.html 에서 설정한 block 설정을 잘못해서 const forms 가 두번 작성되어서 forms가 재선언 되어서 오류가 발생했습니다. 해당 오류는 html 파일에서 block의 구역을 재설정해서 해결하였습니다.

---

## 🔥 느낀점 및 후기

- 그동안 배운 javascript로 AJAX를 구현해서 새로고침 없이 홈페이지를 구현했습니다. 이런식으로 기능을 늘려가면 컴퓨니티를 구현할 수도 있을 것 같습니다.

- 하지만, 생각해보니 커뮤니티만해도 여러개 기능이 한두개가 아니라서 하나의 커뮤니티를 만드는데도 상당히 많은 작업이 필요할 것 같습니다.

- 서비스 하나를 구현하는데 굉장히 많은 시간과 노력이 들어가는데 짐작이 가지않는게 두렵습니다.


