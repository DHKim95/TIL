# from itertools import permutations
import math


def solution(n, k):
    arr = list(range(1, n + 1))
    answer = []

    while arr:
        fact = math.factorial(n - 1)
        q, r = divmod(k, fact)
        # print(q, r)

        # 나누어떨어지면 인덱스에러나니 한칸 아래
        if r == 0:
            q -= 1
        # 아닐경우 그냥
        else:
            q

        answer.append(arr.pop(q))
        n -= 1
        k = r  # 남은수

    return answer