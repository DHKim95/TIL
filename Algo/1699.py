import math

N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
    # 기본 1로 만들기
    dp[i] = i

    for j in range(1, int(math.sqrt(i))+1):
        # 돌고있는 수가 커버리면 셀필요없으니 컷
        # if j ** 2 > i:
        #     break
        dp[i] = min(dp[i], dp[i - (j**2)]+1)

print(dp[N])
