import heapq

N = int(input())
arr = []

for _ in range(N):
    number = int(input())

    if number == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, number)