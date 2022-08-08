C, N = map(int, input().split())
lst = []
cost_lst = [987654321] * (C+100)
cost_lst[0] = 0

for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[0])

for cost, j in lst:
    for i in range(j, C+100):
        cost_lst[i] = min(cost_lst[i-j] + cost, cost_lst[i])

print(min(cost_lst[C:]))