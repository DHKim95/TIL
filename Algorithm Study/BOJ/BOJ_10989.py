import sys

N = int(input())

size = [0] * 10001
for i in range(N):
    number = int(sys.stdin.readline())

    size[number] = size[number] + 1

for i in range(len(size)):
    if size[i] != 0:
        for j in range(size[i]):
            print(i)