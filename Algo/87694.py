from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append([characterX * 2, characterY * 2])
    visited[characterX * 2][characterY * 2] = 0

    while queue:
        x, y = queue.popleft()
        # 도착점
        if x == itemX * 2 and y == itemY * 2:
            answer = (visited[x][y] + 1) // 2
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return answer