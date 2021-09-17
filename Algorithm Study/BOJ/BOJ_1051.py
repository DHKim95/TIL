N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

answer = 0
check = min(N, M)

for i in range(N):
    for j in range(M):
        for k in range(check):
            if ((i+k) < N) and ((j+k) < M) and (graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]):
                answer = max(answer, (k+1)**2)

print(answer)