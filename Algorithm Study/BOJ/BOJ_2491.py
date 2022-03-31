N = int(input())

arr = list(map(int, input().split()))
dp = [1] * N
dp2 = [1] * N

for i in range(1, N):
    # 현재꺼가 전보다 작을 때
    if arr[i] <= arr[i-1]:
        dp[i] = max(dp[i], dp[i-1] + 1)
    # 현재가 전보다 클 때
    if arr[i] >= arr[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1] + 1)

print(max(max(dp), max(dp2)))