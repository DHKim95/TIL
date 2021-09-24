T = int(input()) # 테스트 케이스
for i in range(T):
    arr = int(input())

    cnt_lst = [0 for _ in range(10)]
    Triple = 0 # 트리플 체크 변수
    run_test = 0 # 런 체크 변수
    num = 0

    for j in range(6):
        cnt_lst[arr % 10] += 1
        arr //= 10

    # triple 먼저 확인
    while num < 10:
        if cnt_lst[num] >= 3:
            cnt_lst[num] -= 3
            Triple += 1
            continue
        num += 1

    num = 0
    # run_test 확인
    while num < 8:
        if cnt_lst[num] >= 1 and cnt_lst[num+1] >= 1 and cnt_lst[num+2] >=1:
            cnt_lst[num] -= 1
            cnt_lst[num+1] -= 1
            cnt_lst[num+2] -= 1
            run_test += 1
            continue
        num += 1

    if Triple + run_test == 2:
        print("#{} {}".format(i+1, 1))
    else:
        print("#{} {}".format(i+1, 0))


