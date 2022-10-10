from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    answer = []
    
    for i in range(1, 6):
        # 모든 경우의 수
        for j in product(words, repeat=i):
            answer.append(''.join(list(j)))
    
    # 정렬
    answer.sort()
    return answer.index(word)+1