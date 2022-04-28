arr = [0 for _ in range(31)]
arr[0] = 1
for i in range(28):
    N = int(input())

    arr[N] = 1

for i in range(len(arr)):
    if arr[i] == 0:
        print(i)