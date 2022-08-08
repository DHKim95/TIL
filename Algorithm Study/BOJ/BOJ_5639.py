def DFS(start, end):
    if start > end:
        return

    mid = end + 1

    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            mid = i
            break

    DFS(start + 1, mid - 1)
    DFS(mid, end)
    print(tree[start])

import sys
sys.setrecursionlimit(10 ** 9)

tree = []
cnt = 0
while True:
    try:
        n = int(input())
        tree.append(n)
    except:
        break

DFS(0, len(tree)-1)