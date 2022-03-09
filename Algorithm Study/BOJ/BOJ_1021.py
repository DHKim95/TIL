from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque([i for i in range(1, N+1)])
cnt = 0

for num in arr:
    while True:
        # 0번째면 제거 -> 1번
        if queue.index(num) == 0:
            queue.popleft()
            break

        # 길이 비교해서 왼쪽
        if queue.index(num) - 0 <= len(queue) - queue.index(num):
            queue.append(queue.popleft())
            cnt += 1
        # 아닌경우 오른쪽
        else:
            queue.appendleft(queue.pop())
            cnt += 1

print(cnt)
