n = int(input())

time_lst = []
price_lst = []
dp = [0 for _ in range(n+1)]

for i in range(n):
    time, price = map(int, input().split())
    time_lst.append(time)
    price_lst.append(price)

for i in range(n-1, -1, -1):
    # 주어진 기한보다 넘어서게 되면
    if time_lst[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(price_lst[i] + dp[i + time_lst[i]], dp[i+1])

print(dp[0])

