# 소수 판별
def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return True
    return False

def solution(n, k):
    number = ""
    while n:
        number = str(n % k) + number
        n //= k
        
    cnt = 0
    # 빈칸 제거, 0으로 분리
    lst = list(filter(len, number.split('0')))

    for i in lst:
        # 1일 경우 건너뛰기
        if i == '1':
            continue
        if not is_prime(int(i)):
            cnt += 1
    
    return cnt