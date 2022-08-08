import heapq

def dijkstra(x):
    dp[x] = 0
    heapq.heappush(heap, (0, x))

    while heap:
        d, now = heapq.heappop(heap)

        if dp[now] < d:
            continue

        for w, n in graph[now]:
            next = w + d
            if next < dp[n]:
                dp[n] = next
                heapq.heappush(heap, (next, n))

V, E = map(int, input().split())
K = int(input())

INF = 987654321
heap = []
graph = [[] for _ in range(V+1)]
dp = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K)
for i in range(1, V+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])