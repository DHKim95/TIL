N = int(input())

arr = list(map(int, input().split()))

# 이전까지 합과 현재값중 큰것을 계속 갱신
for i in range(1, N):
    arr[i] = max(arr[i], arr[i] + arr[i-1])

print(max(arr))