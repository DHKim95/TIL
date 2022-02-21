from collections import deque
N = int(input())

lst = deque([i for i in range(1, N+1)])
check = True

while True:
    if len(lst) == 1:
        break

    lst.popleft()
    lst.append(lst.popleft())

print(lst[0])

