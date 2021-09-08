N = int(input()) # 수열 크기
arr = list(map(int, input().split()))
X = int(input())
cnt = 0

arr.sort()
start, end = 0, N-1

while start != end:
    if arr[start] + arr[end] == X:
        cnt += 1
        start += 1
    elif arr[start] + arr[end] > X:
        end -= 1
    else:
        start += 1

print(cnt)