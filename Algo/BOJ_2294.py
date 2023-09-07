N, K = map(int, input().split())
coin_lst = []

for _ in range(N):
    coin_lst.append(int(input()))

# 최댓값보다 위
dp = [10001] * (K+1)
dp[0] = 0

for i in coin_lst:
    for j in range(i, K+1):
        dp[j] = min(dp[j], dp[j-i]+1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
