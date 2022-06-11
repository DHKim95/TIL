N, K = map(int, input().split())
result = 0

# while N >= K:
#     while N % K != 0:
#         N -= 1
#         result += 1
#
#     N //= K
#     result += 1

while True:
    number = (N // K) * K
    result += (N - number)
    N = number

    if N < K:
        break
    
    result += 1
    N //= K

# 마지막 남은 수 빼주기
result += (N - 1)
print(result)