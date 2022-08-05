# &#128197; 반응형 웹페이지 제작

> 작성일 : 2022-08-05  
> 작성자 : 한인환

## &#128226; 문제 별 요구사항

&#128205; **navigation bar**
  - 네비게이션 바는 항상 화면 상단에 고정
  - 네비게이션 메뉴 중 Home과 Community는 하이퍼링크 역할
  - 네비게이션 메뉴 중 Login은 Modal창을 생성
  - 가로가 768px 미만이면 토글 사용
  - 
&#128205; **footer**
  - footer에 작성된 내용은 수직, 수평 가운데 정렬되어 있습니다.

&#128205; **header**
 - 지정된 이미지 3장이 자동으로 전환

&#128205; **home_section**
 - Section 내부의 개별 요소들은 Card로 구성 이미지, 제목, 설명을 포함합니다.
 - Viewport의 가로 크기가 576px에 따라 보여지는 카드의 수 조절
 - 개별 요소가 일정한 간격 유지

&#128205; **community**
- community_Aside
  - 내부의 각 항목이 클릭 가능한 하이퍼링크
  - Viewport의 가로 크기(992px)에 따라 영역 조절
- community_section
  - Viewport의 가로 크기(992px)에 따라 영역 조절
  - Viewport가 992 이하일때와 이상일때 다른 방식으로 Table나오게 조정
- community_pagination
  - 게시판 하단에 위치하며 너비 자유
  - 자신의 영역 안에서 수평 중앙 정렬
  - 내부의 항목들이 전부 하이퍼링크
  
</br></br>


## 💡 문제 별 구현 방법

🎯 **navigation bar**
- Bootstrap Navbar Component 를 활용하여 제작하였다. 기존의 Navbar요소에서 앞 부분만 로고로 바꿔주고 기타 색상 설정등을 넣어서 네비게이션 바를 디자인 하였다.

- 로고 부분은 `<a>`태그에 하이퍼링크 옵션을 주고 그 안에 `<img>`태그를 넣었다.
  
- 네비게이션 메뉴 부분중 Login 부분은 Bootstrap Modal Component 를 활용하여 Login 버튼을 눌렀을때 Modal 창이 뜨도록 했다.

- 화면이 md 사이즈 이하로 작아졌을때 navigation menu 들이 toggle로 작동하는 것은 Bootstrap Navbar Component 에 기본으로 있었으며 해당 코드 내에서 lg값을 md값으로만 
수정하였다.

</br><br>
🎯 **header**

- 주어진 이미지 3장을 Bootstrap Carousel Component 를 활용해서 자동으로 슬라이드 되도록 구현하였다.

</br><br>

🎯 **home_section**

- 영화 포스터, 영화 제목, 영화 줄거리 등이 Card처럼 나오게 하기 위해 Bootstrap Card Component 를 활용했으며 card 클래스 내에서 row-col-sm-3 을 통해서 가로 크기가 576px이상일때 3개 씩 보여주도록 지정하였고, 그 이하일때는 하나씩 보이도록 하였다.

</br><br>

🎯 **community_Aside**

- Bootstrap List group Component 를 활용해서 메뉴 리스틀 만들었으며 각 항목은 하이퍼링크로 지정하였다.
- 해당 메뉴는 Viewport 992px 기준으로 화면이 다르게 보이게 구현하였다.

</br><br>

🎯 **community_Section**

- 게시판은 Bootstrap Tables Content 를 활용해서 구현하였다.
- talbe-dark 클래스와 table-striped 클래스를 이용하여 table을 디자인 했다.
- Display Component 내에서 Hiding Elements 를 이용하여 Viewport 의 크기마다 다른양식의 Table이 나오게 구현 하였다.
- 해당하는 Viewport의 크기가 되면 해당되지 않는 요소들은 Hiding하는 방식을 사용했다.

</br><br>

## &#128187; 출력 결과

- navigation bar (Viewport 768px 이상일때)

![image](https://user-images.githubusercontent.com/109258052/183033011-9e945c62-d211-4041-b071-d597c02b02eb.png)

- navigation bar (Viewport 768px 미만일떄 0

![image](https://user-images.githubusercontent.com/109258052/183032906-d401f0ff-690f-4b21-a8a4-7a9e1fccba5b.png)

</br><br>

- header, footer

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/109258052/183033691-d4d0c758-eb35-4289-9b96-c63889a6a7ae.gif)

</br><br>

- community (Viewport 992px 이상일떄)

<img src="https://user-images.githubusercontent.com/109258052/183033974-b412af6d-09f9-4213-832f-9135f2673b55.png" width="50%" height="50%"/>

- community (Viewport 992px 미만일떄)

<img src="https://user-images.githubusercontent.com/109258052/183034349-c45fd6ab-4dd6-40ce-a166-b6ccf5508ee4.png" width="50%" height="50%"/>

</br><br>

## &#128680; 에러 및 해결법

- navigation bar 제작할때 component 이용하지 않고 직접 만들려고 하였으나, 네비게이션 메뉴들이 수직 정렬이 되지 않는 현상이 발생했었으나 Bootstrap Navbar Component 를 사용해서 접근방식을 바꾸었다. 기존의 Navbar 양식(해당 양식에서는 navgation menu들이 자동 수직정렬 되어 있었음)에서 Narbar Brand부분의 텍스트 태그를 하이퍼링크 이미지 태그로 바꾸어서 해결하였다.

- navigation menu중 Login을 클릭 하여도 modal이 연결되지 않아서 data-target, data-toggle 클래스를 data-bs-target, data-bs-toggle로 수정하였다. bootstrap 5 부터 bs를 넣어줘야한다.

- Viewport에 따라서 화면이 완전 다르게 나오는 idea가 떠오르지 않았으나 같은 반 학우분들께 여쭤봐서 hiding elements 를 사용해서 2개의 창을 적절히 숨겨서 다른 화면을 구현하게 한다는 알아내서 해결하였다.

</br><br>

## &#128293; 느낀점 및 후기


&#128127; 하나를 고치면 다른하나가 문제가 발생한다.

&#128127; 프론트 엔드는 디버깅 하기도 어렵고 무엇이 잘 못 되었는지도 힘들었다. 

&#128127; Component에 의지하며 코딩했기에 Component를 사용하고 오류가 발생하면 어디서 발생되었는지를 파악해야 하는데 Component 를 분석하고 코딩하기에는 너무 오랜 시간이 걸렸다.

&#128558; 껍데기 뿐일 홈페이지만 그래도 나름의 껍데기라도 구현해봤다는 경험이 색달랐다.

&#128077; 컴포넌트를 사용해서 굉장히 편리했다. (재사용성의 장점)

&#128077; 프론트 엔드를 직업으로 하시는 분들 존경합니다.
