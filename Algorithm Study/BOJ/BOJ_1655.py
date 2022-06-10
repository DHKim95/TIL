import heapq
import sys

input = sys.stdin.readline

N = int(input())
left = []
right = []

for _ in range(N):
    number = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -number)
    else:
        heapq.heappush(right, number)

    if right and -left[0] > right[0]:
        leftnumber = heapq.heappop(left)
        rightnumber = heapq.heappop(right)

        heapq.heappush(left, -rightnumber)
        heapq.heappush(right, -leftnumber)

    print(-left[0])