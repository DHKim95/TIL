for tc in range(1, 11):
    N = int(input()) # 테스트의 길이
    arr = input() # 입력칸
    number = [] # 숫자저장
    stack = [] # 연산자 저장

    # 후위표기법 만들기
    for i in arr:
        # 숫자일 경우 숫자리스트에 추가
        if '0' <= i <= '9':
            number.append(i)
        # 숫자가 아닐경우
        else:
            # 괄호는 스택에 쌓아주기
            if i == '(':
                stack.append(i)
            elif i == '*':
                # 스택에 곱셈이 있다면 먼저 없어질때 까지 POP해주고 PUSH
                while stack and (stack[-1] =='*'):
                    number.append(stack.pop())
                stack.append(i)
            # + 스택에 다른 사칙 연산자가 있으면 없어질때까지 POP을 해주고 PUSH
            elif i == '+':
                while stack and (stack[-1] != '('):
                    number.append(stack.pop())
                stack.append(i)
            # 닫는괄호가 나왔으면 여는 괄호를 만날때까지 리스트에 넣어준다.
            elif i == ')':
                while stack and stack[-1] != '(':
                    number.append(stack.pop())
                stack.pop() # 여는괄호 제거

    # 남아있는 스택들을 전부 리스트에 넣어준다.
    while stack:
        number.append(stack.pop())

    # 계산히기
    answer_lst = []
    for i in number:
        if '0' <= i <= '9':
            answer_lst.append(int(i))
        else:
            a = answer_lst.pop()
            b = answer_lst.pop()

            if i == '+':
                answer_lst.append(a+b)
            elif i == '*':
                answer_lst.append(a*b)

    answer = answer_lst[-1]
    print("#{} {}".format(tc, answer))