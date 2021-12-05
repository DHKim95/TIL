def DFS(idx, cnt):
    global max_value

    # 확률 최대치 갱신
    if idx == N:
        if max_value <= cnt:
            max_value = cnt
        return

    # 확률이 낮으면 pass
    if cnt <= max_value:
        return

    for i in range(N):
        # 방문한 것은 넘어가기
        if visited[i] == 1:
            continue

        visited[i] = 1
        DFS(idx + 1, cnt * graph[idx][i] / 100)
        visited[i] = 0


T = int(input())

for tc in range(T):
    N = int(input())  # 직원 N명

    graph = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    answer = []
    max_value = 0

    DFS(0, 1)

    print("#{} {:.6f}".format(tc + 1, max_value * 100))