from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = 1

        while queue:
            x, y = queue.popleft()

            if (x, y) == (N - 1, M - 1):
                return visited[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return -1

    visited = [[0] * M for _ in range(N)]
    answer = BFS(0, 0)

    return answer