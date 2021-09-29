def change(x):
    cnt = 0
    for i in range(7):
        # 해당숫자를 계산하여 더해준다.
        cnt += int(x[i]) * (2 ** (6 - i))
    return str(cnt)

# 16진수에서 2진수로 변경해주기
num_lst = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
hex_num = input() # 16진수 입력받기
number = ""
for i in range(len(hex_num)):
    if '0' <= hex_num[i] <= '9':
        number += num_lst[int(hex_num[i])]
    elif hex_num[i] == 'A':
        number += num_lst[10]
    elif hex_num[i] == 'B':
        number += num_lst[11]
    elif hex_num[i] == 'C':
        number += num_lst[12]
    elif hex_num[i] == 'D':
        number += num_lst[13]
    elif hex_num[i] == 'E':
        number += num_lst[14]
    elif hex_num[i] == 'F':
        number += num_lst[15]

# 7개씩 나누어 떨어지지 않는다면 그 마지막에 남는 부분을 0으로 채워준다.
if len(number) % 7 != 0:
    div = len(number) // 7 * 7
    new_number = number[:div]
    end_number = number[div:].zfill(7)

    number = new_number + end_number

lst = [] # 리스트

# 7개 바이트 마다 출력되므로 7개씩 뽑아낸다.
for i in range(0, len(number), 7):
    bin_num = number[i:i+7]
    # 10진수로 변환하여 리스트에 넣기
    lst.append(change(bin_num))

print("{}".format(', '.join(lst)))