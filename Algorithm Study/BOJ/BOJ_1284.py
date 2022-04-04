while True:
    N = input()

    if N == '0':
        break

    # 공백 더하기
    cnt = len(N) + 1
    # 경우의 수 따라 더하기
    for word in N:
        if word == '0':
            cnt += 4
        elif word == '1':
            cnt += 2
        else:
            cnt += 3
    print(cnt)