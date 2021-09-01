# Django

- 장고는 파이썬을 이용한 웹 프레임워크다.
- 어플리케이션 : 기능단위로 작성하는것이 좋다.



### Web(World Wide Web)

- web : 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 정보공간

- Static web page(정적 웹 페이지)
  - 서버에 미리 저장된 파일이 전달되는 웹 페이지
  - 요청을 받으면 처리과정 없이 클라이언트한테 보냄
  - 모든 사용자에게 동일한 정보를 표시한다.



- Dynamic web page(동적 웹 페이지)
  - 서버는 추가적인 처리 이후 클라이언트에게 응답을 보낸다.
  - 방문자와 상호작용해서 페이지 내용이 계속 다름
  - 서버 사이드 프로그래밍 언어가 사용되며 데이터 베이스와 상호작용이 이루어짐



### Framework

- 프로그래밍에서 특정 운영체제를 위한 응용프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- `웹 페이지 개발과정에서 겪는 어려움을 줄이는 것이 주 목적`(데이터베이스 연동, 템플릿 형태 표준, 코드 재사용 등등)



#### Framework Architecture

- MVC 디자인 패턴
- 프로그램 로직을 분리하여 시각적요소나 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 어플리케이션을 만들 수 있다.
- Django -> MTV Pattern

| MTV pattern                                              | MVC pattern |
| -------------------------------------------------------- | ----------- |
| Model : 데이터구조를 정의, 데이터베이스 기록 관리        | Model       |
| Template 파일의 구조나 레이아웃 정의, 실제 내용을 보여줌 | View        |
| View : HTTP 요청을 수신하고 반환, 필요한 데이터에 접근   | Controller  |



### Django

- Django 가상환경 생성

```bash
# 장고 설치
$ pip install django

# 프로젝트 생성
$ django-admin startproject firstpjt .

# django 서버 실행
$ python manage.py runserver
```

- .을 안붙이면 폴더안에 폴더가 생긴다.

- .을 붙이면 바로 하위폴더 생성

  
  
- 

#### 프로젝트 구조

1.  `__init__.py` : 하나의 Python 패키지로 다루도록 한다.

2. `asgi.py` : Asynchronous Server Gateway Interface, 비동기식 웹 서버와 연결 및 소통하는 것을 도움

3. `settings.py` : 모든 설정

4. `urls.py` : 사이트 url과 view의 연결을 지정한다.

5. `wsgi.py` : django 애플리케이션이 웹서버와 연결 및 소통하는것을 도운다.

6. `manage.py` : Django 프로젝트와 다양한 방법으로 상호작용 하는 유틸리티

   ```bash
   $ python manage.py command option
   ex) python manage.py startapp articles
   ```

   - 어플리케이션 명은 복수형을 권장한다.



#### Aplication 생성

```bash
$ python manage.py startapp articlass
articlass = 이름
```



#### Application 구조

1. `admin.py`: 관리자용 페이지 설정
2. `apps.py` : 앱의 정보 작성
3. `models.py` : 앱에서 사용하는 Model을 정의
4. `test.py` : 프로젝트 테스트 코드 작성
5. `view.py` : view 함수들이 정의



- 프로젝트는 여러 앱이 포함될 수 있고 앱은 여러 프로젝트에 있을 수 있다.
- 앱은 실제 요청을 처리하고 페이지를 보여주는 역할을 담당



#### 앱 등록

- 프로젝트 앱을 사용하기 위해서는 INSTALLED_APPS 리스트에 추가해야 한다.
- INSTALLED_APPS
  - Django installation에 활성화 된 모든 앱을 지정하는 목록
  - 주의사항
    - 반드시 생성 후 등록
    - 등록하고 생성하면 앱이 생성되지 않는다.
    - 순서를 지키는 것을 권장한다.



- URLS

  - HTTP 요청을 알맞은 view로 전달한다.

    ```python
    from articles import views
    
    urlpatterns = [
        path('index/', views.index),
    ]
    # 뒤에는 /를 붙어야하고 끝날때도 , 을 붙여야 한다.
    ```



- Views

  - HTTP 요청을 수신하고 응답을 반환하는 함수

  - Model을 통해 필요 데이터에 접근

    ```python
    # views.py
    from django.shortcuts import render
    
    def index(request):
        return render(request, 'index.html')
    
    # Model을 통해 요청에 맞는 필요 데이터에 접근한다.
    # Template에 HTTP 응답 서식을 맡긴다.
    ```



