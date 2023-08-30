import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
K = int(input())

dp = [[-1] * (M+1) for _ in range(N+2)]
dp[1][1] = 1 # 시작
INF = int(1e9 + 7)

# 구멍없애기
for _ in range(K):
    a, b = map(int, input().split())
    dp[a][b] = 0

# 사이드 없애기
for i in range(N+1):
    dp[i][0] = 0

for j in range(M+1):
    dp[0][j] = 0
    dp[N+1][j] = 0

def DFS(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    print(dp)
    x = DFS(i-1, j) + DFS(i, j-1)
    if j % 2:
        x += DFS(i-1, j-1)
    else:
        x += DFS(i+1, j-1)

    dp[i][j] = x % INF
    return dp[i][j]

print(DFS(N, M))
print(dp)