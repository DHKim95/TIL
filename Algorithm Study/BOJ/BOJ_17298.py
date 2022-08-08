N = int(input())

arr = list(map(int, input().split()))
cnt = [-1] * N

stack = []
for i in range(N):
    while stack and (stack[-1][0] < arr[i]):
        now, idx = stack.pop()
        cnt[idx] = arr[i]
    stack.append((arr[i], i))

print(*cnt)
