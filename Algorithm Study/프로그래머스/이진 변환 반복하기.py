def solution(s):
    cnt = 0
    zero_cnt = 0
    while True:
        if s == '1':
            break
    
        number = s.count('1')
        zero_cnt += s.count('0')
        
        s = bin(number)[2:]
        
        cnt += 1
    
    answer = [cnt, zero_cnt]
    return answer