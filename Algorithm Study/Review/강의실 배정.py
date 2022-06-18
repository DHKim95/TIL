import heapq
import sys

input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])

class_lst = [0]
cnt = 1
for start, end in arr:
    if start >= class_lst[0]:
        heapq.heappop(class_lst)
    else:
        cnt += 1
    heapq.heappush(class_lst, end)

print(cnt)
