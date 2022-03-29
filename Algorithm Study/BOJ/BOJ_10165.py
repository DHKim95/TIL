N = int(input())
cnt = 0
pre_list = [N]

if N == 1:
    print(0)
else:
    while True:

        cnt += 1
        now_list = []

        for num in pre_list:
            if num % 3 == 0:
                now_list.append(num // 3)

            if num % 2 == 0:
                now_list.append(num // 2)

            now_list.append(num - 1)

            if 1 in now_list:
                break

        if 1 in now_list:
            break

        pre_list = list(set(now_list))

    print(cnt)