from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [-1 for _ in range(F+1)]

def BFS(start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        x = queue.popleft()

        if x == G:
            return visited[x]

        for i in (x+U, x-D):
            if 0 < i <= F and visited[i] == -1:
                visited[i] = visited[x] + 1
                queue.append(i)

    return "use the stairs"

print(BFS(S))