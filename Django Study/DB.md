# 데이터베이스(DB)

- 데이터베이스는 체계화된 데이터 모임이다.
- 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체



- 데이터 베이스로 얻는 장점
  - 데이터 중복 최소화
  - 데이터 무결성(정확성)
  - 데이터 일관성
  - 데이터 독립성
  - 데이터 표준화
  - 데이터 보안 유지



## 관계형 데이터베이스

- Relational Database

- key와 value들의 간단한 관계로 표를 정리한 데이터 베이스

- 스키마 : 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적 명세를 기술한 것

  | column  | datatype |
  | :-----: | :------: |
  |   id    |   INT    |
  |  name   |   TEXT   |
  | address |   TEXT   |



- 테이블 : 열과 행의 값을 사용해 조작된 데이터 요소들의 집합

  |  id  |  name  | address |
  | :--: | :----: | :-----: |
  |  1   | 홍길동 |  서울   |
  |  2   | 김길동 |  부산   |

  

- 열 : 각 열에는 고유한 데이터 형식이 지정
- 행 : 실제 데이터가 저장되는 형태
- 기본 키(Primary Key) : 각 행의 고유 값 -> 위에서 id
  - 반드시 설정해야 하며 데이터베이스 관리시 활용됨



- 관계형 데이터베이스 관리 시스템(RDBMS)
  - MySQL
  - SQLite
  - PostgreSQL
  - ORACLE
  - MS SQL



## SQL
- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 **프로그래밍 언어**

  - 데이터베이스 스키마 생성 및 수정
  - 자료의 검색 및 관리
  - 데이터베이스 객체 접근 조정 관리



- SQL 분류

  |          분류          |                          개념                          |             예시             |
  | :--------------------: | :----------------------------------------------------: | :--------------------------: |
  | DDL - 데이터 정의 언어 |    관계형 데이터베이스 구조를 정의하기 위한 명령어     |      CREATE DROP ALTER       |
  | DML - 데이터 조작 언어 |  데이터를 저장, 조회, 수정, 삭제등을 하기 위한 명령어  | INSERT SELECT UPDATE DELETE  |
  | DCL - 데이터 제어 언어 | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어 | GRANT REVOKE COMMIT ROLLBACK |



- DML
  - INSERT : 새로운 데이터 삽입
  - SELECT : 데이터 조회
  - UPDATE : 데이터 갱신
  - DELETE : 데이터 삭제 



- 데이터베이스 생성하기

  ```bash
  $ sqlite3 tutorial.sqlite3
  sqlit> .database
  # .은 프로그램 실행 -> 데이터베이스 실행
  ```



- csv 파일을 table로 만들기

  ```sqlite
  .mode csv
  .import [파일명].csv [테이블명]
  .tables
  -- 테이블 목록이 출력된다.
  ```

  

- 터미널 view 변경하기

  ```sqlite
  .headers on
  .mode column
  
  -- 위 두 명령어를 실행하면 조금 더 보기 편한다.
  ```



- 테이블 생성 및 조회

  - SQL은 세미콜론을 반드시 입력해줘야 문장이 끝났다고 생각해준다
  - 대문자 소문자 상관은 없지만 가능하면 대문자로 쓴다. -> 가독성을 높이기 위해
  - 꼭 필요한 정보를 넣어야 한다면 공백으로 비우면 안된다.

  ```sqlite
  CREATE TABLE example (
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT
  );
  -- 반드시 ;로 끝내줘야 한다.
  
  -- 테이블 확인
  .tables
  -- 스키마 조회
  .schema [테이블명]
  
  -- 공백 없애기
  CREATE TABLE example (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  address TEXT NOT NULL
  );
  ```



- 테이블 삭제

  ```sqlite
  DROP TABLE [테이블명]
  ```



#### CREATE

- INSERT

  - 모든 열에 데이터가 있는 경우 Column을 명시하지 않아도 된다.
  - id를 포함한 모든 value를 작성해주어야 한다.
  - 각 value에 맞는 column들을 작성해주어야 한다.

  ```sqlite
  -- INSERT는 특정 테이블에 레코드(행)을 삽입한다.
  INSERT INTO [테이블명] (컬럼1, 컬럼2 .....) VALUES (값1, 값2 ...)
  
  -- SQLite는 PRIMARY KEY속성을 작성하지 않으면 값이 자동으로 증가하는 pk옵션을 가진 rowid를 정의
  SELECT rowid, * FROM [테이블명]
  ```



#### READ

- SELECT
  - 테이블에서 데이터를 조회한다.
  - 가장 복잡한 문이며 다양한것들과 함께 사용한다.
    - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY

- LIMIT
  - 쿼리에서 반환되는 행 수를 제한한다.
  - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용한다.

- WHERE
  - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정한다.
- DINSTINCT
  - 조회 결과에서 중복 행을 제거한다.
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성한다.

```sqlite
-- 특정 컬럼 조회하기
SELECT 컬럼1, 컬럼2, ... FROM [테이블명];

-- 원하는 수 만큼 조회하기
SELECT 컬럼1, 컬럼2, ... FROM [테이블명] LIMIT 숫자;

-- 세번째에 있는 하나만 조회
-- 인덱스는 0번부터 시작
SELECT 컬럼1, 컬럼2, ... FROM [테이블명] LIMIT 1 OFFSET 2;

-- 조건 확인하여 조회
SELECT 컬럼1, 컬럼2, ... FROM [테이블명] WHERE 조건;

-- 중복없이 가져오기
SELECT DISTINCT 컬럼 FROM [테이블명];
```



