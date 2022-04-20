import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 열별로 합 누적시키기
for i in range(1, N):
    for j in range(M):
        graph[i][j] += graph[i-1][j]

# print(graph)
K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = sum(graph[x2 - 1][y1-1:y2])

    # 중간에서 시작할경우 중간 이전 빼기
    if x1 > 1:
        cnt -= sum(graph[x1-2][y1-1:y2])

    print(cnt)
