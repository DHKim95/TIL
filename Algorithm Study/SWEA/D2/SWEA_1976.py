T = int(input())

for tc in range(T):
    a, b, c, d = map(int, input().split())
    answer_M = 0
    time_H = a + c
    time_M = b + d



    if time_M >= 60:
        time_H += (time_M // 60)
        answer_M = time_M % 60
        time_M = answer_M

    if time_H > 12:
        time_H = time_H % 12
        if time_H == 0:
            time_H = 12
    print("#{} {} {}".format(tc+1, time_H, time_M))