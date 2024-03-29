## HTML

- HTML : Hyper Text Markup Language

  - Hyper : 텍스트 등 정보가 동일 선상에 있는것이 아니라 다중으로 연결된 상태
  - Hyper Text : 참조를 통해 다른문서로 접근할 수 있는 텍스트
  - Markup Language : 문서나 데이터의 구조를 명시, 데이터를 표현하기만 한다. (HTML, Markdown)

  - HTML : 웹페이지를 작성하기 위한 언어 (의미와 구조 정의)



### HTML 구조 파악하기

- head와 body로 구성된다.
  - head : 
    - 문서제목, 코드와 같이 문서 정보를 담는다.
    - 브라우저에 표시되지 않는다. (CSS선언, 외부 로딩파일 지정이 가능)
  - body :
    - 브라우저 화면에 나타나는 정보 (실제정보)



- Open Graph Protocol : 
  - 문서 정보를 전달한다.  
  - 페이스북에서 제작,  메타정보에 해당하는 제목, 설명등을 정의했다.



- DOM(Document object model) 트리 - 
  - 동일한 문서를 표현하고 저장하고 조작하는 방법 제공 (구조, 스타일 내용을 변경할 수 있게 도움 가능)
  - Web Page의 객체지향표현



- 요소 :
  - 태그와 태그 사이에 위치한 내용으로 구성
  - 태그는 컨텐츠(내용)를 감싸는 것
  - 내용이 없는 태그들 
    - br, hr, img, input, link, meta
  - 요소는 중첩이 가능하다.
    - 요소의 중첩으로 문서를 구조화할 수 있다.
    - 태그 쌍 확인 필요
    - 오류를 반환하지 않기에 디버깅이 힘들수도 있음



- 속성 : 
  - 태그별로 사용하는 속성이 다르다.
  - 작성방식을 통일 (공백 없애기, 쌍따옴표 사용)
  - 속성을 통해 부가적인 정보가 설정 가능하다.
  - 요소는 속성 정보를 가질 수 있으며 태그와 상관없이 사용 가능한 속성도 있다.

    ```html
    <a href ="https://www.naver.com"></a>
    href = 속성명
    htps://www.naver.com : 속성값
    ```



- HTML global Attribute (모든 HTML요소가 공통적으로 사용할 수 있는 속성)
  - id, class, hidden, lang, style, tabindex, title



- **시맨틱 태그** : HTML5에서 의미론적 요소를 담은 태그
  - div는 의미를 담고 있지 않다. 최대한 div를 사용자제
  - 대표적인 태그
    - header :  문서 전체 헤드
    - nav : 네비게이션
    - aside : 사이드에 위치한 공간
    - section : 문서의 일반적인 구분
    - article : 문서, 페이지, 사이트안에서 독립적으로 구분되는 영역
    - footer 문서 전체나 섹션 마지막 부분
  - 의미를 가지는 태그들을 활용하기 위한 노력이 필요하다.
  - non-semantic : div, span
  - h1, table 태그들도 시맨틱 태그로 볼 수 있다.
  - 요소의 의미가 명확해지면 코드의 가독성을 높이고 유지보수를 쉽게 할 수 있다.



- 그룹컨텐츠
  - \<p> : 문단
  - \<hr> : 헤드라인
  - \<ol>, \<ul> :오더리스트, 언오더리스트
  - \<pre>, \<blockquote> : 인용

- 텍스트관련
  - \<a> : 하이퍼텍스트
  - \<b> 표현상 굵게한다. vs \<strong> 강조!(의미를 가지고있음) 
  - \<span> = \<div> 동일
  - \<b> vs \<strong> , \<i> vs \<em> : strong과 em은 기울어진 글자 (i는 icon에 많이 쓰임)
  - span은 인라인 요소, div는 블록, br은 뉴라인, 

- form : 서버에서 처리될 데이터를 제공하는 역할

- input : 다양한 타입에 따라 동작이 달라지므로 내용 숙지가 필요하다.
  - input은 닫는게 없다
  - autofocus : 자동으로 눌러준다
  - disabled는 비활성화
  - required 필수선택(필수 요구사항)
  - name = 키값
  - placeholder = 흐린글씨로 누르면 없어지는것



- 기타
  - alt : 이미지가 없을경우 대체 문자 출력이 가능하다.
  - action을 통해 서버를 지정하면 해당 서버로 데이터가 날아간다.
  - radio는 한개만 선택가능
  - checkbox는 중복선택이 가능하다.



- 경로
  - 절대경로 : 최초의 시작점으로부터 경유한 경로를 전부 기록하는 방식
    - 최상위 루트 디렉토리인  C부터 보통 시작한다.
  - 상대경로 : 현재 시점을 기준으로 경로가 구성된다.





## CSS(Cascading Style Sheets)

- 스타일, 레이아웃등을 통해 문서를 표시하는 방법을 지정하는 언어

    ```css
    h1{ <-- 선택자
        color : red;  <-- 선언
        font-size : 10px; 속성 : 값
    }
    ```

