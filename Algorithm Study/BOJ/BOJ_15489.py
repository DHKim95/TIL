R, C, W = map(int, input().split())

# 미리 만들기
dp = [[0] * 31 for _ in range(31)]

for i in range(len(dp)):
    dp[0][i] = 1

# 양 삼각형 1로 만들고 더하기
for i in range(len(dp)):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
hap, cnt = 0, 0
for i in range(R - 1, R + W - 1):
    for j in range(C - 1, C + cnt):
        hap += dp[i][j]
    cnt += 1
print(hap)
