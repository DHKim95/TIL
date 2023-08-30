import heapq

N = int(input())

arr = []
for i in range(N):
    graph = list(map(int, input().split()))
    if not arr:
        for number in graph:
            heapq.heappush(arr, number)
    else:
        for number in graph:
            if arr[0] < number:
                heapq.heappush(arr, number)
                heapq.heappop(arr)

print(arr[0])
