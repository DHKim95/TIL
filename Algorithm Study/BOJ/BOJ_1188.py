def GCD(N, M):
    if N % M == 0:
        return M
    return GCD(M, N % M)

N, M = map(int, input().split())

cnt = GCD(N, M)
print(M - cnt)