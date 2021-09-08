import sys
from collections import deque

T = int(input())

for tc in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    R_cnt = 0
    check = 0
    if n == 0:
        queue = []

    for j in p:
        if j == 'R':
            R_cnt += 1
        elif j == 'D':
            if len(queue) < 1:
                check = 1
                print("error")
                break
            else:
                if R_cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if check == 0:
        if R_cnt % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")