def DFS(V):
    visited[V] = 1

    for i in graph[V]:
        if visited[i] == 0:
            DFS(i)

T = int(input())

for tc in range(T):
    # N까지 출석번호, M장의 신청서
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0 # 그룹 수

    for i in range(M):
        # 양쪽으로 추가 -> 이어진 학생들을 찾기 위해
        graph[arr[i*2]].append(arr[i*2+1])
        graph[arr[i*2+1]].append(arr[i*2])


    # 1번부터 방문하지 않은 학생들을 체크
    for i in range(1, N+1):
        if visited[i] == 0:
            DFS(i)
            cnt += 1

    print("#{} {}".format(tc+1, cnt))
