n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n, results):
    answer = 0

    graph = [[0] * n for _ in range(n)]

    for a,b in results:
        graph[a-1][b-1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] or graph[j][i]:
                cnt += 1
        if cnt == n-1:
            answer += 1

    return answer

print(solution(n, results))