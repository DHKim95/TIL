import sys
input = sys.stdin.readline

words = list(input().strip())
stack = []
N = int(input())

for _ in range(N):
    command = input()
    if command[0] == 'L':
        if len(words) == 0:
            continue
        stack.append(words.pop())
    elif command[0] == 'D':
        if len(stack) == 0:
            continue
        words.append(stack.pop())
    elif command[0] == 'B':
        if len(words) == 0:
            continue
        words.pop()
    elif command[0] == 'P':
        words.append(command[2])

words.extend(stack[::-1])
print(''.join(words))