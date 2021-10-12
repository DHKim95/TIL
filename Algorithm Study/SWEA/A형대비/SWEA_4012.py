from itertools import combinations

T = int(input())

for tc in range(T):
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]
    num_lst = [i for i in range(N)]

    cnt = 999999999
    comb_lst = list(combinations(num_lst, N//2))

    for i in range(len(comb_lst) // 2):
        A_food = 0
        B_food = 0

        # 조합 값 구하기
        for j in range(N//2-1):
            # 나머지 다 더하기
            for k in range(j+1, N//2):
                A_food += graph[comb_lst[i][j]][comb_lst[i][k]]
                A_food += graph[comb_lst[i][k]][comb_lst[i][j]]

        # 반대 되는거 찾기
        for j in range(N//2-1):
            for k in range(j+1, N//2):
                B_food += graph[comb_lst[len(comb_lst)-1-i][j]][comb_lst[len(comb_lst)-1-i][k]]
                B_food += graph[comb_lst[len(comb_lst)-1-i][k]][comb_lst[len(comb_lst)-1-i][j]]

        if cnt > abs(A_food - B_food):
            cnt = abs(A_food - B_food)

    print("#{} {}".format(tc+1, cnt))
