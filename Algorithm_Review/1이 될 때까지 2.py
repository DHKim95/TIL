N, K = map(int, input().split())
result = 0

while True:
    # 나누어떨어질때까지 빼기
    target = (N // K) * K
    result += (N - target)
    N = target

    if N < K:
        break

    result += 1
    N //= K

# 마지막 남은 수 빼기
result += (N-1)
print(result)