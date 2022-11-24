N = int(input()) # 도시의 수
M = int(input()) # 여행 계획에 속한 도시들의 수

def DFS(start):
    visited[start] = 1

    for idx, value in enumerate(graph[start]):
        if value == 1 and visited[idx] == 0:
            # 갈수있는 길이고 방문하지 않았으면
            visited[idx] = 1
            DFS(idx)

graph = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))
visited = [0 for _ in range(N)]

DFS(plans[0]-1)

check = False
for plan in plans:
    if visited[plan-1] == 0:
        check = True
        break
if check:
    print("NO")
else:
    print("YES")
