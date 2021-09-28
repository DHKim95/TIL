N = int(input())

for i in range(N):
    num = float(input())
    print("${:.2f}".format(round(num * 0.8, 2)))