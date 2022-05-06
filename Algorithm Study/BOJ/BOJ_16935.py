# 상하반전
def rotate1(graph):
    arr = [[0] * M for _ in range(N)]
    for i in range(N):
        arr[i] = graph[N-i-1]
    return arr

# 좌우반전
def rotate2(graph):
    arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            arr[i][j] = graph[i][M-j-1]
    return arr

# 오른쪽 90도
def rotate3(graph, N, M):
    arr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            arr[i][j] = graph[N-j-1][i]
    return arr

# 왼쪽으로 90도
def rotate4(graph,N, M):
    arr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            arr[i][j] = graph[j][M-i-1]
    return arr

def rotate5(graph):
    arr = [[0] * M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            arr[i][j + M//2] = graph[i][j]
    for i in range(N//2):
        for j in range(M//2, M):
            arr[i + N // 2][j] = graph[i][j]
    for i in range(N//2, N):
        for j in range(M//2, M):
            arr[i][j - M//2] = graph[i][j]
    for i in range(N//2, N):
        for j in range(M//2):
            arr[i - N//2][j] = graph[i][j]
    return arr

def rotate6(graph):
    arr = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            arr[i + N//2][j] = graph[i][j]
    for i in range(N//2, N):
        for j in range(M//2):
            arr[i][j + M//2] = graph[i][j]
    for i in range(N//2, N):
        for j in range(M//2, M):
            arr[i - N//2][j] = graph[i][j]
    for i in range(N//2):
        for j in range(M//2, M):
            arr[i][j - M //2] = graph[i][j]
    return arr


N, M, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
numbers = list(map(int, input().split()))

for number in numbers:
    if number == 1:
        graph = rotate1(graph)
    elif number == 2:
        graph = rotate2(graph)
    elif number == 3:
        graph = rotate3(graph,N, M)
        N, M = M, N
    elif number == 4:
        graph = rotate4(graph, N, M)
        N, M = M, N
    elif number == 5:
        graph = rotate5(graph)
    else:
        graph = rotate6(graph)

for i in graph:
    print(*i)