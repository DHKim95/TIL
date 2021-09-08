import sys
sys.setrecursionlimit(100000)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    # 방문처리
    visited[x][y] = 1
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위안에 들어오고 방문안했으면 방문
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx,ny)

T = int(input()) # 테스트 케이스
for tc in range(T):
    M, N, K = map(int, input().split()) # M은 가로, N은 세로, K는 위치
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                answer += 1

    print(answer)