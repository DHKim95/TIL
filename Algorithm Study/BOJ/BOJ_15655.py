N, M = map(int, input().split())

x = list(map(int, input().split()))
x.sort()
# visited = [False] * (N)
result = []

def DFS(count):
    if len(result) == M:
        print(*result)
        return

    for i in range(count, N):
        if x[i] not in result:
            result.append(x[i])
            DFS(i+1)
            result.pop()
        # visited[i] = False
DFS(0)