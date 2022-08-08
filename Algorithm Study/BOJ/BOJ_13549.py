from collections import deque

N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]
visited[N] = 0
queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()
    if x == K:
        print(visited[x])
        break

    if 0 <= x-1 < 100001 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        queue.append(x-1)

    if 0 < x*2 < 100001 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        queue.appendleft(x*2)

    if 0 <= x+1 < 100001 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)