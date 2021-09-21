# 수학적인문제 - 한번더..

from math import gcd

# 최소공배수 = 숫자 * 숫자 / 최대공약수
# 최소공배수 * 최대공약수 = 숫자 * 숫자
# 산술기하평균 이용....
gcommon, Lcommon = map(int, input().split())

number = Lcommon // gcommon
start, end = 1, number
for i in range(1, number//2 + 1):
    if number % i == 0:
        a = i
        b = number // i
        if gcd(a,b) != 1:
            continue
        if start+end > a+b:
            start = a
            end = b

print(gcommon*start, gcommon*end)