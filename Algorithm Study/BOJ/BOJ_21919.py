def is_prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

N = int(input())
arr = set(map(int, input().split()))
cnt = 1

for number in arr:
    if is_prime(number):
        # print(number)
        cnt *= number

if cnt == 1:
    print(-1)
else:
    print(cnt)