def DFS(c, max_cnt):
    global min_value
    cnt = 0
    for i in range(len_s):
        data = sorted(result[i])
        lst = []
        now_time = 1
        while data or lst:
            break



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]

    stair = []
    people = []

    for i in range(N):
        for j in range(N):
            # 사람 찾기
            if graph[i][j] == 1:
                people.append((i,j))
            # 계단 찾기
            elif graph[i][j] > 1:
                stair.append((i,j,graph[i][j]))

    len_p = len(people) # 사람 수
    len_s = len(stair) # 계단 수
    result = [[] for _ in range(len_s)]
    min_value = 987654321



