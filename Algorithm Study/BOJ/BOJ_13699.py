N = int(input())

answer = [1]
# 전체 돌기
for i in range(1, N+1):
    number = 0
    # 점화식에 따른 계산하기
    for j in range(i):
        number += answer[j] * answer[i-j-1]
    answer.append(number)

print(answer[N])