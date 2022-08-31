N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

def DFS(x, y, cnt):
    global answer
    # 옆으로 움직이면서 하나씩 확인 가로 다하면 세로로감
    if y == M:
        x += 1
        y = 0

    # 세로가 끝나면 점수 계산
    if x == N:
        answer = max(answer, cnt)
        return

    # 확인하고 다시 되돌리기
    if visited[x][y] == 0:
        for i in range(4):
            a, b, c, d = shape[i]
            na, nb, nc, nd = x+a, y+b, x+c, y+d
            if 0 <= na < N and 0 <= nb < M and 0 <= nc < N and 0 <= nd < M and visited[na][nb] == 0 and visited[nc][nd] == 0:
                visited[na][nb] = 1
                visited[nc][nd] = 1
                visited[x][y] = 1
                DFS(x, y+1, cnt + graph[x][y] * 2 + graph[na][nb] + graph[nc][nd])
                visited[na][nb] = 0
                visited[nc][nd] = 0
                visited[x][y] = 0
    DFS(x, y+1, cnt)

shape = [[0 , -1, 1, 0], [-1, 0, 0, -1], [-1, 0, 0, 1], [0, 1, 1, 0]]
visited = [[0] * M for _ in range(N)]
answer = 0
DFS(0, 0, 0)
print(answer)