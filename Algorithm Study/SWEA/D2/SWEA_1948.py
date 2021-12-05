calc = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for tc in range(T):
    answer = 0
    a, b, c, d = map(int, input().split())

    if a == c:
        answer = d - b + 1
    else:
        for i in range(a+1,c):
            answer += calc[i-1]
        answer += d
        answer += (calc[a-1] - b + 1)

    print("#{} {}".format(tc+1, answer))