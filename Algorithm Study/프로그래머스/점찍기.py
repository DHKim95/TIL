import math
from itertools import product


def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        a = math.pow(i, 2)
        b = math.pow(d, 2)
        max_value = int(math.sqrt(b - a))
        answer += ((max_value // k) + 1)

    # 이거 안되네...
    # a = range(0, d+1, k)
    # arr = product(a, repeat=2)

    # answer = 0
    # max_length = d
    # for num in arr:
    #     # print((num[0] ** 2 + num[1] ** 2) ** 0.5 <= d)
    #     if int(math.sqrt(num[0] ** 2 + num[1] ** 2)) <= max_length:
    #         answer += 1

    return answer