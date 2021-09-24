T = int(input())
for tc in range(T):
    N = int(input())
    lst = [i for i in range(1, N + 1)]
    answer = 0
    for i in range(len(lst)):
        # 짝수일 경우 더한다,
        if i % 2 == 0:
            answer += lst[i]
        # 홀수일 경우 -1을 곱한후 더한다.
        else:
            answer += (-1 * lst[i])

    print("#{} {}".format(tc + 1, answer))