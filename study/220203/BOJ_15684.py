def check():
    for i in range(N):
        # 이동하는 세로선 위치
        now = i
        for j in range(H):
            # 오른쪽이 1인경우
            if graph[j][now] == 1:
                now += 1
            # 왼쪽이 1인경우
            elif now > 0 and graph[j][now -1]:
                now -= 1

        if now != i:
            return False
    return True

def DFS(cnt, x, y):
    global answer
    # 가로선을 정답보다 많이 만든 경우 확인하지 않는다.
    if answer <= cnt:
        return

    # i번 세로선이 i번 나오는지 체크
    if check():
        answer = min(answer, cnt)
        return

    if cnt == 3:
        return
    for i in range(x, H):
        # 같으,ㄴ 세로줄 확인하며 y부터 확인 다르면 0부터
        if i == x:
            t = y
        else:
            t = 0
        for j in range(t, N-1):
            # 0인경우 가로줄 만들고 연속선 안만들기
            if graph[i][j] == 0:
                graph[i][j] = 1
                DFS(cnt +1, i, j+2)
                graph[i][j] = 0

N, M, H = map(int, input().split())

graph = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

answer = 4
DFS(0, 0, 0)
if answer <= 3:
    print(answer)
else:
    print(-1)