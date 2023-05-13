graph = [list(map(int, input().split())) for _ in range(19)]

dir = [(0, 1), (1, 0), (-1, 1), (1, 1)]

def check(x, y):
    for d in dir:
        nx, ny = x + d[0], y + d[1]
        cnt = 1

        # 오목인지 계속 확인
        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == graph[x][y]:
            cnt += 1
            nx += d[0]
            ny += d[1]

            # 5개일때
            if cnt == 5:
                # 6목방지
                if not (0<=nx<19 and 0 <= ny < 19 and graph[x][y] == graph[nx][ny]):
                    # 6목방지
                    if not (0<=x-d[0]<19 and 0<=y-d[1]<19 and graph[x-d[0]][y-d[1]] == graph[x][y]):
                        print(graph[x][y])
                        print(x+1, y+1)
                        exit(0)
                    else:
                        break
                else:
                    break

for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            check(i, j)

print(0)  # 승부가 나지 않았을 때