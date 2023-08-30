from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input().strip()[1:-1].split(',')
    queue = deque(arr)
    check = False
    reverse_cnt = 0

    if n == 0:
        queue = []

    for direction in p:
        if direction == 'R':
            reverse_cnt += 1

        elif direction == 'D':
            if not queue:
                check = True
                print("error")
                break
            else:
                if reverse_cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if not check:
        if reverse_cnt % 2 == 1:
            queue.reverse()
        print("["+",".join(queue) + "]")