T = int(input()) # 테스트 갯수
for i in range(T):
    words = "" 
    N = int(input()) # 몇개의 단어를 입력 받는지
    for j in range(N): # 단어를 입력받아서 문자열로 만들어준다
        a, b = map(str, input().split())
        words += a*int(b)

    cnt = 0 # 개수
    print(f"#{i+1}") # 테스트 번호 출력
    for word in range(len(words)): # 
        cnt += 1
        if (cnt % 10) == 0: # 10번째 문자열을 출력하면 출력하고 다음줄로 넘어간다.
            print(words[word])
        else:
            print(words[word],end='') # 10번째가 아니면 옆에다가 계속 붙여준다.
    print() # 마지막 방지 