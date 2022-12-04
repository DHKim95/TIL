from collections import Counter

def solution(k, tangerine):
    lst = Counter(tangerine)
    # 갯수별로 정리하기
    sort_lst = sorted(lst.items(), key=lambda x: x[1], reverse=True)
    
    # 가능한 만큼 뽑아내기
    answer = 0
    for idx, value in sort_lst:
        if k <= 0:
            break
        
        k -= value
        answer += 1
        
    return answer