import heapq
import sys

input = sys.stdin.readline
arr = []
N = int(input())
for _ in range(N):
    X = int(input())

    if X == 0:
        if len(arr):
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, X)