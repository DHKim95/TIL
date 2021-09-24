T = int(input())
for tc in range(T):
    str1, str2 = map(str, input().split())

    check_str1 = 0
    check_str2 = 0
    for i in str1:
        if i in 'B':
            check_str1 += 2

        elif i in 'ADOPQR':
            check_str1 += 1

    for i in str2:
        if i in 'B':
            check_str2 += 2


        elif i in 'ADOPQR':
            check_str2 += 1

    if check_str1 == check_str2:
        print("#{} {}".format(tc+1, "SAME"))
    else:
        print("#{} {}".format(tc+1, "DIFF"))