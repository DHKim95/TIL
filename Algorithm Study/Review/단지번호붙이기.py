from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

cnt_lst = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt_lst.append(BFS(i,j))

cnt_lst.sort()
print(len(cnt_lst))
for i in cnt_lst:
    print(i)