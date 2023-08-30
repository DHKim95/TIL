K, N = map(int, input().split())

rope_list = []
for _ in range(K):
    rope_list.append(int(input()))

start = 1
end = max(rope_list)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += rope_list[i] // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)