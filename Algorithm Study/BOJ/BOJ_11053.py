# N = int(input())
#
# arr = list(map(int, input().split()))
# result = [1] * N
#
# for i in range(1, N):
#     for j in range(i):
#         print("보자",i, j)
#         if arr[j] < arr[i]:
#             result[i] = max(result[i], result[j] + 1)
#             print(result)

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))