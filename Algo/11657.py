# N은 도시개수, M은 노선 정보
N, M = map(int, input().split())

graph = []
dist = [1e9] * (N+1)

for _ in range(M):
    # a는 시작, b는 도착, c는 거리
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def bellmanford(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            now = graph[j][0]
            next = graph[j][1]
            time = graph[j][2]

            if dist[now] != 1e9 and dist[next] > dist[now] + time:
                dist[next] = dist[now] + time
                if i == N-1:
                    return True
    return False

check = bellmanford(1)

if check:
    print("-1")
else:
    for i in range(2, N+1):
        if dist[i] == 1e9:
            print("-1")
        else:
            print(dist[i])