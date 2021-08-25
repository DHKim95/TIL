N = int(input())
check_num = int(input())

number = N*N

graph = [[0] * N for _ in range(N)]

# 아래 오른쪽 위 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direction = 0
x, y = 0, 0

while True:
    graph[x][y] = number
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] != 0:
        direction += 1
        if direction == 4:
            direction = 0
        continue

    x, y = nx, ny
    number -= 1
    if number == 1:
        graph[x][y] = 1
        break

for i in range(N):
    for j in range(N):
        if graph[i][j] == check_num:
            check_x, check_y = i,j
        print(graph[i][j], end=' ')
    print()
print(check_x+1, check_y+1)