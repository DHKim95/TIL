from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque()
visited = set()

for water in arr:
    queue.append((water, 1))
    visited.add(water)

answer = 0
home_cnt = 0
while queue:
    x, cnt = queue.popleft()
    for d in [1, -1]:
        nx = x + d
        if nx not in visited:
            visited.add(nx)
            answer += cnt
            home_cnt += 1
            queue.append((nx, cnt+1))

            if home_cnt == K:
                queue = []
                break

print(answer)
