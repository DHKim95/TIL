import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(graph, cost, x, y):
    q = []
    heapq.heappush(q, (graph[x][y], x, y))
    while q:
        now_cost, x, y = heapq.heappop(q)
        if cost[x][y] < now_cost:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                n_cost = graph[nx][ny]
                if now_cost + n_cost < cost[nx][ny]:
                    cost[nx][ny] = (now_cost + n_cost)
                    heapq.heappush(q, (now_cost + n_cost, nx, ny))

    return cost[N-1][N-1]

INF = int(1e9)
cnt = 0
while True:
    N = int(input())

    cnt += 1
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    cost = [[INF] * N for _ in range(N)]

    answer = dijkstra(graph, cost, 0, 0)
    print(f"Problem {cnt}: {answer}")