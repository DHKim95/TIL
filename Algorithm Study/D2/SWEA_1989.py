N = int(input()) # 테스트 케이스 갯수
for i in range(N):
    words = input() # 단어 입력
    check_word = "" # 뒤집을 단어
    for j in range(len(words)-1, -1, -1): #단어 뒤집어서 만들어주기
        check_word += words[j]
    if words == check_word: # 같으면 1반환
        print(f"#{i+1} 1")
    else: # 다르면 0반환
        print(f"#{i+1} 0")