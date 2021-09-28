from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(i,j):
    square = 1 # 사각형 넓이
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1 # 방문처리

    while queue:
        x, y = queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                square += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return square # 사각형 넓이 개수 반환


M, N, K = map(int, input().split()) # M은 세로, N은 가로, K는 분리영역

graph = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2,M-y1):
        for j in range(x1,x2):
            graph[i][j] = 1

cnt = 0 # 영역 개수 세기
square_lst = [] # 영역 넓이 개수
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and visited[i][j] == 0:
            cnt += 1
            square_lst.append(BFS(i,j))

print(cnt)
square_lst.sort()
print(*square_lst)