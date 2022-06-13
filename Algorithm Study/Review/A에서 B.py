A, B = map(int, input().split())

cnt = 1
while True:
    if A == B:
        break
    elif A > B or (B % 10 != 1 and B % 2 != 0):
        cnt = -1
        break
    elif B % 10 == 1:
        B //= 10
        cnt += 1
    elif B % 2 == 0:
        B //= 2
        cnt += 1

print(cnt)

# BFS 로 풀수 있는 문제
# from collections import deque
#
# A, B = map(int, input().split())
# queue = deque()
# queue.append((A, 1))
# cnt = 0
#
# while queue:
#     n, t = queue.popleft()
#     if n > B:
#         continue
#     if n == B:
#         print(t)
#         break
#     queue.append((int(str(n)+"1"),t+1))
#     queue.append((n*2, t+1))
# else:
#     print(-1)