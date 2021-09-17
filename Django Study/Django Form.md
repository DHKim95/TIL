# 🀄Django Form

- Django는 반복코드를 줄여주어 작업을 쉽게 만들어준다.



## Django Form Class

- Django가 Form에 관련해서 처리해주는 작업
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리

- Form Class는 Django Form 관리 시스템의 핵심이다.



#### Form 선언

- App폴더안에 forms.py를 만들어주어야 한다.

-  model을 선언하는 것과 유사하며 같은 필드타입을 사용한다.

- forms 라이브러리에서 파생된 form 클래스를 상속 받는다.

  ```python
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField()
  ```

  

#### Form 사용

- 간단하게 form을 선언하여 사용할 수 있다.

  ```python
  # views.py
  
  def new(request):
      form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'new.html', context)
  ```



