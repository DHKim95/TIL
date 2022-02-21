N = int(input())

for _ in range(N):
    lst = input()
    stack = []

    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append('(')
        elif lst[i] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif len(stack) == 0:
                stack.append(')')

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

