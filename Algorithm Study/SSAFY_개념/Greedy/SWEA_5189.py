def DFS(idx, cnt):
    global current_value

    if sum(visited) == N:
        answer.append(cnt)
        current_value = cnt

    # 중간에 범위가 초과해버리면 건너뛰기
    elif current_value < cnt:
        return

    for i in range(N):
        # 열과 행이 같으면 넘어가기
        if idx == i:
            continue

        # 방문한 것은 넘어가기
        if visited[i] == 1:
            continue

        # 출발점을 제외한 모든점이 안채워졌으면 넘어간다.
        # 출발점은 마지막에
        if i == 0 and sum(visited[1:]) != N-1:
            continue

        visited[i] = 1
        DFS(i, cnt + graph[idx][i])
        visited[i] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = []
    current_value = 99999999

    DFS(0, 0)

    print("#{} {}".format(tc+1, min(answer)))