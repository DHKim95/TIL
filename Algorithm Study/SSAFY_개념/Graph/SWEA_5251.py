T = int(input())

for tc in range(T):
    N, E = map(int, input().split())
    graph = [[999999999] * (N+1) for _ in range(N+1)]

    for _ in range(E):
        start, end, w = map(int, input().split())
        graph[start][end] = w

    # 플로이드 워셜 알고리즘
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

<<<<<<< HEAD
    print("#{} {}".format(tc+1, graph[0][N]))
=======
<<<<<<< HEAD
    print("#{} {}".format(tc+1, graph[0][N]))
=======
    print("#{} {}".format(tc+1, graph[0][N]))
>>>>>>> 51f2741b542d3a054cdef77c17242bef479402fc
>>>>>>> b3fb155ee50f7573883106c96eddcc62e329ff98
