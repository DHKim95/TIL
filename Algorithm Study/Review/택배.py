N, C = map(int, input().split())
M = int(input())

arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])

lst = [C] * N
cnt = 0
for start, end, box in arr:
    min_value = C
    for i in range(start, end):
        if min_value > min(lst[i], box):
            min_value = min(lst[i], box)

    for i in range(start, end):
        lst[i] -= min_value
    cnt += min_value

print(cnt)