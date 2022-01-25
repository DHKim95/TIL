N, R = map(int, input().split())
arr = list(map(int, input().split()))

lst = [1] * (N+1)
lst[0] = 0

for i in arr:
    lst[i] = 0

if N == R:
    print("*")
else:
    for i in range(len(lst)):
        if lst[i] != 0:
            print(i, end=' ')