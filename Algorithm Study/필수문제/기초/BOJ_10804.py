arr = [i for i in range(1,21)]

for i in range(10):
    a, b = map(int, input().split())
    lst = arr[a-1:b]
    lst = reversed(lst)
    arr[a-1:b] = lst

for i in range(len(arr)):
    print(arr[i], end=' ')