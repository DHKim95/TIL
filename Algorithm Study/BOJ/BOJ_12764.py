import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []
computer = [0 for _ in range(N)]
lst = [0 for _ in range(N)]
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(heap, [a, b])

while heap:
    now = heapq.heappop(heap)
    for i in range(len(computer)):
        if computer[i] <= now[0]:
            if computer[i] == 0:
                cnt += 1

            computer[i] = now[1]
            lst[i] += 1
            break

print(cnt)
for i in lst:
    if i != 0:
        print(i, end=' ')
