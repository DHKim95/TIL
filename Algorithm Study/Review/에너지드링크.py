N = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
cnt = arr[0]
for i in range(1, N):
    cnt += arr[i] / 2

print("%g" %(cnt))