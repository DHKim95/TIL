a, b, c = map(int, input().split())

def multi(b):
    if b == 1:
        return a % c
    if b % 2 == 0:
        x = multi(b // 2)
        return x * x % c
    else:
        x = multi(b // 2)
        return x * x * a % c

print(multi(b))