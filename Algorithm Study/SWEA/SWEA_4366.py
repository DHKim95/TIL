def change_dec(num, notation):
    tmp = 0

    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val * (notation ** n)
    return tmp

# def change_dec2(num, notation):
#     tmp = 0
#     n = len(num) - 1
#     for i in map(int, num):
#         tmp += i * (notation ** n)
#         n -= 1
    # return tmp

def check(num, notation):
    change_num = change_dec(num, notation)

    for n, val in enumerate(list(map(int, num)))[::-1]:
        for j in range(notation):
            if val == j:
                continue
            tmp = change_num - val (notation ** n) + j * (notation ** n)
            if tmp not in binary_lst:
                binary_lst.append(tmp)


T = int(input())

for tc in range(T):
    num_two = (input())
    num_three = list(input())

    binary_lst = []

    check(num_two, 2)

    print("#{} {}".format(tc+1, check(num_three, 3)))