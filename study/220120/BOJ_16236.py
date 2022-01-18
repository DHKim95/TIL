from collections import deque

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

baby_x, baby_y = 0, 0
baby_size = 2

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            baby_x, baby_y = i, j
            graph[baby_x][baby_y] = 0


def BFS():
    distance = [[-1] * N for _ in range(N)]
    queue = deque([(baby_x, baby_y)])
    distance[baby_x][baby_y] = 0

    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N:
                if distance[nx][ny] == -1 and graph[nx][ny] <= baby_size:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    return distance

result = 0
shark_eat = 0

def shark_find(dis):
    x, y = 0, 0
    min_distance = 987654321
    for i in range(N):
        for j in range(N):
            if dis[i][j] != -1 and graph[i][j] >= 1 and graph[i][j] < baby_size:
                if min_distance > dis[i][j]:
                    x, y = i, j
                    min_distance = dis[i][j]

    if min_distance == 987654321:
        return None
    else:
        return x, y, min_distance

while True:
    lst = shark_find(BFS())
    if lst == None:
        print(result)
        break
    else:
        now_x, now_y = lst[0], lst[1]
        result += lst[2]
        graph[now_x][now_y] = 0
        shark_eat += 1

        if shark_eat >= baby_size:
            baby_size += 1
            shark_eat = 0
