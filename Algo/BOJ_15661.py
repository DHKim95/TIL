N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
answer = int(1e9)

def cal():
    global answer
    start_team = 0
    link_team = 0
    for i in range(N):
        for j in range(N):
            # 스타트팀 계산
            if visited[i] and visited[j]:
                start_team += graph[i][j]
            # 링크팀 계산
            elif not visited[i] and not visited[j]:
                link_team += graph[i][j]
    answer = min(answer, abs(start_team-link_team))
    return

def recur(x):
    if x == N:
        cal()
        return

    visited[x] = 1
    recur(x+1)
    visited[x] = 0
    recur(x+1)

recur(0)
print(answer)
