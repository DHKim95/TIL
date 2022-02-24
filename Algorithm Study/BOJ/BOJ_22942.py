import sys
input = sys.stdin.readline

N = int(input())
circle_lst = []
stack = []

for i in range(N):
    x = input().split()
    a = int(x[0]) - int(x[1])
    b = int(x[0]) + int(x[1])
    circle_lst.append([a, i, 0])
    circle_lst.append([b, i, 1])

circle_lst.sort()

for i in range(N):
    first = circle_lst[i][2]
    if first == 0:
        stack.append(circle_lst[i])
    else:
        if stack[-1][2] == 0:
            if stack[-1][1] == circle_lst[i][1]:
                stack.pop()
            else:
                print("NO")
                exit(0)

print("YES")