from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    sub_cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 가장자리만 골라내기
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 0
                    sub_cnt += 1
    return sub_cnt

answer = []
time = 0
while True:
    cnt = BFS()
    answer.append(cnt)
    if cnt == 0:
        break
    time += 1

print(time)
print(answer[-2])