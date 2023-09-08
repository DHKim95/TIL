N = int(input())

arr = list(map(int, input().split()))
dp = [0] * (N+1)
max_value = 0

for i in range(N):
    idx = arr[i]
    # 가장 긴 배열 수 구하기
    dp[idx] = dp[idx-1] + 1
    # print(i, dp)
    max_value = max(dp[idx], dp[idx-1] + 1)

print(N - max(dp))

# 3, 2 3 1 <<