T = int(input())
for tc in range(T):
    number = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while True:
        if number % 11 == 0:
            number //= 11
            e += 1
            continue
        elif number % 7 == 0:
            number //= 7
            d += 1
            continue
        elif number % 5 == 0:
            number //= 5
            c += 1
            continue
        elif number % 3 == 0:
            number //= 3
            b += 1
            continue
        elif number % 2 == 0:
            number //= 2
            a += 1
            continue

        if number == 1:
            break
    print("#{} {} {} {} {} {}".format(tc+1, a, b, c, d, e))