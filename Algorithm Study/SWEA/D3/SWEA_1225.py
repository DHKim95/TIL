for tc in range(1, 11):
    T = int(input()) # 테스트 케이스 번호
    arr = list(map(int, input().split()))

    while True:
        # 0이 되는것 체크 변수
        check = False

        # 1사이클 5 빼주기
        for i in range(1,6):
            # 제일 앞에꺼를 차례대로 빼준다.
            num = arr.pop(0) - i

            # 빼주는 값이 0이하가 되면 0으로 만들어준다,
            if num < 0:
                num = 0

            # 맨뒤에 다시 채워주기
            arr.append(num)

            # 음수나 0이면 0으로 되기 때문에 체크변수 체크해주고 탈출
            if num == 0:
                check = True
                break

        # 체크변수가 True면 끝난 것이기 때문에 탈출
        if check == True:
            break

    print("#{}".format(T), end=' ')
    print(*arr)