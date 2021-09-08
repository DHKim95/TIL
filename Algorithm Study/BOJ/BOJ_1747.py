def isPrime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

N = int(input())
answer = 0

for i in range(N, 1000001):
    if i == 1: # 1은 소수가 아니다
        continue
    if str(i) == str(i)[::-1]:
        if isPrime(i) == True:
            answer = i
            break

if answer == 0:
    answer = 1003001

print(answer)