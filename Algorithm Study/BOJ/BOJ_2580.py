zero_lst = []
graph = []

for i in range(9):
    graph.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero_lst.append((i, j))

def checkrow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkcol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def check(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx + i][ny + j]:
                return False
    return True

def DFS(x):
    if x == len(zero_lst):
        for i in range(9):
            print(*graph[i])

        exit(0)

    for i in range(1, 10):
        a = zero_lst[x][0]
        b = zero_lst[x][1]

        if checkrow(a, i) and checkcol(b, i) and check(a, b, i):
            graph[a][b] = i
            DFS(x + 1)
            graph[a][b] = 0

DFS(0)