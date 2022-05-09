K = int(input())
# 이진수로 변경
binary_number = format(K+1, 'b')
# print(binary_number)
binary_number = binary_number[1:]
# print(binary_number)
# 0은 4로 1은 7로
print(binary_number.replace('0', '4').replace('1', '7'))