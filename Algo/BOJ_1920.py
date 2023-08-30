N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
M_arr = list(map(int, input().split()))

def binarySearch(arr, value, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] > value:
        return binarySearch(arr, value, start, mid-1)
    elif arr[mid] < value:
        return binarySearch(arr, value, mid+1, end)
    else:
        return 1

for i in M_arr:
    print(binarySearch(A, i, 0, len(A)-1))