N = int(input())
arr = []
cnt = 0
max_cnt = 0
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, 1])
    arr.append([end, -1])

arr.sort()

for time, value in arr:
    cnt += value
    if value == 1:
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
