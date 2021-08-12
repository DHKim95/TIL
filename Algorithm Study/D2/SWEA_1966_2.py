T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, len(arr)-1):
        min_value = i
        # 최소를 찾아 교환
        for j in range(i+1, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]

    print("#{}".format(tc+1), end=' ')
    print(*arr)