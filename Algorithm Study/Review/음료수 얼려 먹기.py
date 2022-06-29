N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def DFS(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if DFS(i,j) == True:
            cnt += 1

print(cnt)