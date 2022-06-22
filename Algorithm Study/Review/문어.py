N = int(input())

arr = [1, 2] * (N // 2)
if N % 2:
    arr += [3]
else:
    arr += []

print(*arr)