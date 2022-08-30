N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
lst = []

def DFS():
    if len(lst) == M:
        print(*lst)
        return

    for i in range(N):
        lst.append(arr[i])
        DFS()
        lst.pop()

DFS()