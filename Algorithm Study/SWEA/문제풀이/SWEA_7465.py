def DFS(V):
    visited[V] = 1

    for i in graph[V]:
        if visited[i] == 0:
            DFS(i)

T = int(input())

for tc in range(T):
    # N은 사람 수, M은 관계 수
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            DFS(i)
            cnt += 1

    print("#{} {}".format(tc+1, cnt))
