dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N*N+1) # 해당 방과 다음 방이 연결 되어 있는지 확인

    for i in range(N):
        for j in range(N):
            for direction in range(4):
                nx = i + dx[direction]
                ny = j + dy[direction]

                if 0 <= nx < N and 0 <= ny < N and graph[i][j] + 1 == graph[nx][ny]:
                    visited[graph[i][j]] = 1

    cnt = 0 # 개수 세기
    start = 0 # 시작 방번호
    max_cnt = 0 # 방의 개수 체크

    for i in range(N*N, -1, -1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1 # 한칸 이동했으니 +1한 값이 시작방
            cnt = 0

    print("#{} {} {}".format(tc+1, start, max_cnt + 1))