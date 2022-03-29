N = int(input())
arr = list(map(int, input().split()))

# 리스트
dp = [i for i in arr]

for i in range(N):
    # 현재까지 상승폭 보기
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))