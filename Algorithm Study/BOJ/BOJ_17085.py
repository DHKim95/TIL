N, M = map(int, input().split())

graph = [input() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 십자가 크기가 얼마나인지 확인하기
def search(x, y):
    cnt = 0
    while 0 <= x - cnt < N and 0 <= x + cnt < N and 0 <= y - cnt < M and 0 <= y + cnt < M and graph[x-cnt][y] == graph[x+cnt][y] == graph[x][y-cnt] == graph[x][y+cnt] == '#':
        cnt += 1

    # 십자가 저장
    while cnt:
        square_lst.append((cnt, x, y))
        cnt -= 1

# 영역이 겹치면 False
def check(cross1, cross2):
    checkboard = [[0] * M for _ in range(N)]

    for i in range(cross1[0]):
        for d in range(4):
            checkboard[cross1[1] + dx[d] * i][cross1[2] + dy[d] * i] = 1

    for i in range(cross2[0]):
        for d in range(4):
            if checkboard[cross2[1] + dx[d] * i][cross2[2] + dy[d] * i] == 1:
                return False
    return True


square_lst = []
answer = 0

# 영역 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] == '#':
            search(i, j)

# 곱한거 최대로 찾기
for i in range(len(square_lst)-1):
    for j in range(i+1, len(square_lst)):
        cross = ((square_lst[i][0]-1) * 4 + 1) * ((square_lst[j][0]-1) * 4 + 1)
        if cross > answer and check(square_lst[i], square_lst[j]) == True:
            answer = cross

print(answer)