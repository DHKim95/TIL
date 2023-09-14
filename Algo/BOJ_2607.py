N = int(input())
target = list(input())
answer = 0

for _ in range(N-1):
    word = input()
    compare_word = target[:]
    sub_cnt = 0

    for alpha in word:
        # 비슷한 단어 체크
        if alpha in compare_word:
            compare_word.remove(alpha)
        else:
            sub_cnt += 1

    if sub_cnt <= 1 and len(compare_word) <= 1:
        answer += 1

print(answer)