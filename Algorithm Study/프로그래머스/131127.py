# 할인행사
from collections import Counter

def solution(want, number, discount):
    
    dic = {}
    for fruit, cnt in zip(want, number):
        dic[fruit] = cnt
        
    answer = 0
    _sum = sum(number)
    for i in range(len(discount)-_sum+1):
        arr = Counter(discount[i:i+_sum])
        
        if arr == dic:
            answer += 1
    
    return answer