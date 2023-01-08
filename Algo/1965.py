N = int(input())

arr = list(map(int, input().split()))
dp = [1] * N

for now in range(N):
    for i in range(now):
        if arr[now] > arr[i]:
            dp[now] = max(dp[i]+1, dp[now])

# print(dp)
print(max(dp))