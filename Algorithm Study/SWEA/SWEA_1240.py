data = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    # code = [list(map(int, input())) for _ in range(N)]
    code = [input() for _ in range(N)]

    lst = ""
    check = False

    for i in range(N):
        for j in range(M-1, -1, -1):
            if code[i][j] == '1':
                lst += (code[i][j-55:j+1])
                check = True
                break
        if check == True:
            break

    number_lst = []

    for i in range(0, len(lst), 7):
        bin_num = lst[i:i + 7]
        # 10진수로 변환하여 리스트에 넣기
        number_lst.append(data[bin_num])


    odd = 0
    even = 0

    for i in range(7):
        if i % 2 == 0:
            odd += int(number_lst[i])
        else:
            even += int(number_lst[i])

    cnt = odd * 3 + even + int(number_lst[7])

    if cnt % 10 == 0:
        number_lst = map(int, number_lst)
        print("#{} {}".format(tc+1, sum(number_lst)))
    else:
        print("#{} {}".format(tc+1, 0))