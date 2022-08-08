N = int(input())

star = [[' '] * 2 * N for _ in range(N)]

def recursion(x, y, size):
    if size == 3:
        star[x][y] = '*'
        star[x + 1][y - 1] = star[x + 1][y + 1] = '*'
        for k in range(-2, 3):
            star[x + 2][y - k] = '*'

    else:
        new = size // 2
        recursion(x, y, new)
        recursion(x + new, y - new, new)
        recursion(x + new, y + new, new)

recursion(0, N-1, N)
for s in star:
    print("".join(s))