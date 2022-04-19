T = int(input())

for _ in range(T):
    N = int(input())
    arr = [25, 10, 5, 1]
    lst = []

    for i in arr:
        lst.append(N // i)
        N = N % i
    print(*lst)