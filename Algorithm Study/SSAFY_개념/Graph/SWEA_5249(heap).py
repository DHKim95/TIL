import heapq

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    # 그래프 추가해주기
    for _ in range(E):
        a, b, x = map(int, input().split())
        graph[a].append((b,x))
        graph[b].append((a,x))

    start = 0
    min_distance = 999999999
    distance = [999999999] * (V+1)
    queue = []
    heapq.heappush(queue, (0, 0))
    print(queue)

    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] == min_distance:
            distance[now] = cost
            for pos, co in graph[now]:
                if distance[pos] > co:
                    heapq.heappush(queue, [co,pos])

    print("#{} {}".format(tc+1, sum(distance)))