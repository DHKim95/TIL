from itertools import combinations

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

max_cnt = 0
for a, b, c in combinations(range(M), 3):
    now_cnt = 0
    for i in range(N):
        now_cnt += max(arr[i][a], arr[i][b], arr[i][c])

    max_cnt = max(max_cnt, now_cnt)

print(max_cnt)
