N, r, c = map(int, input().split())

cnt = 0
while N != 0:
    N -= 1
    size = 2 ** N

    if r < size and c < size:
        cnt += 0

    elif r < size and c >= size:
        cnt += (size * size)
        c -= size

    elif r >= size and c < size:
        cnt += (size * size * 2)
        r -= size

    else:
        cnt += (size * size * 3)
        r -= size
        c -= size

print(cnt)