- Templates
  - 실제 내용을 보여주는데 사용하는 파일
  - 파일의 구조나 레이아웃을 정의해준다.
  - 기본 경로값은 app폴더 안의 templates 폴더로 지정



### Template

- 데이터 표현을 제어하는 도구



#### Django Template Language

- django template에서 사용하는 built-in template 시스템
- 조건, 반복, 치환, 필터등의 기능을 제공한다.
- Python이 HTML에 포함된 것이 아니며 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- 파이썬 코드로는 실행이 되지 않는다.



#### DTL Syntax

1. `{{ variable }}`

- render()을 사용하여 views.py에서 정의한 것을 template 파일로 넘겨 사용한다.
- 변수명은 숫자와 밑줄의 조합으로 구성



2. Filters -> `{{ variable|filter }}`

- ex) `{{ name|lower }}`name 변수를 소문자로 출력



3. Tags -> `{% tag %}`

- 출력 테스트를 만들거나 반복, 논리 수행
- ex) `{% if %} {% end if %}`



4. Comments -> `{# #}`

- 주석라인 표현
- 여러줄 주석은 `{% comment %} {% endcomment %}`



#### 코드 작성 순서

1. urls.py
2. views.py
3. templates



#### Template inheritance (상속)

- 템플릿 상속은 코드 재사용이 목적이다.
- 상속을 하면 공통 요소를 포함하고 하위 템플릿이 재정의 할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿 만들기 가능
- 두개는 상속이 안된다. 최상단이기 때문에 한개만 상속이 가능하다.



```
{% extend '' %}
자식 템플릿이 부모 템플릿을 확장한다.
반드시 최상단 작성 필요

{% block content %} {% endblock %}
하위 템플릿에서 재지정 할 수 있는 블록을 정의
하위템플릿이 채우는 공간
```

- Settings.py에 DIR은 app_name/templates 디렉토리 외 템플릿 추가 경로 설정할 때 쓰인다.



### HTML FORM

- HTML form element
  - 웹에서 사용자 정보를 입력하는 여러 방식을 제공하고 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
  - 속성
    - action : 입력 데이터가 전송될 URL 지정
    - method : 입력 데이터 전달 방식 지정
- HTML input element
  - 사용자로부터 데이터를 입력 받기 위해 사용
  - type속성에 따라 동작 방식이 다름
  - GET/POST 방식으로 서버에 전달하는 파라미터 형태로 전달
- HTTP request method - "GET"
  - 서버로부터 정보를 조회하는데 사용
  - 데이터 가져올때만 사용
  - 전송할 때 body가 아닌 query string parameters로 전송



### URL

#### Variable Routing

- URL주소를 변수로 사용하는 것
- URL 일부를 변수로 지정하여 view 함수의 인자로 넘기기 가능
- 변수 값에 따라 하나의 path에 여러 페이지를 연결 시키기 가능



#### URL Path converters

- str
  - '/'을 제외하고 비어 있지 않은 모든 문자열 매치
- int
  - 0 또는 양의 정수와 매치
- slug
  - 아스키 코드 문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 문자열과 매치



#### App URL mapping

- app의 view 함수가 많아지면 사용하는 path가 많아지고 app또한 많아지면 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않다.

  





















python manage.py startapp (name) -> urls.py 에서 등록

showmigrations - python manage.py showmigrations -> 상태확인



추가를 하면 설계도를 만들어줘야한다.

python manage.py makemigrations -> 선택지 2개를 줌, 여기서 키값을 넣던지 나가서 넣던지

1번은 알아서 적용해주고 2번은 알아서 적용해라



앞에있던 설계도 기준으로 2번 설계도가 만들어진다.

python manage.py migrate를 통해서 해준다.



auto_now_add는 최초생성일자라 created_at

auto_now 는 최종수정일자라 updated에 썼다

 

migrate하면 x표시 나오고 안했을경우 비어있음











migrations 기반으로 database가 생성된다

적용하는 과정은 orm이 해준다.



sqlmigrate

python manage.py sqlmigrate articles 0001



편리하게 보기 python manage.py shell_plus



장고는 데이터베이스에서 삭제된 것을 재사용하지 않는다.

1,2,3 사용인데 1번을 삭제하고 새로 생성하면 4번이 생성된다.
