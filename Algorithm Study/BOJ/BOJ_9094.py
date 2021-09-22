T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    cnt = 0
    for i in range(1, N-1):
        for j in range(i+1, N):
            if (i ** 2 + j ** 2 + M) % (i * j) == 0:
                cnt += 1

    print(cnt)