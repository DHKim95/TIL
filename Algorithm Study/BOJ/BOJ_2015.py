from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
dic = defaultdict(int)

# 누적
for i in range(1, len(arr)):
    arr[i] += arr[i-1]

for i in range(len(arr)):
    if arr[i] == K:
        cnt += 1

    cnt += dic[arr[i]-K]
    dic[arr[i]] += 1

print(cnt)