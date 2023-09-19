import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리되어 있으면 패스
        if distance[now] < dist:
            continue

        # 인접노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)

N, D = map(int, input().split())

graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    start, end, short = map(int, input().split())
    if end > D:
        continue

    graph[start].append((end, short))

dijkstra(0)

print(distance[D])