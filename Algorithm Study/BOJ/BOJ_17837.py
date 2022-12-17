N, K = map(int, input().split())

# 맨 위
graph = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]

# print(graph)
turn_list = [] # 말 번호 기록
for num in range(K):
    x, y, d = map(int, input().split())
    # 말 고정
    turn_list.append([x-1, y-1, d-1])
    # 말 좌표에 추가
    board[x-1][y-1].append(num)

# 우좌상하
moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]

############################################################
def move(idx):
    x, y, d = turn_list[idx]
    nx = x + moves[d][0]
    ny = y + moves[d][1]

    # 블루인 경우
    if 0 > nx or nx >= N or 0 > ny or ny >= N or graph[nx][ny] == 2:
        # 방향 전환
        if d % 2 == 1:
            d -= 1
        else:
            d += 1

        # 위치 정보 갱신
        turn_list[idx][2] = d
        nx = x + moves[d][0]
        ny = y + moves[d][1]

        # 뒤도 막혀있음
        if 0 > nx or nx >= N or 0 > ny or ny >= N or graph[nx][ny] == 2:
            return False # 더이상못움직이므로 종료

    arr = [] # 옮길거
    for i, v in enumerate(board[x][y]):
        if v == idx:
            # 말보다 위에 있는것들 옮기기
            arr = board[x][y][i:]
            board[x][y] = board[x][y][:i] # 아래는 남기기
            break

    # 빨간색이면 뒤집기
    if graph[nx][ny] == 1:
        arr = reversed(arr)

    # 위치 갱신
    for i in arr:
        board[nx][ny].append(i)

        turn_list[i] = [nx, ny, turn_list[i][2]]

    # 4개 이상이면 종료
    if len(board[nx][ny]) >= 4:
        return True
    return False

#########################################################

turn = 1
while turn <= 1000:
    for i in range(K):
        check = move(i)
        if check:
            print(turn)
            exit()
    turn += 1
print(-1)