for _ in range(10):
    T = int(input()) # 테스트 케이스 번호
    arr = []

    # 입력받기
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    # arr = [list(map(int, input().split())) for _ in range(100)]

    answer = [] # 각 합을 저장할 리스트
    # 각 행의 합
    for i in range(100):
        hap = 0
        for j in range(100):
            hap += arr[i][j]
        answer.append(hap)

    # 각 열의 합
    for i in range(100):
        hap = 0
        for j in range(100):
            hap += arr[j][i]
        answer.append(hap)

    # 우측아래 대각선 합
    hap = 0
    for i in range(100):
        hap += arr[i][i]
    answer.append(hap)
    # hap = 0
    # for i in range(100):
    #     for j in range(100):
    #         if i == j:
    #             hap += arr[i][j]
    # answer.append(hap)

    # 왼쪽아래 대각선 합
    hap = 0
    for i in range(100):
        hap += arr[i][99-i]
    answer.append(hap)
    # hap = 0
    # for i in range(100):
    #     for j in range(100):
    #         if (i+j) == 100:
    #             hap += arr[i][j]
    # answer.append(hap)

    max_value = 0
    for num in answer:
        if num > max_value:
            max_value = num

    print("#{} {}".format(T, max_value))