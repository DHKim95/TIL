arr = [1,2,3]
N = 3

sel = [0] * N

# and 연산자를 썼을때 판별하는 친구

def perm(idx, check: int):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1 << j):
            continue

        sel[idx] = arr[j]
        perm(idx + 1, check | (1<<j))

perm(0, 0)