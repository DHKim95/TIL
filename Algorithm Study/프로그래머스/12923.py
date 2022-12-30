import math


def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        number = 1
        # 나눠지는수들은 넣기
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                number = (num // i)
                if num // i > 10000000:
                    number = 1
                    continue
                else:
                    break
                    # number = (num // i)
                # break

        answer.append(number)
        # 소수인것들은 1추가
        # else:
        #     answer.append(1)
    if begin == 1:
        answer[0] = 0

    return answer