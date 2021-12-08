dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x,y, chk_cnt):
    global cnt
    if graph[x][y] == 3:
        if cnt == 1:
            print(visited)
        cnt_lst.append(cnt)
        return

    if chk_cnt < L:
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 갈고리가 없는 경우
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                chk_cnt += 1
                DFS(nx, ny, chk_cnt)
                chk_cnt -= 1
                visited[nx][ny] = 0

            # 갈고리만나면 추가
            elif 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x = chk_cnt
                chk_cnt = 0
                DFS(nx, ny, chk_cnt)
                chk_cnt = x
                visited[nx][ny] = 0
                cnt -= 1

            elif 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 3 and visited[nx][ny] == 0:
                DFS(nx, ny, chk_cnt)
    else:
        return

T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split()) # N은 행, M은 열, L은 최대이동거리
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    # 1은 암벽고리, 0은 고리없음, 2는 출발지, 3은 도착지
    cnt = 0
    chk_cnt = 0
    cnt_lst = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                DFS(i,j, chk_cnt)


    print(cnt_lst)
    if len(cnt_lst) == 0:
        print("{}".format(-1))
    else:
        print("{}".format(min(cnt_lst)))