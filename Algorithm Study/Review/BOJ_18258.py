import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

stack = deque()

for i in range(N):
    x = input().split()

    if x[0] == 'push':
        stack.append(int(x[1]))
    elif x[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
            stack.popleft()

    elif x[0] == 'size':
        print(len(stack))

    elif x[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif x[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])

    elif x[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


