N = int(input())

graph = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 플로이드 워셜로 풀기
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited[i][j] = 1

max_value = 0
for num in visited:
    max_value = max(max_value, sum(num))

print(max_value)