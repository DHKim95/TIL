T = int(input())

for tc in range(T):
    cnt = 0
    word = "0"
    num = input()

    for i in range(len(num)):
        if num[i] != word:
            cnt += 1
            word = num[i]

    print("#{} {}".format(tc+1, cnt))