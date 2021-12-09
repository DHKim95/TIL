def virus(x, y):
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if block[nx][ny] == 0:
                block[nx][ny] = 2
                virus(nx, ny)

def score():
    score = 0
    for i in range(N):
        for j in range(M):
            if block[i][j] == 0:
                score += 1
    return score

def DFS(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                block[i][j] = graph[i][j]

        for i in range(N):
            for j in range(M):
                if block[i][j] == 2:
                    virus(i,j)

        result = max(result, score())
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                DFS(count)
                graph[i][j] = 0
                count -= 1

# N은 세로, M은 가로
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
block = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0 # 안전영역

DFS(0)
print(result)

