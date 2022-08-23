from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for cor in course:
        arr = []
        for order in orders:
            comb = combinations(sorted(order), cor)
            arr += comb

        sub_arr = Counter(arr)
        if len(sub_arr) > 0:
            max_value = max(sub_arr.values())
            if max_value > 1:
                for key, value in sub_arr.items():
                    if value == max_value:
                        answer.append(''.join(map(str, key)))

    answer.sort()
    return answer