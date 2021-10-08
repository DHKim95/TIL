T = int(input())

for tc in range(T):
    N = int(input())
    # 돈 리스트
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # 정답 카운트 리스트
    answer = [0] * 8

    for i in range(8):
        if N // money[i] != 0:
            # 해당 지폐만큼 카운트
            answer[i] = N // money[i]
            N = N % money[i] # 나머지 금액으로 반복
    print("#{}".format(tc+1))
    print(*answer)