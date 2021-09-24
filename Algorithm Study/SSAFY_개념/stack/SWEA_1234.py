for tc in range(10):
    N, words = map(str, input().split())
    stack = []
    for word in words:
        if not stack:
            stack.append(word)
        elif word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)

    print("#{} {}".format(tc+1, ''.join(stack)))