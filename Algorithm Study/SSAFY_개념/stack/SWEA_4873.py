T = int(input())
for tc in range(T):
    words = input()
    stack = [] # 스택 리스트
    # 문자열 회전
    for word in words:
        # 스택에 아무것도 없으면 추가
        if not stack:
            stack.append(word)
        # 스택에 마지막 부분이 현재 알파벳이랑 같으면 스택 마지막부분 제거
        elif word == stack[-1]:
            stack.pop()
        # 그게 아닐경우 스택에 단어를 추가해준다.
        else:
            stack.append(word)

    print("#{} {}".format(tc+1, len(stack)))