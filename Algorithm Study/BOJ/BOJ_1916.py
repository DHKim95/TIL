import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(x):
    queue = []
    heapq.heappush(queue, (0, x))
    distance[x] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for nw, nx in graph[now]:
            cost = dist + nw

            if distance[nx] > cost:
                heapq.heappush(queue, (cost, nx))
                distance[nx] = cost

dijkstra(start)

print(distance[end])