N = int(input())

x = N * 5 - 400

print(x)
if N > x:
    print(1)
elif N == x:
    print(0)
else:
    print(-1)