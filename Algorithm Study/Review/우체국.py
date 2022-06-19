N = int(input())

max_people = 0
arr = []
for _ in range(N):
    village, people = map(int, input().split())
    max_people += people
    arr.append([village, people])

arr.sort(key=lambda x: x[0])

cen_people = max_people / 2

cnt = 0
for idx, value in arr:
    cnt += value
    if cnt >= cen_people:
        print(idx)
        break