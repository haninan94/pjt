## 📅 Vue를 활용한 SPA 구성

> 작성일 : 2022-11-11

## 📢 문제 별 요구사항

---

> **A. 최고 평점 영화 출력**

- 네비게이션 바에서 Movie 링크(/movies)를 클릭하면 AJAX 통신을 이용하여 TMDB API로 부터 JSON 데이터를 받아와 다음과 같이 영화 목록을 출력합니다.

> **B. 최고 평점 영화 중 랜덤 영화 한 개 출력**

- 네비게이션 바에서 Random 링크(/random)를 클릭하면
  저장된 최고 평점 영화 목록 중 랜덤으로 한 개를 출력합니다.

> **C. 보고 싶은 영화 등록 및 삭제하기**

- 네비게이션 바에서 WatchList 링크(/watch-list)를 클릭하면
  보고 싶은 영화 제목을 등록할 수 있는 Form이 출력됩니다.

- 등록된 영화 제목을 클릭하면 취소선이 그어집니다.

---

## 💡 문제 별 구현 방법

🎯 **최고 평점 영화 출력**

- 최고 평점 영화 데이터가 필요합니다. 
  
  - axios.get 을 이용해서 TMDB API 에서 Json 형태로 최고 평점 영화 데이터를 받아옵니다.

- 각각의 영화 객체를 v-for를 통해서 MovieCard컴포넌트에서 꺼내 출력합니다.



🎯 **최고 평점 영화 중 랜덤 영화 한 개 출력**

- 최고 평점 영화 데이터는 위에서 구한 데이터를 사용합니다.

- 화면 내 button을 click하면 getRandomMovie() 메서드를 실행합니다.
  
  - axios.get을 통해 TMDB API에서 받아온 url을 response로 전달합니다.
  
  - 해당 response에서 필요한 데이터만 movies에 저장합니다.
  
  - 랜덤한 movie하나가 필요하므로 lodash 라이브러리를 사용합니다.
  
  - lodash를 사용하여 sampling된 movie의 정보를 data에 저장합니다.

- 해당 데이터를 template부분에 작성합니다.



🎯 **보고 싶은 영화 등록 및 삭제하기**

- text box에 영화를 넣고 Enter가 입력되면 목록이 추가될 수 있게 구현했습니다.
  
  - Enter가 눌러진다면 createWatchList() 메서드가 실행됩니다.
  
  - store/index.js에서 watch list에 들어갈 항목이 추가되는 로직이 실행됩니다.

- 항목을 클릭하면 줄이 쳐지는 효과와 배경색이 바뀌게 구현했습니다.
  
  - 항목을 클릭하면 updateItemStatus() 메서드가 실행됩니다.
  
  - store/index.js에서 watch list의 isCompleted 항목이 boolean값으로 treu와 false가 토글될 수 있게 처리합니다.
  
  - 항목이 isCompleted의 값에 따라 줄이 그어지는 효과와 배경색이 바뀝니다.

---

## 💻 출력 결과

- Movies

<img src="https://user-images.githubusercontent.com/109258052/201295667-18ab072e-1528-4bd3-b6c4-532f6c20db43.png" title="" alt="image" width="415">

- Random

<img src="https://user-images.githubusercontent.com/109258052/201295772-6de9f0ed-dbcf-44fe-86a2-d121b0381fc1.png" title="" alt="image" width="417">

- Watch List

<img src="https://user-images.githubusercontent.com/109258052/201296031-e6c9bd60-0a36-4648-8ddc-ce2a0a7a229f.png" title="" alt="image" width="427">

---

## 🚨 에러 및 해결법

- 처음에 Random 페이지에서 Pick을 누르지 않으면 영화 항목이 자동으로 로드되지 않는 현상이 발생했습니다.
  
  - created() 를 통해서 굳이 Pick을 누르지 않더라도 우선 만들고 시작하게끔 처리하였습니다.

---

## 🔥 느낀점 및 후기

- 부트스트랩에 의존하지 않고 css를 더 공부해서 자유자재로 커스텀 해야겠다는 생각이 들었습니다.

- 시간을 투자할수록 눈에 확 변화가 느껴지는게 front-end의 매력인거 같습니다.

- Final Project에 얼마나 많은 시간을 쏟아부어야 할지 감이 안옵니다.
