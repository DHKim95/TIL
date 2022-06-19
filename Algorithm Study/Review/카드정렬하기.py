import heapq

N = int(input())
arr = []
cnt = 0

for i in range(N):
    heapq.heappush(arr, int(input()))

if len(arr) == 1:
    print(0)
else:
    while len(arr) > 1:
        number = heapq.heappop(arr) + heapq.heappop(arr)
        cnt += number
        heapq.heappush(arr, number)

    print(cnt)