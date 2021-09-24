T = int(input())

for tc in range(T):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    answer = [0] * 8
    for i in range(8):
        if N // money[i] != 0:
            answer[i] = N // money[i]
            N = N % money[i]
    print("#{}".format(tc+1))
    print(*answer)