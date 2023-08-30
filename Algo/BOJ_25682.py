N, M, K = map(int, input().split())

graph = [list(map(str, input())) for _ in range(N)]
hap_graph = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i+j) % 2:
            if graph[i-1][j-1] == 'W':
                hap_graph[i][j] = hap_graph[i-1][j] + hap_graph[i][j-1] - hap_graph[i-1][j-1]
            else:
                hap_graph[i][j] = hap_graph[i - 1][j] + hap_graph[i][j - 1] - hap_graph[i - 1][j - 1] + 1
        else:
            if graph[i-1][j-1] == 'B':
                hap_graph[i][j] = hap_graph[i-1][j] + hap_graph[i][j-1] - hap_graph[i-1][j-1]
            else:
                hap_graph[i][j] = hap_graph[i - 1][j] + hap_graph[i][j - 1] - hap_graph[i - 1][j - 1] + 1

max_value = -1
min_value = 987654321
for i in range(K, N+1):
    for j in range(K, M+1):
        max_value = max(hap_graph[i][j] - hap_graph[i-K][j] - hap_graph[i][j-K] + hap_graph[i-K][j-K], max_value)
        min_value = min(hap_graph[i][j] - hap_graph[i-K][j] - hap_graph[i][j-K] + hap_graph[i-K][j-K], min_value)

print(min(max_value, min_value, K*K-max_value, K*K-min_value))