import heapq

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    heapq.heapify(arr)
    cnt = 0
    if len(arr) == 1:
        print(arr[0])
    else:
        while len(arr) > 1:
            number = heapq.heappop(arr) + heapq.heappop(arr)
            cnt += number
            heapq.heappush(arr, number)

        print(cnt)