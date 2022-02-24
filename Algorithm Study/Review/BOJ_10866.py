import sys
from collections import deque

arr = deque()
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    x = list(input().split())

    if x[0] == "push_front":
        arr.appendleft(x[1])
    elif x[0] == 'push_back':
        arr.append(x[1])
    elif x[0] == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif x[0] == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif x[0] == 'size':
        print(len(arr))
    elif x[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif x[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])