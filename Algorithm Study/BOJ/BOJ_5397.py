T = int(input())

for i in range(T):
    words = input()
    left, right = [], []

    for word in words:
        if word == "<":
            if left:
                right.append(left.pop())
        elif word == '>':
            if right:
                left.append(right.pop())
        elif word == '-':
            if left:
                left.pop()
        else:
            left.append(word)

    for i in reversed(right):
        left.append(i)

    print(''.join(left))