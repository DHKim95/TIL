def DFS(V):
    # 방문하기
    visited[V] = True
    # 그래프 순회
    for i in graph[V]:
        if not visited[i]:
            DFS(i)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split()) # V개 노드, E개 간선

    # 그래프, 방문표시
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    # 간선 입력 받기
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    # [[], [4, 3], [3, 5], [], [6], [], []]

    # 출발점, 도착점
    S, G = map(int, input().split())

    DFS(S)

    # 도착점을 방문했으면 1출력
    if visited[G] == True:
        print("#{} {}".format(tc+1, 1))
    else:
        print("#{} {}".format(tc+1, 0))