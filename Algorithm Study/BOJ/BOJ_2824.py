N = int(input())
A_lst = list(map(int, input().split()))
M = int(input())
B_lst = list(map(int, input().split()))

A_cnt = A_lst[0]
for i in range(1,len(A_lst)):
    A_cnt *= A_lst[i]

B_cnt = B_lst[0]
for i in range(1, len(B_lst)):
    B_cnt *= B_lst[i]

import math

number = math.gcd(A_cnt, B_cnt)
if number > 999999999:
    print(str(number)[-9:])
else:
    print(number)