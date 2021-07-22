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
   - id() : 변수에 할당된 값의 고유 주소, 메모리주소

   ```python
   name = "Hello"
   type(name)
   ```

3. 식별자

   - 첫 글자에는 숫자 불가 , 대소문자 구별
   - 식별자 이름은 영문, 숫자, 언더바(_)로 구성
   - 예약어는 사용불가 (충돌이 일어남)

   ```python
   # 예약어 확인
   import keyword
   print(keyword.kwlist)
   ```

4. 진수 표현

   ```python
   # 2진수
   0b11 # -> 3
   # 8진수
   0o10 # -> 8
   # 16진수
   0x64 # -> 100
   ```

5.  복소수형(Complex)

   - 복소수는 j로 표현
   - type = Complex

   ```python
   # ex) 
   a = 4+j
   
   a.real # 실수 리턴
   a.image # 허수 리턴
   a.conjugate # 켤레복소수
   ```

6. 부동소수점 연산

   ```python
   # 왼쪽과 오른쪽 값이 다르다
   0.1 * 3 - 0.3 != 0
   
   # 해결법
   import math
   math.isclose(0.1*3, 0.3) # -> True
   ```

7. 논리연산자

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

8. 조건표현식

   ```python
   if score >= 60:
       result = "합격"
   else:
       result = "불합격"
       
   result = "합격" if score >= 60 else "불합격"
   ```

9. enumerate

   - index와 value를 같이 반환(알고리즘문제에서 자주 쓰임)

   ```python
   fruit = ['사과','바나나','수박']
   for index, value in enumerate(fruit):
   	print(index, value)
   ```

10. 정렬

   - sort와 sorted의 차이

   ```python
   lst = [5,2,3,4,1]
   # lst의 원본이 바뀐다.
   lst.sort()
   # 새로운 함수를 제시해준다.
   sort_lst = sorted(lst)
   ```

11. 문자 뒤집기

    - 다양한 방법 존재

    ```Python
    string = "Hello"
    
    1. string[::-1]
    
    2. "".join(reversed(string))
    
    3. for문
    reversed_string = ""
    for i in string:
        reverse_str = i + reversed_string
    ```

    

