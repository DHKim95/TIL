T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [list(input()) for _ in range(N)]

    max_value = N * M

    cnt_one = 0
    for i in range(N-2):
        for j in range(M):
            if graph[i][j] != 'W':
                cnt_one += 1

        cnt_two = 0
        for k in range(i+1, N-1):
            for l in range(M):
                if graph[k][l] != 'B':
                    cnt_two += 1

            cnt_thr = 0
            for m in range(k+1, N):
                for n in range(M):
                    if graph[m][n] != 'R':
                        cnt_thr += 1

            cnt = cnt_one + cnt_two + cnt_thr

            if cnt < max_value:
                max_value = cnt

    print("#{} {}".format(tc+1, max_value))