import sys
input = sys.stdin.readline

N = int(input())

arr = []
people_cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
    people_cnt += b

arr.sort()
mid_people = people_cnt // 2

if people_cnt % 2:
    mid_people += 1

cnt = 0
for i, j in arr:
    cnt += j
    if cnt >= mid_people:
        print(i)
        break