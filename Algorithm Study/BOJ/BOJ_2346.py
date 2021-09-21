N = int(input())
arr = list(map(int, input().split()))
idx_lst = [i for i in range(1, N+1)]

idx = 0
answer = []

number = arr.pop(idx)
answer.append(idx_lst.pop(idx))

while arr:
    if number < 0:
        idx = (idx + number) % len(arr)
    else:
        idx = (idx + (number - 1)) % len(arr)
    number = arr.pop(idx)
    answer.append(idx_lst.pop(idx))

print(*answer)