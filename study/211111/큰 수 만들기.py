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
    number = list(number)
    stack = [number.pop(0)]
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    if k > 0:
        return ''.join(stack)[:-k]
    return ''.join(stack)



print(solution(number, k))