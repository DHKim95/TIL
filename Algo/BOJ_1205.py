import sys
input = sys.stdin.readline  # 이거 EOF때문에 필요

N, score, P = map(int, input().split())
arr = list(map(int, input().split()))

if N == 0:
    print(1)
else:
    if N == P and arr[-1] >= score:
        print(-1)
    else:
        rank = N+1
        for i in range(N):
            if arr[i] <= score:
                rank = i + 1
                break
        print(rank)