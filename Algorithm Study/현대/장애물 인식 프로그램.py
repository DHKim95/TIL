from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위안에 들면
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    cnt_lst.append(cnt)

N = int(input())

graph = [list(map(int,input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt_lst = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == 1:
            BFS(i,j)

# 순서대로 정렬
cnt_lst.sort()
print(len(cnt_lst))
for i in cnt_lst:
    print(i)