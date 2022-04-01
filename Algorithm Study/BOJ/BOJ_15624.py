N = int(input())
a, b = 0, 1
for i in range(N):
    # 나눠야 한다....
    a, b = (a+b) % 1000000007, a % 1000000007
print(a)