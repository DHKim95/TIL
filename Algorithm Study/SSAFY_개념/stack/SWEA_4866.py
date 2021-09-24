T = int(input())
for tc in range(T):
    words = input() # 문자열 입력받기
    stack = []
    for word in words:
        # 여는 괄호
        if (word == "(") or (word == "{"):
            stack.append(word)
        # 닫는 괄호인 경우
        elif (word == ")") or (word == "}"):
            # 스택에 아무것도 없는 경우 실패
            if len(stack) == 0:
                stack.append(0)
                break
            # 일치하는 경우 스택에 있는걸 삭제
            elif (stack[-1] == "(") and (word == ")"):
                stack.pop()
            elif (stack[-1] == "{") and (word == "}"):
                stack.pop()
            # 아무것도 아닌경우 괄호가 일치하지 않으므로 0 추가해서 잘못된 길로 가게 하기
            else:
                stack.append(0)

    # 스택이 비어있으면 괄호가 일치하므로 1 출력
    if len(stack) == 0:
        print("#{} {}".format(tc+1, 1))
    else:
        print("#{} {}".format(tc+1, 0))
