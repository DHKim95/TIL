from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
zero = [[0] * M for _ in range(N)] # 빈땅 그룹 체크
answer = [[0] * M for _ in range(N)] # 정답라인

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
g_num = 1
g_dict = {}

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    check = 1
    while queue:
        x, y = queue.popleft()
        zero[x][y] = g_num
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                check += 1

    return check

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == 0:
            cnt = BFS(i, j)
            g_dict[g_num] = cnt
            g_num += 1

# 벽부수고 개수 적기
def total_cnt(x, y):
    num_set = set()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not zero[nx][ny]:
            continue
        num_set.add(zero[nx][ny])

    # 10으로 나누어주래
    idx_cnt = 1
    for k in num_set:
        idx_cnt += g_dict[k]
        idx_cnt %= 10
    return idx_cnt


for i in range(N):
    for j in range(M):
        if graph[i][j]:
            answer[i][j] = total_cnt(i, j)

for i in range(N):
    for j in range(M):
        print(answer[i][j], end='')
    print()