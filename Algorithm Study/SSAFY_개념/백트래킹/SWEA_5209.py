def DFS(idx, cnt):
    global current_value

    if sum(visited) == N:
        if current_value > cnt:
            current_value = cnt

    # 중간에 범위가 초과해버리면 건너뛰기
    elif current_value <= cnt:
        return

    for i in range(N):

        # 방문한 것은 넘어가기
        if visited[i] == 1:
            continue

        visited[i] = 1
        DFS(idx+1, cnt + graph[idx][i])
        visited[i] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = []
    current_value = 99999999

    DFS(0, 0)

    print("#{} {}".format(tc+1, current_value))