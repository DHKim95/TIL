# 진수 변환하기
def convert(num, d):
    number = "0123456789ABCDEF"
    x = ""
    if num == 0:
        return '0'
    while num > 0:
        x = number[num % d] + x
        num //= d
    return x

def solution(n, t, m, p):
    answer = ""
    sub_answer = ""
    
    # 말해야하는 숫자까지 구하기
    for i in range(t * m):
        sub_answer += convert(i, n)
    
    for i in range(p-1, m*t, m):
        answer += sub_answer[i]
    
    return answer