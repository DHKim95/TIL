from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[999999999] * N for _ in range(N)]

    queue = deque()
    visited[0][0] = 0
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 범위 안에 갈 수 있으면
            if 0 <= nx < N and 0 <= ny < N:
                # 이번꺼와 전에꺼 차이 계산
                if graph[nx][ny] > graph[x][y]:
                    diff = graph[nx][ny] - graph[x][y]
                # 차이가 없다면 0 고정
                else:
                    diff = 0
                min_value = visited[x][y] + 1 + diff
                if visited[nx][ny] > min_value:
                    visited[nx][ny] = min_value
                    queue.append((nx, ny))

    print("#{} {}".format(tc+1, visited[N-1][N-1]))