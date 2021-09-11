from collections import deque
import sys

queue = deque([])
input = sys.stdin.readline

N = int(input())
for i in range(N):
    x = input().split()

    if x[0] == 'push':
        queue.append(int(x[1]))

    elif x[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif x[0] == 'size':
        print(len(queue))

    elif x[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif x[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif x[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

