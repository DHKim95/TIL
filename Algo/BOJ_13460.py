from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited = []
queue.append((rx, ry, bx, by, 1))
visited.append((rx, ry, bx, by))

def move_check(x, y, a, b):
    sub_cnt = 0
    while graph[x+a][y+b] != '#' and graph[x][y] != 'O':
        x += a
        y += b
        sub_cnt += 1

    return x, y, sub_cnt

def BFS():
    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        # 10회 초과시 탈출
        if cnt > 10:
            break

        for d in range(4):
            nrx, nry, r_cnt = move_check(rx, ry, dx[d], dy[d])
            nbx, nby, b_cnt = move_check(bx, by, dx[d], dy[d])

            # 파란공 구멍에 빠지면 패스
            if graph[nbx][nby] == 'O':
                continue

            # 빨간공빠지면 끝
            if graph[nrx][nry] == 'O':
                return cnt

            # 같을경우
            if nrx == nbx and nry == nby:
                if r_cnt > b_cnt:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            if (nrx, nry, nbx, nby) not in visited:
                queue.append((nrx, nry, nbx, nby, cnt+1))
                visited.append((nrx, nry, nbx, nby))
            
    return -1

print(BFS())