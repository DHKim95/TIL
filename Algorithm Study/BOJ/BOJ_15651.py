N, M = map(int, input().split())
visited = [False] * (N+1)
answer = []

def DFS(start, cnt):
    if cnt == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, N+1):
        if visited[i] == M:
            pass

        if visited[i] < M:
            answer.append(i)
            visited[i] += 1
            DFS(i, cnt+1)
            answer.pop()
            visited[i] -= 1

DFS(1, 0)