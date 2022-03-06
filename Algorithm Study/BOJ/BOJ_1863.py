N = int(input())

stack = []
cnt = 0

for i in range(N):
    x, y = map(int, input().split())
    while len(stack) > 0 and stack[-1] > y:
        cnt += 1
        stack.pop()


    if len(stack) > 0 and stack[-1] == y:
        continue
    stack.append(y)

while len(stack) > 0:
    if stack[-1] > 0:
        cnt += 1
    stack.pop()

print(cnt)