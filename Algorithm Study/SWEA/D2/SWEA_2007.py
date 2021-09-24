T = int(input())
for tc in range(T):
    word = input()
    # 최대 10글자
    for i in range(1, 10):
        # 똑같은 단어가 나오면 길이 반환
        if word[0:i] == word[i:i+i]:
            print("#{} {}".format(tc+1, i))
            break