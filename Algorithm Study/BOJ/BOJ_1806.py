N, S = map(int, input().split())

arr = list(map(int, input().split()))
start, end, now = 0, 0, 0
ans = 987654321

while True:
    if now >= S:
        ans = min(ans, end - start)
        now -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        now += arr[end]
        end += 1
    print(start, end)

if ans == 1000001:
    ans = 0
print(ans)