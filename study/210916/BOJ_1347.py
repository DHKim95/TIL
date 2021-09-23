# 틀린코드

# 남 서 북 동
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())

# 이동
lst = list(input())

direction = 0
x, y = 0, 0
graph = [[x,y]]
square = [[0] * 100 for _ in range(100)]

for move in lst:
    if move == 'F':
        x += dx[direction]
        y += dy[direction]
        graph.append([x,y])
    elif move == 'R':
        direction += 1
        if direction == 4:
            direction = 0
    else:
        direction -= 1
        if direction == -1:
            direction = 3

row_lst = []
col_lst = []
for i in graph:
    col_lst.append(i[1]+50) # 가로 모으기
    row_lst.append(i[0]+50) # 세로 모으기

row = len(set(row_lst))
col = len(set(col_lst))

for i in range(len(row_lst)):
    square[row_lst[i]][col_lst[i]] = 1

answer = []
for i in range(min(row_lst), max(row_lst)+1):
    answer.append(square[i][min(col_lst):max(col_lst)+1])

for i in range(len(answer)):
    for j in range(len(answer[0])):
        if answer[i][j] == 1:
            answer[i][j] = '.'
        else:
            answer[i][j] = '#'

for i in answer:
    print(''.join(i))