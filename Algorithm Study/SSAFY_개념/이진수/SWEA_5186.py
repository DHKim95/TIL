T = int(input())

for tc in range(T):
    number = float(input())

    cnt = ""
    # 12자리 까지 이므로 for문 돌려주기
    for num in range(-1, -13, -1):
        # 나누어 떨어지는 만큼 몫을 더해주기
        cnt += str(int(number // (2 ** num)))

        # 나누고 나머지만 남김
        number %= (2 ** num)

        # 숫자가 더이상 존재하지 않으면 끝
        if number == 0:
            answer = cnt
            break
    # 13자리 이상이 되면 overflow 출력
    else:
        answer = "overflow"

    print("#{} {}".format(tc+1, answer))