#### DELETE

- DELETE

  - 테이블에서 행을 제거한다.
  - 중복 불가능한 rowid 기준으로 삭제하는 것이 좋다.
  - SQLite는 기본적으로 id를 재사용 한다.

  ```sqlite
  DELETE FROM [테이블 명] WHERE 조건;
  ```

- 재사용 방지

  ```sqlite
  CREATE TABLE [테이블명] (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  )
  ```

  

#### UPDATE

- UPDATE

  - 기존 행의 데이터를 수정한다.
  - 중복 불가능한 rowid를 기준으로 수정하는 것이 좋다.

  ```sqlite
  UPDATE [테이블명] SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;
  ```

  

#### SQL Aggregate Functions

- SQLite aggregate functions

  - COUNT : 그룹의 항목 수를 가져옴

    ```sqlite
    SELECT COUNT(컬럼) FROM [테이블명]
    ```

  - AVG : 값 집합의 평균을 계산한다.

    ```sqlite
    SELECT AVG(컬럼) FROM [테이블명]
    ```

  - MAX : 그룹에 있는 모든 값의 최대값을 가져온다.

    ```sqlite
    SELECT MAX(컬럼) FROM [테이블명]
    ```

  - MIN : 그룹에 있는 모든 값의 최소값을 가져온다.

    ```sqlite
    SELECT MIN(컬럼) FROM [테이블명]
    ```

  - SUM : 모든 값의 합을 계산한다.

    ```sqlite
    SELECT SUM(컬럼) FROM [테이블명]
    ```



#### LIKE

- 패턴 일치를 기반으로 데이터를 조회하는 방법

- 2개의 Wildcard를 제공

  - % : 0개 이상의 문자, 문자열이 있을수도 있고 없을 수도 있다.

  - _ : 임의의 단일 문자, 반드시 한개의 문자가 존재해야 한다.

    |  와일드카드패턴  |                     의미                      |
    | :--------------: | :-------------------------------------------: |
    |        2%        |                2로 시작하는 값                |
    |        %2        |                 2로 끝나는 값                 |
    |       %2%        |                2가 들어가는 값                |
    |       _2%        | 아무 값이 하나 있고 두번 째가 2로 시작하는 값 |
    |       1___       |          1로 시작하고 총 4자리인 값           |
    | 2\_%\_% / 2\_\_% |        2로 시작하고 적어도 3자리인 값         |

    ```sqlite
    -- ex)
    SELECT * FROM [테이블명] WHERE age LIKE '3_';
    ```



##### ORDER BY

- 조회 결과 집합을 정렬한다.

- SELECT 문에 추가한다.

- 오름차순과 내림차순이 존재한다.

  ```sqlite
  -- 오름차순
  SELECT * FROM [테이블명] ORDER BY 컬럼 ASC;
  -- 내림차순
  SELECT * FROM [테이블명] ORDER BY 컬럼 DESC;
  ```



#### GROUP BY

- 행 집합에서 요약 행을 만듬

- WHERE 절 뒤에 작성을 해야한다.

- 지정된 기준에 따라 행 세트를 그룹으로 결합하고 요약하는 상황에 자주 쓰인다.

- AS를 활용하여 컬럼명을 바꿔서 조회도 가능하다.

  ```sqlite
  SELECT [컬럼] FROM [테이블명] GROUP BY [컬럼]
  ```

  

#### ALTER TABLE

- 테이블 이름 변경이 가능하다.

  ```sqlite
  ALTER TABLE [기존테이블명] RENAME TO [새로운 테이블 명]
  ```

- 테이블에 새로운 컬럼을 추가할 수 있다.

  - 테이블에 있던 레코드들은 새로 추가할 필드에 대한 정보가 없기 때문에 NOT NULL은 추가가 불가능하다.

  ```sqlite
  ALTER TABLE [테이블명] ADD COLUMN [컬럼이름][데이터타입]
  ```

- 컬럼 이름 수정이 가능하다.





## SQL & ORM

- 실행

  ```bash
  $ python manage.py shell_plus
  ```



- 모든 User 레코드 조회

  - ORM

    ```shell
    User.objects.all()
    ```

  - SQL

    ```sqlite
    SELECT * FROM users_user;
    ```

    

- CREATE

  - ORM

    ```sqlite
    User.objects.create(
    first_name='도훈',
    last_name='김',
    age=27,
    country='경상남도',
    phone='010-1111-2222',
    balance=100)
    ```

- Read

  - ORM

    ```sqlite
    User.objects.get(pk=100)
    ```

  - SQL

    ```sqlite
    SELECT * FROM users_user WHERE id=100

- Update

  - ORM

    ```sqlite
    user = User.objects.get(pk=100)
    user.last_name='김'
    user.save()
    user.last_name
    ```

  - SQL

    ```sqlite
    UPDATE users_user SET last_name='김' WHERE id = 100;
    ```

- DELETE

  - ORM

    ```sqlite
    User.objects.get(pk=100).delete
    ```

  - SQL

    ```sqlite
    DELETE FROM users_user WHERE id=100;
    ```

    
