N = int(input())
H = list(map(int, input().split()))
arr = [0] * (1000001)

cnt = 0
for i in range(len(H)):
    if arr[H[i]] == 0:
        cnt += 1
        arr[H[i]-1] += 1
    else:
        arr[H[i]] -= 1
        arr[H[i]-1] += 1

print(cnt)