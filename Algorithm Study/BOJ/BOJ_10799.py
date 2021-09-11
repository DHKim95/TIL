ring_lst = list(input())
answer = 0
stack = []

for i in range(len(ring_lst)):
    if ring_lst[i] == '(':
        stack.append(ring_lst[i])

    else:
        # 레이저
        if ring_lst[i-1] == '(':
            stack.pop()
            answer += len(stack)
        # 쇠막대기 추가
        else:
            stack.pop()
            answer += 1

print(answer)
