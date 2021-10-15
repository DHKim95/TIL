def DFS(V, cnt):
    global max_value

    # 최장거리 찾으면 계속 갱신
    if cnt > max_value:
        max_value = cnt

    for i in graph[V]:
        if visited[i] == 0: # 방문하지 않은거면
            visited[i] = 1 # 체크
            DFS(i, cnt+1)
            visited[i] = 0 # 다시 미체크

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    for _ in range(M):
        # 양쪽 선 다 추가해주기
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    max_value = 0 # 최장거리 변수

    # 1번부터 차례로 전부 탐색
    for i in range(1, N+1):
        # 모든경우 탐색해주기
        visited[i] = 1
        DFS(i, 1)
        visited[i] = 0

    print("#{} {}".format(tc+1, max_value))