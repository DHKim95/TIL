N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

max_value = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def DFS(x, y, idx, total):
    global answer
    # 남은게 answer보다 작으면 패스
    if answer >= total + max_value * (4-idx):
        return
    # 4칸일경우
    if idx == 4:
        answer = max(answer, total)
        return
    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # ㅗ자 모양
                if idx == 2:
                    visited[nx][ny] = 1
                    DFS(x, y, idx+1, total + graph[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                DFS(nx, ny, idx+1, total+graph[nx][ny])
                visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(i, j, 1, graph[i][j])
        visited[i][j] = 0

print(answer)