def comb(idx, cnt, k):
    global min_value
    if cnt == k:
        A_lst = []
        B_lst = []
        for i in range(N):
            if sel[i] == 1:
                A_lst.append(i)
            else:
                B_lst.append(i)

        A_food = 0
        for i in A_lst:
            for j in A_lst:
                A_food += graph[i][j]

        B_food = 0
        for i in B_lst:
            for j in B_lst:
                B_food += graph[i][j]

        min_value = min(min_value, abs(A_food-B_food))
        return

    # 범위 초과 리턴
    if idx == N:
        return

    sel[idx] = 1
    comb(idx+1, cnt+1, k)
    sel[idx] = 0
    comb(idx+1, cnt, k)

T = int(input())

for tc in range(T):
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]

    sel = [0] * N
    min_value = 999999999
    k = N // 2 # 조합

    comb(0, 0, k)

    print("#{} {}".format(tc+1, min_value))