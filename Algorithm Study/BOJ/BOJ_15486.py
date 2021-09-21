import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []

dp = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N):
    # 상담 날짜가 전체 일수보다 작야아함
    if T[i] <= N - i:
        # r금액이 더 많은걸 찾는다.
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])

    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N])