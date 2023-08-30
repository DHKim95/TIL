N, K = map(int, input().split())
graph = [[] for _ in range(K+1)]
answer = 987654321

for _ in range(N):
    x, y, p = map(int, input().split())
    graph[p].append((x, y))

def DFS(cnt, K, min_X, min_Y, max_X, max_Y, graph):
    global answer
    if cnt > K:
        X = abs(max_X - min_X)
        Y = abs(max_Y - min_Y)
        square = X * Y
        if answer > square:
            answer = square
        return

    if graph[cnt]:
        for nx, ny in graph[cnt]:

            nmin_X = min(min_X, nx)
            nmax_X = max(max_X, nx)
            nmin_Y = min(min_Y, ny)
            nmax_Y = max(max_Y, ny)
            ox = nmax_X - nmin_X
            oy = nmax_Y - nmin_Y
            nsquare = ox * oy
            if answer > nsquare:
                DFS(cnt+1, K, nmin_X, nmin_Y, nmax_X, nmax_Y, graph)



for x, y in graph[1]:
    DFS(2, K, x, y, x, y, graph)

print(answer)