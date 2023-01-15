from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = []

def BFS(x):
    queue = deque([x])
    visited[x] = 1

    while queue:
        now = queue.popleft()

        # 친구 탐색
        for i in graph[now]:
            if not visited[i]:
                visited[i] = visited[now] + 1
                queue.append(i)


for i in range(1, N+1):
    visited = [0] * (N+1)
    BFS(i)
    # print(visited)
    answer.append(sum(visited))

# print(answer)
print(answer.index(min(answer))+1)