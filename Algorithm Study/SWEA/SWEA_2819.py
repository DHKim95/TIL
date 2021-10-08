dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(number, x, y):
    # 개수가 7개가 되면 딕셔너리에 넣고 종료
    if len(number) == 7:
        number_lst[number] = 1
        return

    for direction in range(4):
        new_x = x + dx[direction]
        new_y = y + dy[direction]

        # 사각형안에 들어오면 계속 가지치기
        if 0 <= new_x < 4 and 0 <= new_y < 4:
            number += graph[new_x][new_y]
            check(number, new_x, new_y)
            number = number[:-1] # 아닐경우 마지막꺼 제외

T = int(input())

for tc in range(T):
    graph = [list(input().split()) for _ in range(4)]
    number_lst = {}
    for i in range(4):
        for j in range(4):
            check(graph[i][j], i, j)

    print("#{} {}".format(tc+1, len(number_lst)))