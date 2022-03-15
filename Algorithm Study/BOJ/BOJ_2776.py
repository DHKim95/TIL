def binary_search(start, end, arr_N, number):
    while start <= end:
        mid = (start + end) // 2
        if arr_N[mid] == number:
            return 1
        elif arr_N[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return 0

T = int(input())

for tc in range(T):
    N = int(input())
    arr_N = list(map(int, input().split()))

    M = int(input())
    arr_M = list(map(int, input().split()))

    arr_N.sort()
    for number in arr_M:
        print(binary_search(0, N-1, arr_N, number))