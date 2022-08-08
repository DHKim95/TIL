from collections import deque

N = int(input())

graph = [0 for _ in range(N+1)]

def BFS(x):
    queue = deque()
    queue.append((x, [x]))
    while queue:
        a, lst = queue.popleft()
        if a == 1:
            print(len(lst)-1)
            print(*lst)
            break
        if graph[a] == 0:
            graph[a] = 1
            if a % 3 == 0:
                queue.append((a // 3, lst + [a // 3]))
            if a % 2 == 0:
                queue.append((a // 2, lst + [a // 2]))
            queue.append((a-1, lst + [a-1]))

BFS(N)