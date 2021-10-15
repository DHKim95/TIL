from itertools import combinations

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
num_lst = [i for i in range(1, N+1)]
comb_lst = list(combinations(num_lst, N//2))

min_value = 999999999

for num in range(len(comb_lst)//2):
    # print(comb_lst[num])
    start_A = 0
    start_B = 0
    for i in comb_lst[num]:
        for j in comb_lst[num]:
            # print(i,j)
            start_A += graph[i-1][j-1]

    for i in comb_lst[len(comb_lst)-1-num]:
        for j in comb_lst[len(comb_lst)-1-num]:
            start_B += graph[i-1][j-1]

    min_value = min(min_value, abs(start_A - start_B))
print(min_value)