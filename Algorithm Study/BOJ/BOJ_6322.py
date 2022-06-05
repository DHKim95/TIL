cnt = 0

while True:
    cnt += 1
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    if cnt == 1:
        pass
    else:
        print()

    print("Triangle #{}".format(cnt))
    if a == -1:
        if b >= c:
            print("Impossible.")
        else:
            number = (c ** 2 - b ** 2) ** 0.5
            print("a = {:.3f}".format(number))


    elif b == -1:
        if a >= c:
            print("Impossible.")
        else:
            number = (c ** 2 - a ** 2) ** 0.5
            print("b = {:.3f}".format(number))
    elif c == -1:
        number = (a ** 2 + b ** 2) ** 0.5
        print("c = {:.3f}".format(number))
