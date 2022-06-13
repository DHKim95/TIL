N = int(input())
arr = list(map(int, input().split()))

arr.sort()
min_value = -1

if N % 2 == 0:
    while arr:
        num = arr[0] + arr[-1]
        arr.pop(0)
        arr.pop(-1)
        if min_value < num:
            min_value = num
else:
    min_value = arr[-1]
    arr.pop()
    while arr:
        num = arr[0] + arr[-1]
        arr.pop(0)
        arr.pop(-1)
        if min_value < num:
            min_value = num

print(min_value)