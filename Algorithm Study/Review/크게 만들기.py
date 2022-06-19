N, K = map(int, input().split())
number = list(input())

max_K = K
stack = []
for i in range(N):
    while max_K > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        max_K -= 1
    stack.append(number[i])

print(''.join(stack[:N-K]))