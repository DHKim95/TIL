data = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',
        '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111'}

T = int(input())

for tc in range(T):
    N, number = input().split()

    answer = ""
    for num in number:
        answer += data[num]
    print("#{} {}".format(tc+1, answer))


# for tc in range(T):
#     N, number = input().split()
#
#     h = int('0x'+number, 16)
#     b = format(h, 'b')
#
#     if len(b) % int(N) != 0:
#         answer = '0' * (int(N) - (len(b) % int(N))) + b
#     else:
#         answer = b
#
#     print("#{} {}".format(tc+1, answer))