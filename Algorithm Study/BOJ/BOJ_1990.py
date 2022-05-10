def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

a, b = map(int, input().split())

arr = []
# 천만이상인 수중에 조건에 맞는 수는 없다.
if b > 10000000:
    b = 10000000

for i in range(a, b+1):
    # 팰린드롬 찾기
    if str(i) == str(i)[::-1]:
        arr.append(i)

# 소수 찾기
for i in arr:
    if isPrime(i):
        print(i)

print(-1)