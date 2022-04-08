N = int(input())

for _ in range(N):
    number, b = map(int, input().split())
    num = bin(number)[2:].count('1')
    if int(num) % 2 == b:
        print("Valid")
    else:
        print("Corrupt")