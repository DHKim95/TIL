T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    N = int(input())
    cnt = 0
    for _ in range(N):
        cx, cy, cr = map(int, input().split())
        distance1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        distance2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        new_cr = cr ** 2

        if new_cr > distance1 and new_cr > distance2:
            pass
        elif new_cr > distance1:
            cnt += 1
        elif new_cr > distance2:
            cnt += 1

    print(cnt)