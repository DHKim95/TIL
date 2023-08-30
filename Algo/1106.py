C, N = map(int, input().split())
INF = int(1e9)

graph = [list(map(int, input().split())) for _ in range(N)]
dp = [0] + [INF] * (C + 100)

for cost, customer in graph:
    for now in range(customer, C+101):
        dp[now] = min(dp[now], dp[now - customer] + cost)

print(min(dp[C:C+101]))