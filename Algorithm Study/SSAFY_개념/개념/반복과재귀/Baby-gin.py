N = 6 # 길이
K = 3  # 선택
arr = [0] * N

def babygin(arr, idx, cnt):
    if cnt == K:
        print()
        return

    if idx == N:
        return
    arr[idx] = 1
    babygin(arr, idx+1, cnt+1)
    arr[idx] = 0
    babygin(arr, idx +1, cnt)

babygin(arr, 1, 1)