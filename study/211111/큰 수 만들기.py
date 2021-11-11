from itertools import combinations

number = "1111"
k = 2
# number = "1231234"
# k = 3

# 시간초과
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
# --------------------------------------------------------

def solution(number, k):
    answer = []
    for num in number:
        # answer값이 현재 보다 작으면
        while answer and k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    # 같은 숫자일때 걸러내기 위해
    return ''.join(answer)[:len(number)-k]

print(solution(number, k))