N, M = map(int, input().split())

arr = list(map(int, input().split()))
value = 0
sum_arr = [0]

for i in arr:
    value += i
    sum_arr.append(value)

for _ in range(M):
    a, b = map(int, input().split())
    print(sum_arr[b] - sum_arr[a-1])