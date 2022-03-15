N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

first = arr[N-1]
second = arr[N-2]

cnt = int(M / (K + 1)) * K
cnt += M % (K + 1)

result = 0
result += (cnt) * first
result += (M - cnt) * second

print(result)