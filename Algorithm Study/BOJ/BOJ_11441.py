import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

cnt = 0
sum_arr = [0]

for i in arr:
    cnt += i
    sum_arr.append(cnt)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    print(sum_arr[b] - sum_arr[a-1])