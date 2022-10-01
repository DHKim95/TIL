def solution(dartResult):
    answer = []
    # 10점을 간편하게 바꾸기
    dartResult = dartResult.replace('10', 'X')

    dart = list(dartResult)
    for i in range(1, len(dart)):
        # 점수대로 계산
        if dart[i] == 'S':
            if dart[i - 1] == 'X':
                answer.append(10)
            else:
                answer.append(int(dart[i - 1]))
        elif dart[i] == 'D':
            if dart[i - 1] == 'X':
                answer.append(10 ** 2)
            else:
                answer.append(int(dart[i - 1]) ** 2)
        elif dart[i] == 'T':
            if dart[i - 1] == 'X':
                answer.append(10 ** 3)
            else:
                answer.append(int(dart[i - 1]) ** 3)

        # 스타상
        if dart[i] == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        # 아차상
        elif dart[i] == '#':
            answer[-1] = answer[-1] * (-1)

    return sum(answer)