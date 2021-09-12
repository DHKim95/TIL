import sys
input = sys.stdin.readline

arr = []
lst = list(map(str, input().split()))
N = int(lst[0])
for i in range(1, len(lst)):
    arr.append(int(lst[i][::-1]))

while True:
    if len(arr) == N:
        break

    sub_lst = list(map(str, input().split()))
    for j in sub_lst:
        arr.append(int(j[::-1]))

arr.sort()
for num in arr:
    print(num)