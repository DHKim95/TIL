while True:
    number = int(input())

    if number == 0:
        break

    while True:
        # 한자리 될때까지 계속 더하기
        number = sum(list(map(int, str(number))))

        # 한자리수면 끝
        if number // 10 == 0:
            print(number)
            break