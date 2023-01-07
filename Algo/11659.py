import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]

# print(dp)
for _ in range(M):
    a, b = map(int, input().split())

    print(dp[b] - dp[a-1])