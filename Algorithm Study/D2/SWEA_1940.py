T = int(input())
for tc in range(1, T+1):

    N = int(input())

    total = 0
    speed = 0

    for i in range(N):
        commands = list(map(int, input().split()))

        # 가속일 때
        if commands[0] == 1:
            speed += commands[1]
        # 감속일 때
        elif commands[0] == 2:
            if speed < commands[1]:
                speed = 0
            else:
                speed -= commands[1]

        total += speed

    print('#{} {}'.format(tc, total))