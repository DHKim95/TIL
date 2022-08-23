from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
H, W, sr, sc, fr, fc = map(int, input().split())

# 벽 미리 체크
wall_lst = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            wall_lst.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽이 없는지 체크하기
def block_check(x, y):
    for i, j in wall_lst:
        if x <= i < x+H and y <= j < y+W:
            return False
    return True

def BFS():
    queue = deque()
    # 시작점, 횟수
    queue.append((sr-1, sc-1, 0))

    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = 1

        if (x == fr-1) and (y == fc-1):
            print(cnt)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nx + H - 1 < N and 0 <= ny + W - 1 < M:
                if visited[nx][ny] == 0:
                    if block_check(nx, ny) == True:
                        visited[nx][ny] = 1
                        queue.append((nx, ny, cnt+1))


    # 갈수없는곳
    print(-1)
    return

BFS()