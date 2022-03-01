# from itertools import combinations
#
# N, M = map(int, input().split())
#
# x = [i for i in range(1, N+1)]
# lst = list(combinations(x, M))
#
# for num in lst:
#     print(*num)

N, M = map(int, input().split())
visited = [False] * (N+1)
answer = []

def DFS(start, cnt):
    if cnt == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, N+1):
        if visited[i] == 0:
            answer.append(i)
            visited[i] = True
            DFS(i, cnt+1)
            answer.pop()
            visited[i] = False

DFS(1, 0)