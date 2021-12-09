from collections import deque
import sys
input = sys.stdin.readline

# N은 도시개수, M은 도로개수, K는 거리정보, X는 출발도시번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시 최단 거리
distance = [-1] * (N+1)
distance[X] = 0

queue = deque([X])
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            queue.append(i)

check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)