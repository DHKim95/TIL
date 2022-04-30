while True:
    arr = list(map(int, input().split()))
    # 0이면 종료
    if arr[0] == 0:
        break

    N = 1
    for i in range(arr[0]):
        a = arr[2 * i + 1]
        b = arr[2 * i + 2]
        N = N * a - b
    print(N)