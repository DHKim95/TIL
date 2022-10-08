import re
from collections import Counter

def solution(s):
    answer = []
    # 숫자 추출하기
    s = Counter(re.findall('\d+', s))
    # 많은 순으로 정렬
    s = sorted(s.items(), key=lambda x: x[1], reverse=True)
    
    for i in s:
        answer.append(int(i[0]))
    
    return answer