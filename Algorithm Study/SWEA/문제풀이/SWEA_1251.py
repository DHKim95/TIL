T = int(input())

for tc in range(T):
    N = int(input())

    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))

    E = float(input())

    graph = []
    for i in range(N):
        for j in range(i, N):
            graph.append(((x_lst[i] - x_lst[j]) ** 2 (y_lst[i] - y_lst[j]) ** 2) * E)
