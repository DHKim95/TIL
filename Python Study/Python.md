## Python

Python 모르는 것 공부하기



### Python 특징

-----------------------

 - 인터프리터 언어 -> 한줄씩 바로 실행 가능 -> 대화형환경
 - 객체 지향 -> 전부 객체로 이루어짐
 - 동적 타이핑 -> 별도 타입 지정 필요 없음



###  문법 공부

------

1. 주석

   ```python
   # 으로 주석 표현
   
   # print("ABCD")
   print("ABCD")
   
   """
   여기는 주석입니다.
   """
   print("여기는 주석이 아닙니다.")
   ```

2. 변수

   - type(문자) : 할당된 타입

   ```python
   name = "Hello"
   type(name)
   ```

3.  식별자

   - 첫 글자에는 숫자 불가 , 대소문자 구별

   - 식별자 이름은 영문, 숫자, 언더바(_)로 구성

   - 예약어는 사용불가 (충돌이 일어남)

     ```python
     # 예약어 확인
     import keyword
     print(keyword.kwlist)
     ```

4.  진수 표현

   ```python
   # 2진수
   0b11 # -> 3
   # 8진수
   0o10 # -> 8
   # 16진수
   0x64 # -> 100
   ```

5. 부동소수점 연산

   ```python
   # 왼쪽과 오른쪽 값이 다르다
   0.1 * 3 - 0.3 != 0
   
   # 해결법
   import math
   math.isclose(0.1*3, 0.3) # -> True
   ```

6. 논리연산자

   ```python
   # and 연산인 경우 뒤를 확인 후 반환
   # or 연산인 경우 앞에가 참이면 바로 반환
   print(2 and 4) # -> 2
   print(2 and 0) # -> 0
   print(0 and 2) # -> 0
   print(0 and 0) # -> 0
   
   print(4 or 2) # -> 4
   print(2 or 0) # -> 2
   print(0 or 2) # -> 2
   print(0 or 0) # -> 0
   ```

   
