# from itertools import permutations
#
# N, M = map(int, input().split())
#
# arr = list(map(int, input().split()))
#
# lst = list(permutations(arr, M))
# lst = list(set(lst))
# lst.sort()
#
# for i in lst:
#     print(*i)

def DFS():
    if len(lst) == M:
        print(*lst)
        return

    x = 0
    for i in range(N):
        if not visited[i] and x != arr[i]:
            visited[i] = True
            lst.append(arr[i])
            x = arr[i]
            DFS()
            visited[i] = False
            lst.pop()

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

visited = [0] * N
lst = []

DFS()