- 선택자를 통해 스타일을 지정할 HTML요소 선택

- 중괄호 안에는 속성과 값 (쌍으로 이루어져 있다.)
- 속성 : 어떤 스타일 기능 변경

- 값 : 어떻게 스타일 기능을 변경할지



### CSS정의 방법

1. 인라인
   1. 해당 태그에 직접 style 속성을 활용
2. 내부참조 - \<style> 사용
   1. head 태그 내에 style을 지정
3. 외부참조 - 분리된 css파일 사용
   1. 각각의 CSS파일을 만들어 불러와서 쓴다 (외부참조 장점)
   2. 자주 사용하는 속성은 몇개 없다.

​	

### CSS Selector

- HTML에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자가 필요하다

- 기본 선택자
  - 전체선택자, 요소 선택자
  - 클래스, 아이디, 속성 선택자
- 결합자
  - 자손, 자식 결합자
  - 일반 형제, 인접 형제 결합자
- 클래스 선택자와 id선택자는 각각에 맞게 설정을 한다.
- id선택자는 해당 id에 한번만 스타일링 해야한다(중복은 불가), 클래스는 여러번 가능하다.


- 우선순위
  - !important -> 우선순위가 가장 높다
  - 우선순위
    - 인라인 > id선택자 > 클래스 선택자 > 요소 선택자
  - 소스 코드 순서



#### CSS상속

- CSS는 상속을 통해 부모 속성을 자식에게 상속한다.
  - 상속 : 텍스트 관련 요소는 상속되지만 나머지는 되지 않는다.
- 크기단위
  - 픽셀 : 모니터 해상도의 픽셀을 기준 (고정적 단위)
  - % : 백분율 단위, 전체적인 레이아웃에 따라 달라짐, 가변적인 레이아웃에서 자주 사용한다.
  - em : 상속의 영향을 받는다. ex) 부모가 10인데 2em이면 20px이다
  - rem : 상속의 영향을 받지 않음, 최상위 요소를 기준으로 배수단위(최상위 요소는 16px이다)
  - viewport : 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정
- 색상단위
    1. 색상 키워드
       - 대소문자를 구분하지 않는다.
    2. RGB 색상
       - 16진수 또는 함수형 표기법을 사용해서 색을 표현한다.
    3. HSL 색상
       - 색상, 채도, 명도를 통해 표현



#### 결합자

- 결합자

  - 자손결합자 : 자손결합자는 밑에 자손들을 전부 선택(띄어쓰기 사용)
  -  자식결합자 : 자식결합자는 바로 밑에 자식만 선택(>사용)
  - 일반형제결합자 : p ~ span : p뒤에 나타나는 span요소 모두 선택
  - 인접형제결합자 : p + span : p뒤에 바로 해당하는 span태그만 선택

  

#### Box model

- 모든 HTML요소는 box형태
  - content : 글이나 이미지 등 요소의 실제 내용
  - padding : 테두리 안쪽의 내부 여백 요소
  - border : 테두리 영역
  - margin : 테두리 바깥의 외부 여백 (배경 지정 불가능)



- box model 구성
  - 2가지만 제시될 경우 : 상하/좌우
  - 3가지만 제시될 경우 : 상/좌우/하
  - 4가지가 제시될 경우 : 상/우/하/좌



- box sizing
  - 기본적으로 모든 요소는 content-box
    - padding을 제외한 순수 contents 영역으로 box를 지정한다.
  - border까지 너비를 원한다면
    - box-sizing을 border-box로 구성한다.



- 마진 상쇄 : Block A와 Block B에 각각 적용된 margin둘중에서 큰 값으로 겹쳐지게 된다.



#### CSS Display

- display
  - block요소
    - 줄바꿈이 일어나는 요소
    - 화면 크기가 전체의 가로폭을 차지한다.
    - 대표적인 블록 레벨 요소 : div / ul, il, li / p / hr / form 등등
  - inline요소
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로폭을 차지한다.
    - 대표적인 인라인 레벨 요소 : span / a / img / imput, label / b, em, i, strong 등등
  - inline-block
    - block과 inline 특징을 모두 가진다.
  - display none
    - 공간을 차지하지 않는다. 그냥 사라진다.
  - hidden
    - 공간을 차지하고 사라진다.



#### CSS Position

- 문서 상에서 요소를 배치하는 방법을 지정한다.
- static : 모든 태그의 기본 값
  - 일반적인 요소의 배치 순서에 따름

- relative : 상대위치
  - 자기 자신의 static 위치를 기준으로 이동한다.

- absolute : 절대위치 (원래 자리는 없어짐)
  - 요소를 일반적인 문서에 제거 후 레이아웃에 공간을 차지하지 않는다.

- fixed : 고정위치
  - 요소에 관계없이 viewport 기준으로 이동
  - 스크롤 시에도 항상 같은곳에 위치