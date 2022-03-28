N = int(input())

dp = [-1] * (N+1)
dp[0] = 0
dp[1] = 1

for n in range(2, N+1):
    # 최대값 설정
    dp[n] = 987654321
    # 제곱수 까지 확인
    for k in range(1, int(n ** 0.5) + 1):
        # 자신의 수보다 작은 제곱수를 뺀것에 최소를 구하고 + 1
        dp[n] = min(dp[n], dp[n - k ** 2] + 1)

print(dp[N])