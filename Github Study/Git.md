# Git

Github 공부용



## Git 설치







## Git 기본명령어

- git 로컬 저장소 생성하기

  ->  VSCode 터미널에서 해당폴더로 접근 후 생성 가능

  - git init 명령어를 실행하면 새로운 저장소 생성

  ```
  $ git init
  ```

  - .git 폴더가 생성되며 프로젝트 관리 파일이 들어 있음



- git 상태 확인

  -  현재 저장소 내 파일들을 확인해 볼 수 있다.

  ```
  $ git status
  ```



- Index에 파일 추가 (git add)

  ```
  $ git add [파일명] 또는 git add . (해당 폴더 한번에 올리기)
  ```

  - 이력관리 대상에 포함되지 않으면 Untracked file이라고 표시

  - 인덱스에 포함된 파일은 Changes to be commited 라고 표시

  - 인덱스에 추가된 파일을 제외하려면 

    ```
    $ git rm --cached [파일명]
    ```
    
    

- git 변경사항 확정 

  ```t
  $ git commit -m "메시지"
  ```



- git commit 작성자(설정)

  ```
  $ git config --global user.email [github 이메일]
  $ git config --global user.name [github 닉네임]
  
  # git 설정 확인
  $ git config --global -l
  ```



- 원격 저장소 등록

  ```
  $ git remote and origin https://github.com/[본인 github 닉네임]/TIL.git
  ```



- 원격 저장소 업로드

  ```
  $ git push 또는 git push origin [브랜치명]
  ```

  

