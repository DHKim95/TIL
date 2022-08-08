N = int(input())

graph1 = list(input() for _ in range(N))
graph2 = list(input() for _ in range(N))
answer = [['.'] * N for _ in range(N)]

dx = [-1, -1, -1, 0,0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if graph1[i][j] == '.' and graph2[i][j] == 'x':
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if graph1[nx][ny] == '*':
                    cnt += 1

            answer[i][j] = cnt

        if graph1[i][j] == '*' and graph2[i][j] == 'x':
            for a in range(N):
                for b in range(N):
                    if graph1[a][b] == '*':
                        answer[a][b] = '*'

for i in range(N):
    for j in range(N):
        print(answer[i][j], end='')
    print()