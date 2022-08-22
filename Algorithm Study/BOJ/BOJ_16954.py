from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dy = [0, 0, -1, 1, -1, 1, -1, 1, 0]

def BFS(x, y):
    queue = deque()
    queue.append((x ,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        # 오른쪽 위 도착하면 끝
        if graph[x][y] == '#':
            continue

        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
                continue

            if graph[nx][ny] == '#':
                continue

            if nx == 0:
                return True

            # 한칸 당겨지는것 고려
            if visited[nx-1][ny] == 0:
                visited[nx-1][ny] = 1
                queue.append((nx-1, ny))

    return False


graph = deque(list(input()) for _ in range(8))
visited = [[0] * 8 for _ in range(8)]

answer = BFS(7, 0)
if answer == True:
    print(1)
else:
    print(0)