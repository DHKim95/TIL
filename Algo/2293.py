N, K = map(int, input().split())

dp = [0 for _ in range(K+1)]
dp[0] = 1
coin_lst = []

for _ in range(N):
    coin_lst.append(int(input()))

for coin in coin_lst:
    for i in range(coin, K+1):
        # i-coin에서 coin을 추가하면 그 방법 수
        dp[i] += dp[i-coin]
    # print(dp)

print(dp[K])