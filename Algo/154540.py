from collections import deque

def solution(maps):
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS(x, y):
        visited[x][y] = 1
        queue = deque()
        queue.append((x, y))
        cnt = int(maps[x][y])

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= H or ny >= V:
                    continue

                if maps[nx][ny] == 'X' or visited[nx][ny] == 1:
                    continue

                if not maps[nx][ny] == 'X' and visited[nx][ny] == 0:
                    cnt += int(maps[nx][ny])
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

        return cnt

    H = len(maps)
    V = len(maps[0])

    visited = [[0] * V for _ in range(H)]
    for i in range(H):
        for j in range(V):
            if not maps[i][j] == 'X' and visited[i][j] == 0:
                answer.append(BFS(i, j))

    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))