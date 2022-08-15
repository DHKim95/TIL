# Github Mirror

1. 프로젝트 원본을 그대로 사용하거나 fork해서 사용
2. git clone 하기
    
    ```bash
    $ git clone --mirror 복사할주소 --depth 1
    # depth를 늘리면 용량을 나눠서 가져갈 수 있다.
    $ cd 클론한폴더.git
    $ git fetch --unshallow
    ```
    
3. BFG-Repo-Cleaner 설치
    
    [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)
    
4. BFG 알집 파일을 클론한 폴더와 같은 위치에 위치시키기
5. 내용에 맞게 명령어 수행
    
    ```bash
    $ cd .;.
    $ java -jar bfg-1.14.0.jar --strip-biggest-blobs 100 --no-blob-protection 클론한파일.git
    $ cd 클론한파일.git
    $ git reflog expire --expire=now --all && git gc --prune=now --aggressive
    $ git push
    $ git push --mirror 깃헙주소
    ```