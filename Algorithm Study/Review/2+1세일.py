N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

cnt = 0
for i in range(2, len(arr), 3):
    cnt += arr[i]

print(sum(arr) - cnt)