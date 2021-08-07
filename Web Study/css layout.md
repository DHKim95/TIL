## CSS layout

- 웹페이지에 포함되는 요소를 어떻게 취합하고 그것들을 어느 위치에 놓일 것인지 제어



#### Float

- 본래의 이미지 주변으로 텍스트를 둘러싸는 레이아웃 -> 전체 레이아웃을 만드는것으로 발전했다.

- 속성
  - none : 기본값
  - left : 요소를 왼쪽으로 띄운다.
  - right : 요소를 오른쪽으로 띄운다.



- float clear
  - 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성한다.
  - content 속성과 함께 요소에 장식용 콘텐츠를 추가할 때 사용

- ::after 선택한 요소 맨 마지막 자식으로 가상 요소를 하나 생성

    ```css
    .clearfix::after {
        clear:both;
    }
    
    after은 가상요소
    left, right다 가능 보통은 clear:both 사용
    ```

- Float 정리
  - flexbox 및 그리드 레이아웃 기술이 나오기 이전에 Float은 열 레이아웃 만드는데 사용
  - flexbox와 grid 출현으로 float 이미지 역할로 되돌아감
  - 웹에서 여전히 사용도 함





#### CSS flexible box layout

- 요소간 공간 배분과 정렬기능을 위한 1차원 레이아웃

- 오랫동안 레이아웃 작성도구는 float와 positioning -> 문제가 있는건 아니지만 제한적이고 한계적

- 요소와 축은 반드시 기억
  - 요소 : Flex Container(부모요소), Flex Item(자식요소)
  - 축 : main axis(메인축), cross axis(교차축 ) -> 메인축을 x축이라 생각하면 안된다.



- Flexbox는 축과 container, item이 전부이다.
  - Flex container
    - 레이아웃을 형성하는 기본 모델
    - Flex item이 놓여있는 영역
    - 생성하려면 display속성을 flex or inline-fliex
  - Flex item
    - 컨테이너의 컨텐츠



- Flex에 적용하는 속성
  - 배치방향설정 flex-direction (메인축만 알면됨)
  - 메인축방향정렬 : justify-content
  - 교차축방향정렬 : align-items, align-self, align-content
  - 기타 : flex-wrap, flex-flow, flex-grow, order



#### flex-box

- flex-direction
  - flexbox는 단방향 레이아웃
  - row(default) 오른쪽, column은 밑으로, reverse붙이면 반대로 간다.
  - content는 여러줄 정렬, items는 한줄정렬, self는 개별요소
  - ex) justify-content : 메인축 기준 여러줄 정렬

- 명령어
  - justify-content
    - flex-start : 시작점부터 차례로 
    - flex-end : 뒤쪽부터 차례로 
    - center : 정중앙 
    - space-between : 좌우 정렬 
    - space-around : 균등 좌우 정렬(내부 여백은 외곽의 2배) 
    - space-evenly : 균등 정렬 -> 내부 외각 동일
  - align-items
    - flex-start, flex-end, center, stretch
  - align-content
    - flex-start, flex-end, stretch, space-between, space-around
  - align-self
    - flex-start, flex-end, center, stretch
  - flex-wrap
    - 요소들이 강제로 한줄에 배치 되게 할지 설정
    - nowrap : 모든 아이템이 한줄에 표시
    - wrap : 넘치면 그다음줄로 계속
    - wrap-reverse : 넘치면 윗줄로 보내기
  - flex-grow
    - 메인축에서 남은 공간을 쪼개서 나눈다.(남은 공간에 대한 배분)
  - flex-flow
    - flex-direction과 flex-wrap의 동시사용
  - order : 작은 숫자 일수록 앞으로 간다. (기본 0)





