T = int(input())
for tc in range(T):
    N = int(input())
    graph = [list(map(str, input().split())) for _ in range(N)]

    graph_90 = []
    for i in range(N):
        sub_lst = []
        for j in range(N):
            sub_lst.append(graph[N-1-j][i])
        graph_90.append(sub_lst)

    graph_180 = []
    for i in range(N):
        sub_lst = []
        for j in range(N):
            sub_lst.append(graph[N-1-i][N-1-j])
        graph_180.append(sub_lst)

    graph_270 = []
    for i in range(N):
        sub_lst = []
        for j in range(N):
            sub_lst.append(graph[j][N-1-i])
        graph_270.append(sub_lst)

    print("#{}".format(tc+1))
    for i in range(N):
        print(''.join(graph_90[i]), end=' ')
        print(''.join(graph_180[i]), end=' ')
        print(''.join(graph_270[i]))