def fact(number):
    if number > 0:
        return number * fact(number-1)
    else:
        return 1

import sys
input = sys.stdin.readline

while True:
    N = input().rstrip()
    # 0이면 그냥 종료
    if N == '0':
        break
    result = 0
    for i in range(1, len(N)+1):
        result += int(N[len(N)-i]) * fact(i)
    print(result)