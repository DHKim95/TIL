import math


def solution(arrayA, arrayB):
    answer = 0

    # def check(arr):
    #     num = arr[0]
    #     for i in arr:
    #         num = math.gcd(num, i)
    #     return num

    def custom_gcd(a, b):
        if a % b == 0:
            return b
        elif b == 0:
            return a
        else:
            return custom_gcd(b, a % b)

    def check(arr):
        num = arr[0]
        for i in arr:
            num = custom_gcd(num, i)

        return num

    number_A = check(arrayA)
    number_B = check(arrayB)

    # print(number_A, number_B)

    # 나누어지는거 찾기
    for a in arrayB:
        if a % number_A == 0:
            break
    else:
        answer = max(number_A, answer)

    # 나누어지는거 찾기
    for b in arrayA:
        if b % number_B == 0:
            break
    else:
        answer = max(number_B, answer)

    return answer