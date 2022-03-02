# from itertools import combinations_with_replacement
#
# N, M = map(int, input().split())
#
# x = list(map(int, input().split()))
# x.sort()
# lst = list(combinations_with_replacement(x, M))
#
# for num in lst:
#     print(*num)


N, M = map(int, input().split())

x = list(map(int, input().split()))
x.sort()
visited = [0] * (N)
result = [0] * M

def DFS(start, count):
    if count == M:
        print(*result)
        return

    for i in range(start, len(x)):
        if visited[i] > M:
            continue
        visited[i] += 1
        result[count] = x[i]
        DFS(i, count+1)
        visited[i] -= 1
DFS(0, 0)