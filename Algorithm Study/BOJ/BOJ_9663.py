# 대각선 확인
def check(x):
    for i in range(x):
        if abs(graph[x] - graph[i]) == (x-i):
            return False
    return True

def DFS(x):
    global cnt
    if x == N:
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:
            graph[x] = i

            if check(x):
                visited[i] = True
                DFS(x+1)
                visited[i] = False

N = int(input())

cnt = 0
visited = [0 for _ in range(N)]
graph = [0 for _ in range(N)]

DFS(0)
print(cnt)