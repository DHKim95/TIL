N = int(input())

arr = [0]
sub = list(map(int, input().split()))
arr += sub
# print(arr)

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], arr[j] + dp[i-j])

print(dp[N])