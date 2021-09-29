def change(x):
    cnt = 0
    for i in range(7):
        # 해당숫자를 계산하여 더해준다.
        cnt += int(x[i]) * (2 ** (6 - i))
    return str(cnt)

number = input() # 입력 받기
lst = [] # 리스트

# 7개 바이트 마다 출력되므로 7개씩 뽑아낸다.
for i in range(0, len(number), 7):
    bin_num = number[i:i+7]
    # 10진수로 변환하여 리스트에 넣기
    lst.append(change(bin_num))

print("{}".format(', '.join(lst)))