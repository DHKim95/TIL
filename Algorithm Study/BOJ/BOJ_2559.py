N, K = map(int, input().split())
arr = list(map(int, input().split()))

idx = 0
arr_sum = sum(arr[:K])
max_sum = arr_sum
if K == 1:
    print(max(arr))
else:
    while True:
        arr_sum -= arr[idx]
        # 범위 초과하면 탈출
        if idx + K >= N:
            break

        arr_sum += arr[idx + K]
        # 최대값이 기존값보다 작으면 갱신
        if max_sum < arr_sum:
            max_sum = arr_sum
        idx += 1
    print(max_sum)
