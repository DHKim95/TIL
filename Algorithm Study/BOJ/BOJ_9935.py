words = input()
bomb = list(input())

stack = []
for i in range(len(words)):
    stack.append(words[i])
    # 같은거 찾아서 삭제하기
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")