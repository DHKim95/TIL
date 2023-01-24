from collections import deque

N = int(input())
graph = [[1e7] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

score_lst = []
for i in range(1, N+1):
    score_lst.append(max(graph[i][1:N+1]))

min_value = min(score_lst)
# 회장 후보 점수와 후보의 수
print(min_value, score_lst.count(min_value))

answer = []
for i in range(N):
    if score_lst[i] == min_value:
        answer.append(i+1)

print(*answer)