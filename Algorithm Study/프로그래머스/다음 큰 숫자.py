def solution(n):
    cnt = n
    zero_cnt = bin(n)[2:].count('0')
    one_cnt = bin(n)[2:].count('1')
    while True:
        cnt += 1

        sub_zero = bin(cnt)[2:].count('0')
        sub_one = bin(cnt)[2:].count('1')
        
        if one_cnt == sub_one:
            break
    
    return cnt