# 📅 Django 웹페이지 제작

> 작성일 : 2022-09-02 
> 작성자 : 한인환

## 📢 문제 별 요구사항

---

📍 **base.html**

- 모든 템플릿 파일은 base.html을 상속받아 사용합니다.

- bootstrap양식을 상속받습니다.

📍 **index.html**

- "전체 영화 목록 조회 페이지"
  
  - 데이터 베이스에 존재하는 모든 영화의 목록을 표시합니다.
  
  - 적절한 HTML 요소를 사용하여 영화 제목 및 평점을 표시하며, 제목을 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동합니다.

📍 **detail.html**

- "영화 상세 정보 페이지"
  
  - 특정 영화의 상세 정보를 표시합니다.
  
  - 해당 영화의 수정 및 삭제 버튼을 표시합니다.
  
  - 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

📍 **new.html**

- "영화 생성 페이지"
  
  - 특정 영화를 생성하기 위한 HTML form 요소를 표시합니다.
  
  - 작성한 정보는 제출(submit)시 단일 영화 데이터를 저장하는 URL로 요청과 함께 전송됩니다.
  
  - 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

📍 **edit.html**

- "영화 수정 페이지"
  
  - 특정 영화를 수정하기 위한 HTML form 요소를 표시합니다.
  
  - HTML input 요소에는 기존 데이터를 출력합니다.
  
  - Reset 버튼은 사용자의 모든 입력을 초기 값으로 재설정 합니다.
  
  - 작성한 정보는 제출(submit)시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송됩니다.
  
  - 영화 상세 정보 페이지(detail.html)로 이동하는 링크를 표시합니다.



## 💡 문제 별 구현 방법

---

🎯 **base.html**

- project와 app과 같은 경로에 templates 폴더를 생성해서 templates에 base.html을 생성한다.

- bootstrap cdn을 적용하고 block으로 예외 부분 적용한다.

🎯 **index.html**

- 홈페이지라고 볼 수도 있다.

- movies/urls.py 에 path를 작성한다.

- movies/views.py 에 함수를 작성해서 movies 객체를 만들어 데이터를 참조하고 index.html을 rendering할 수 있도록 한다.

- 해당 데이터를 가지고 movies/templates/movies/index.html에 html로 홈페이지에 보여질 화면을 구상한다.

- 새로운 영화 데이터를 만들 수 있는 CREATE(NEW) 하이퍼 링크를 만든다.

🎯 **new.html**

- 새로운 영화 데이터를 생성하는 page이다.

- movies/urls.py 에 path를 작성한다.

- movies/view.py 에 def 함수를 작성해서 html을 rendering 할 수 있도록 한다.

- form 태그로 영화의 정보를 제출할 수 있게 작성한다.

- 작성한 DATA는 create로 전달된다.

- 전체 영화 목록 조회 페이지 (index.html)로 이동하게 a태그를 이용한다.

🎯 **create**

- new에서 전달받은 데이터들을 POST형태로 받아 get메서드로 벨류를 저장한다.

- 저장한 데이터들을 통해 movie라는 인스턴스를 생성한다.

- 해당 인스턴스를 detail에 전달한다.

🎯 **delete**

- 자료를 제거할 수 있게 delete 함수를 작성합니다.

- movie 의 pk(prime key) 값을 받아 해당 pk의 값을 delete 해서 index로 redirect합니다.

🎯 **edit.html**

- movies/urls.py 에 path를 작성한다.

- movies/view.py 에 def 함수를 작성해서 html을 rendering 할 수 있도록 한다.

- create에서 전달받은 데이터들을 html 로 작성하여 화면을 구상합니다.

- detail.html 에서 edit과 delete를 위한 이동 버튼을 작성합니다.

- detail.html 에서 index.html로 이동할 수 있는 버튼을 작성합니다.

🎯 **update**

- 자료를 업데이트할 함수를 작성합니다.

- request로 자료를 전달받아 해당 클래스의 변수에 저장합니다.

- detail로 redirect합니다.





## 💻 출력 결과

---

- index

<img src="https://user-images.githubusercontent.com/109258052/188260393-43c7ab37-514e-4d0a-86f4-26bbb5a9c628.PNG" title="" alt="home" width="385">

- new

<img src="https://user-images.githubusercontent.com/109258052/188260412-af0fc105-6250-4931-b3e9-8fe2459333e5.png" title="" alt="image" width="279">

- detail

<img src="https://user-images.githubusercontent.com/109258052/188260436-63161a11-6792-4622-ada7-b60b0b2cb427.png" title="" alt="image" width="185">

- edit

<img src="https://user-images.githubusercontent.com/109258052/188260452-437e1ee1-61ea-43b7-9e2b-fb10d8ca75a9.png" title="" alt="image" width="275">





## 🚨 에러 및 해결법

---

- 대부분의 오류는 오타나 적어야할 내용을 적지 못해서 발생했다.

- 가령 return render(request , 'xxx.html') 이렇게 작성해야 하는데 render를 빼먹었다던가 데이터베이스에서 변수의 형식을 지정할때 클래스 인스턴스를 만드는 과정에서 괄호를빼먹었다던가 불러온 변수에서 s를 빼먹고 작성하였다던가 오타나 필요한 내용을 적지 않았을때 발생했다.

- 기존 03_pjt(이전 웹 프로젝트) 에서 사용하던 폼에 이번에 진행한 프로젝트를 적용할려고 했을때 static에대한 개념을 같은반 학우에게 전달받아(학우님 감사합니다.) 적용했다.

- 상속받는 쪽에서 load static을 적용해야하는지 상속하는 곳에 적용해야 하는지에 대한 문제에서 상속받는곳 block내 최상단에 적용했을때 정상적으로 실행되는것을 확인하였다.





## 🔥 느낀점 및 후기

---

👿 저번 웹 프로젝트와 마찬가지로 하나를 고치면 다른 곳에서 문제가 발생한다.

👿 하나의 html을 작성하면 그냥 넘어가는 경우가없다. 매번 오류가 난다.

👿 좀더 내용을 숙지해서 기존의 자료 없이도 혼자 0에서 100까지 코딩 할 수 있도록 공부가 필요하다.

👿 오류 해결한다고 오타찾는시간이 걸려서 home 화면밖에 css를 적용하지 못했다.

😮 이전에 내가 작성한 웹 프로젝트에 이번 django project를 적용해서 사이트를 구동하니까 굉장히 재미있었다.

😮 이런식으로 규모를 늘려가면 하나의 서비스를 제공하는 시스템을 만들 수 있을 것 같다는 생각이 들었다.

👍 역시나 기존에 있던 자료를 활용하니까 두개의 프로젝트를 합치는데는 시간이 많이 걸리지 않았다.

👍 Framework의 위대함을 또한번 느낄 수 있었다.


