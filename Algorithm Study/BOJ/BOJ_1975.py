import sys
input = sys.stdin.readline

def f(N, i):
    if N % i == 0:
        return 1 + f(N // i, i)
    else:
        return 0

T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0

    for i in range(2, N+1):
        cnt += f(N, i)

    print(cnt)