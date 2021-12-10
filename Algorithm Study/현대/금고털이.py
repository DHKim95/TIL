import sys

input = sys.stdin.readline

W, N = map(int, input().split())
# 배낭에 W까지 담기 가능,

lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[1], reverse=True)

cnt = 0

for weight, price in lst:
    if W > weight:
       cnt += weight * price
       W -= weight
    else:
        cnt += W * price
        break

print(cnt)