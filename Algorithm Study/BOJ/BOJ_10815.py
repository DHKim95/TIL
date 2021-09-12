import sys
input = sys.stdin.readline

N = int(input())
N_arr = set(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))
answer = []

for i in M_arr:
    if i in N_arr:
        print(1, end=' ')
    else:
        print(0, end=' ')
