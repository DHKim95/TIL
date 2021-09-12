import sys
input = sys.stdin.readline

lst = []
N = int(input())
for i in range(N):
    lst.append(int(input()))

lst.sort()
for i in lst:
    print(i)