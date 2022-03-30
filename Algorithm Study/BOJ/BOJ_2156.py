N = int(input())

wine = [int(input()) for _ in range(N)]

dp = [0, wine[0]]
if N > 1:
    dp.append(wine[0] + wine[1])

for i in range(3, N+1):
    case1 = wine[i-1] + dp[i-2] # 이번꺼먹고 이전 포도주 안먹기
    case2 = wine[i-1] + wine[i-2] + dp[i-3] # 이번꺼 먹고 이전꺼 먹기
    case3 = dp[i-1] # 이번 포도주 안먹기
    count = max(case1, case2, case3)

    dp.append(count)

print(dp[N])