import heapq

T = int(input())

for _ in range(T):
    N = int(input())
    file_lst = list(map(int, input().split()))
    answer = 0

    heapq.heapify(file_lst)
    while len(file_lst) > 1:
        x, y = heapq.heappop(file_lst), heapq.heappop(file_lst)
        answer += (x + y)
        heapq.heappush(file_lst, (x+y))
    print(answer)