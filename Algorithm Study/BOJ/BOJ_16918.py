from collections import deque

R, C, N = map(int, input().split())
graph = [list(input()) for _ in range(R)]

N -= 1
while N:
    bom = deque()
    # 폭탄 넣기
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                bom.append((i, j))
    # 폭탄 아닌거 변경
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

    N -= 1
    if N == 0:
        break

    while bom:
        r, c = bom.popleft()
        graph[r][c] = '.'
        if 0 <= r - 1:
            graph[r-1][c] = '.'
        if r + 1 < R:
            graph[r+1][c] = '.'
        if 0 <= c - 1:
            graph[r][c-1] = '.'
        if c + 1 < C:
            graph[r][c+1] = '.'
    N -= 1

for i in range(R):
    for j in range(C):
        print(graph[i][j], end='')
    print()