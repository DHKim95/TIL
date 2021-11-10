from itertools import combinations

number = "1924"
k = 2
# number = "1231234"
# k = 3


# def solution(number, k):
#     len_num = len(number)
#     lst = list(number)
#     comb_lst = list(combinations(lst, len_num-k))
#     answer = []
#
#     for i in comb_lst:
#         answer.append(int(''.join(i)))
#
#     return str(max(answer))

def solution(number, k):
    stack = []
    for i in number:
        



print(solution(number, k))