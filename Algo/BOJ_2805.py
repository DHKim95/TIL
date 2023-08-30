N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for num in arr:
        if num > mid:
            cnt += (num - mid)
    # print(start, end, cnt)
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)