def BFS(x,y):
    # 처음 시작점 큐에 넣어주고 방문 표시
    queue = [(x,y)]
    visited[x][y] = 1

    while queue:
        # 큐에 있는걸 뽑아내서 시작
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

           # 지도 범위안에 있고 방문을 안했으며 벽이 아닐 경우에
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] != 1:
                # 도착지점인 3을 찾으면 전에 거리값 반환
                if graph[nx][ny] == 3:
                    answer = visited[x][y]
                    return answer
                # 다음 지점 큐에 넣고 방문처리, 거리처리리
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


# 테스트 케이스
T = int(input())

for tc in range(T):
    N = int(input()) # 크기
    graph = [list(map(int, input())) for _ in range(N)] # 지도
    visited = [[0] * N for _ in range(N)] # 방문표시

    # 4가지 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 출발점 2를 찾아서 수행후 break
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                cnt = BFS(i,j)
                break

    if cnt == None:
        cnt = 0
    else:
        cnt -= 1

    print("#{} {}".format(tc+1, cnt))
