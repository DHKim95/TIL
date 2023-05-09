N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr_sum = [0] * (N+1) # 누적합

for i in range(1, N+1):
    arr_sum[i] = arr_sum[i-1] + arr[i-1]

arr_sum = list(map(lambda x: x % M, arr_sum))

cnt_list = [0] * M
for num in arr_sum[1:]:
    cnt_list[num] += 1

answer = 0
for i in range(1, N+1):
    answer += cnt_list[arr_sum[i-1]]
    cnt_list[arr_sum[i]] -= 1

print(answer)