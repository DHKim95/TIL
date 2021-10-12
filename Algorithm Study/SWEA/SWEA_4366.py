def change_dec(num, number):
    tmp = 0
    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val * (number ** n)
    return tmp

def check(num, number):
    # 진수 변환
    change_num = change_dec(num, number)

    for idx, val in enumerate(list(map(int, num))[::-1]):
        for j in range(number):
            if val == j: # 자릿수가 동일하면 건너뛰기
                continue
            temp = change_num - val * (number ** idx) + j * (number ** idx)

            if temp in binary_lst:
                return temp
            else:
                binary_lst.append(temp)


T = int(input())

for tc in range(T):
    num_two = input()
    num_three = list(input())

    binary_lst = []

    check(num_two, 2)

    print("#{} {}".format(tc+1, check(num_three, 3)))