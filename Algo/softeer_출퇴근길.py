import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# N은 정점개수, M은 간선개수

graph_s = [[] for _ in range(N+1)]
graph_e = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph_s[a].append(b)
    graph_e[b].append(a)

start, end = map(int, input().split())

# print(graph_s)
# print(graph_e)

def DFS(start, graph, visited):
    # print("비교 ",visited)
    if visited[start] == 1:
        return
    visited[start] = 1
    for i in graph[start]:
        DFS(i, graph, visited)
    return

visited_s = [0] * (N+1)
visited_s[end] = 1
DFS(start, graph_s, visited_s)

visited_e = [0] * (N+1)
visited_e[start] = 1
DFS(end, graph_s, visited_e)

visited_start = [0] * (N+1)
DFS(start, graph_e, visited_start)
visited_end = [0] * (N+1)
DFS(end, graph_e, visited_end)

cnt = 0
for i in range(1, N+1):
    if visited_s[i] and visited_e[i] and visited_start[i] and visited_end[i]:
        cnt += 1

print(cnt-2)