# 현재값 설정을 안했더니 9번에서 시간초과가 났다...

dx = [0, 1]
dy = [1, 0]

def DFS(x, y):
    global cnt, current_value

    # 현재 값이 도착값 보다 크면 바로 종료
    if current_value < cnt:
        return

    # 끝지점 도달하면 값 넣어주기
    if x == N-1 and y == N-1:
        answer.append(cnt)
        current_value = cnt
        return

    # 아래와 오른쪽만 진행
    for direction in range(2):
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위안에 있으면
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += graph[nx][ny]
            DFS(nx,ny)
            cnt -= graph[nx][ny]
            visited[nx][ny] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    answer = [] # 정답 리스트
    cnt = graph[0][0] # 시작 값
    current_value = 999999 # 현재 값

    DFS(0,0)

    print("#{} {}".format(tc+1, min(answer)))