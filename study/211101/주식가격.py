prices = [1,2,3,2,3]

def solution(prices):
    answer = [0] * len(prices)

    # 마지막 전까지 -> 마지막은 0임
    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            # 가격이 낮아지면 끝
            if prices[i] > prices[j]:
                break
            # 아닐경우 계속 카운트
            else:
                answer[i] += 1
    return answer

# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             if prices[i] > prices[j]:
#                 cnt += 1
#                 break
#             else:
#                 cnt += 1
#         answer.append(cnt)
#     return answer

# 그냥 pop(0) 스택으로는 효율성에서 통과가 되지 않는다.
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        # price = prices.pop(0)
        price = prices.popleft()
        cnt = 0
        for num in prices:
            cnt += 1
            if price > num:
                break
        answer.append(cnt)
    return answer

print(solution(prices))