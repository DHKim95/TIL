import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
cnt = 0

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def DFS(n, d):
    left, right = 0, 0
    for i, j in graph[n]:
        next = DFS(i, j)
        if left <= right:
            left = max(left, next)
        else:
            right = max(right, next)

    global cnt
    cnt = max(cnt, left + right)
    return max(left + d, right + d)

DFS(1, 0)
print(cnt)