import sys
import math

input = sys.stdin.readline
N = int(input())

dp = [0] * (N+1)

for i in range(1, (N+1)):
    dp[i] = i
    # 제곱수만 찾아서 다시 초기화
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[N])