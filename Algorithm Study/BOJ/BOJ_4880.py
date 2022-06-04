while True:
    a, b, c = map(int, input().split())

    if a == b == c:
        break
    elif b-a == c-b:
        print("AP {}".format(c+b-a))
    else:
        print("GP {}".format(c * (b//a)))
