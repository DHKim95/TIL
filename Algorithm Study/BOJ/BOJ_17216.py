N = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

for i in range(N):
    for j in range(i):
        # 큰것들 찾기
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))