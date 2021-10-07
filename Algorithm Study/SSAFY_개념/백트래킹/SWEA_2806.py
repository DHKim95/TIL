# 아직 미해결
def DFS(idx):
    global cnt
    if idx >= N:
        cnt += 1
        return

    for y in range(N):
        if visited[y] == 0:
            check = True
            for j in range(idx):
                if abs(graph[j][0] - idx) == abs(graph[j][1] - y):
                    check = False
                    break
            if check == True:
                graph[idx][y] = 1
                visited[y] = 1
                DFS(idx+1)
                visited[y] = 0
                graph[idx][y] = 0

T = int(input())

for tc in range(T):
    N = int(input())

    graph = [[0] * N for _ in range(N)]
    visited = [0] * N
    cnt = 0

    DFS(0)

    print("#{} {}".format(tc+1, cnt))