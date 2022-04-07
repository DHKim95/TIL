x, y = map(int, input().split())
lst = [x / y]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    lst.append(x / y)

print("{:.2f}".format(min(lst) * 1000))