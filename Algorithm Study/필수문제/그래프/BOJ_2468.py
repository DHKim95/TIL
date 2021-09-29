from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] > k:
                visited[nx][ny] = 1
                queue.append((nx, ny))

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 가장 높은 위치까지 돌린다.
for k in range(max(max(graph))):
    cnt = 0 # 영역의 개수
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:
                cnt += 1
                BFS(i,j)

    result = max(result, cnt)

print(result)