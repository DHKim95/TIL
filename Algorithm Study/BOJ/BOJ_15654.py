# from itertools import permutations
#
# N, M = map(int, input().split())
#
# x = list(map(int, input().split()))
# x.sort()
# lst = list(permutations(x, M))
#
# for num in lst:
#     print(*num)

N, M = map(int, input().split())

x = list(map(int, input().split()))
x.sort()
visited = [False] * (N)
result = [0] * M

def DFS(count):
    if count == M:
        print(*result)
        return

    for i in range(len(x)):
        if visited[i] == True:
            continue
        visited[i] = True
        result[count] = x[i]
        DFS(count+1)
        visited[i] = False
DFS(0)