N = int(input())

graph = [[] for _ in range(N+1)]
for i in range(N):
    graph[i+1].append(int(input()))

def DFS(x):
    if visited[x] == 0:
        visited[x] = 1
        for i in graph[x]:
            up.add(x)
            bottom.add(i)

            # 같아지면 끝
            if up == bottom:
                answer.extend(list(bottom))
                return
            DFS(i)
    visited[x] = 0

answer = []

for i in range(1, N+1):
    visited = [0] * (N+1)
    # 중복 방지
    up = set()
    bottom = set()

    DFS(i)

answer = list(set(answer))
answer.sort()

print(len(answer))
for i in answer:
    print(i)