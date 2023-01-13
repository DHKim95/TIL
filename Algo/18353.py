N = int(input())

arr = list(map(int, input().split()))
dp = [1] * N

# 돌면서 최소값 찾기
for i in range(N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(N - max(dp))