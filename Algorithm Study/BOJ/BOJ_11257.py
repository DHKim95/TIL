N = int(input())

a_num = 35 * 0.3
b_num = 25 * 0.3
c_num = 40 * 0.3

for _ in range(N):
    number, a, b, c = map(int, input().split())

    if a < a_num or b < b_num or c < c_num:
        print("{} {} FAIL".format(number, (a+b+c)))
    elif a+b+c < 55:
        print("{} {} FAIL".format(number, (a + b + c)))
    else:
        print("{} {} PASS".format(number, (a+b+c)))