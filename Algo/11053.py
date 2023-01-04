N = int(input())

arr = list(map(int, input().split()))
dp = [1] * N

# 현재에서 전에 수들 보면서 가장 높은 숫자 찾기 -> 높은거만 해야됨
for now in range(N):
    for j in range(now):
        if arr[now] > arr[j]:
            dp[now] = max(dp[j]+1, dp[now])

# 가장 큰 수
print(max(dp))