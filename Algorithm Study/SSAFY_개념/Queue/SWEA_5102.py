def BFS(start):
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            # 방문 안했을 경우
            if visited[i] == 0:
                queue.append(i)
                # 거리 체크
                visited[i] = visited[v] + 1

T = int(input())
for tc in range(T):
    V, E = map(int,input().split()) # V는 노드, E는 간선

    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)
    for i in range(E):
        # 방향성이 없으므로 2번
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())

    BFS(start)

    if visited[end] == 0:
        print("#{} {}".format(tc+1, 0))
    else:
        print("#{} {}".format(tc+1, visited[end]-1))

