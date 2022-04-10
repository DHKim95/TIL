while True:
    B, N = map(int, input().split())

    # 0, 0이면 바로 종료
    if B == 0 and N == 0:
        break

    #카운트하기
    cnt = 0
    # 곱한수가 넘어갈때까지 찾기
    while cnt ** N < B:
        cnt += 1
    # 현재 제곱수와 전의 제곱수를 비교하여 숫자 찾기
    if cnt ** N - B < B - (cnt -1) ** N:
        print(cnt)
    else:
        print(cnt-1)