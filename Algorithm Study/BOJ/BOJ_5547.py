def DFS(y, x):
    stack = [(y, x)]
    visited[y][x] =1
    cnt = 0
    while stack:
        y, x = stack.pop()
        if y % 2:
            dxdy = [(-1, 0), (-1, -1), (0, -1), (0, 1), (1, 0), (1, -1)]
        else:
            dxdy = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        for i, j in dxdy:
            if y + i >= 0 and y + i < N and x + j >= 0 and x + j < M and not visited[y+i][x+j]:
                if graph[y+i][x+j]:
                    cnt += 1
                else:
                    visited[y+i][x+j] = 1
                    stack.append((y+i, x+j))

    return cnt

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

total_cnt = 0
# 위아래
for j in [0, N-1]:
    for i in range(M):
        # 2개씩 추가
        if graph[j][i]:
            total_cnt += 2
            # 끝점
            if (i == M-1 and j == 0) or (i==0 and j == N-1):
                total_cnt -= 1
        elif graph[j][i] == 0 and not visited[j][i]:
            total_cnt += DFS(j, i)

# 왼오
for j in range(N):
    for i in [0, M-1]:
        if graph[j][i]:
            if (i == 0 and j % 2) or (i == M-1 and j % 2 == 0):
                total_cnt += 3
            else:
                total_cnt += 1
        elif graph[j][i] == 0 and not visited[j][i]:
            total_cnt += DFS(j, i)

print(total_cnt)