T = int(input())

for tc in range(T):

    N = int(input()) # 초기숫자
    cnt = [0] * 10
    answer = 0
    for i in range(1, 100001):
        number = str(N * i)
        for num in number:
            if cnt[int(num)] == 0:
                cnt[int(num)] = 1
            else:
                pass

        if sum(cnt) == 10:
            answer = int(number)
            break

    print("#{} {}".format(tc+1, answer))