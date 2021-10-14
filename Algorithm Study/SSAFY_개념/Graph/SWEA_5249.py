T = int(input())

for tc in range(T):
    # 노드번호 V, 간선 개수 E
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1) # 방문 표시
    distance = [999999999] * (V+1)  # 거리 표시

    # 양쪽으로 갈 수 있으므로 가중치를 2차원으로 표시
    for _ in range(E):
        a, b, x = map(int, input().split())
        graph[a][b] = x
        graph[b][a] = x

    start = 0 # 시작점
    visited[start] = 1 # 시작점 방문 표시
    distance[start] = 0 # 시작점 거리 0 표시

    idx = 0 # 노드 갯수, 전체 갯수랑 같으면 한바퀴 돌기 완료

    while idx < V: # 노드를 다 돌때 까지
        for nx in range(V+1):
            # 방문한 적이 없고 그래프가 존재하고 그래프 거리가 distance보다 작을 경우
            # print(distance)
            if visited[nx] == 0 and graph[start][nx] and graph[start][nx] < distance[nx]:
                distance[nx] = graph[start][nx]

        # 최솟값 노드를 찾기
        # 거기서 다시 시작하여 방문 안한곳 들어간다.
        min_distance = 999999999  # 최소 거리
        for nx in range(V+1):
            if visited[nx] == 0 and distance[nx] < min_distance:
                min_distance = distance[nx]
                start = nx

        visited[start] = 1
        idx += 1

    answer = sum(distance)
    print("#{} {}".format(tc+1, answer))