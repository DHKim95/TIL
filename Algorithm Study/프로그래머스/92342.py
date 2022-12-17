from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    answer = []
    score = info[::-1]
    _len = len(info)
    max_value = -1
    
    # 경우의 수 만들기
    for num in combinations_with_replacement(range(_len), n):
        apeach, ryan = 0, 0
        tmp = [0 for _ in range(_len)]
        
        # 만든거 카운팅
        cou = Counter(num)
        # print(cou)
        
        # 비교해서 넣기
        for i in range(_len):
            if score[i] < cou[i]:
                ryan += i
            elif score[i] >= cou[i] and score[i] > 0:
                apeach += i
                
            tmp[i] = cou[i]
        
        # 라이언이 점수가 높다면
        if apeach < ryan:
            number = ryan - apeach
            # 최대값보다 높으면 갱신
            if max_value < number:
                max_value = number
                answer = tmp
            
    if len(answer) > 0:
        # 초반에 뒤집어서 출력에 맞게 뒤집기
        return answer[::-1]
    return [-1]