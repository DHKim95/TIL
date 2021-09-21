from math import gcd
import sys

input = sys.stdin.readline

N = int(input())
tree = [int(input()) for _ in range(N)]

distance_lst = []
for i in range(N-1):
    distance_lst.append(tree[i+1]-tree[i])

max_num = gcd(distance_lst)

answer = 0
for i in distance_lst:
    answer += ((i//max_num)-1)
print(answer)