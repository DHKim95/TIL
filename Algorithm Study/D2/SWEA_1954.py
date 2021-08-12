T = int(input())
for tc in range(T):
    N = int(input()) # 그래프 크기
    graph = [[0] * N for _ in range(N)] # 그래프

    dx = [1, 0, -1, 0] # 하, 좌, 상, 우 방향
    dy = [0, -1, 0, 1]
    num = 1 # 숫자는 1부터 시작

    for i in range(0,N): # 가로는 차례대로 숫자를 넣어준다.
        graph[0][i] = num
        num += 1

    x, y = 0, N-1 # 가로가 끝난 후 시작하는 곳
    cnt = N - 1 # 횟수 카운트
    direction = 0 # 방향

    # 4칸 사각형 기준으로 오른쪽으로 처음에 4칸을 진행하면 그 다음부터는 3칸이동 2번, 2칸이동 2번, 1칸이동 2번으로 마무리를 해준다.
    # 그래서 for문을 2번씩 진행하고 카운트를 -1씩 해주었다.
    while True:
        # 횟수가 0이되면 숫자가 다 찼으므로 탈출
        if cnt == 0:
            break

        # 한 방향으로 횟수 카운트 만큼 숫자를 넣어준다.
        for _ in range(cnt):
            x += dx[direction]
            y += dy[direction]
            graph[x][y] = num
            num += 1

        # 한방향이 끝났으니 다른방향으로 바꿔준다.
        direction += 1
        if direction == 4:
            direction = 0

        # 똑같이 한 방향을 넣어준다.
        for _ in range(cnt):
            x += dx[direction]
            y += dy[direction]
            graph[x][y] = num
            num += 1

        # 방향이 끝났으니 다른방향으로 바꿔주고 direction이 4가 되면 다시 맨 앞으로 돌아오게 설정해준다.
        cnt -= 1
        direction += 1
        if direction == 4:
            direction = 0

    print("#{}".format(tc+1))
    for row in range(len(graph)):
        for col in range(len(graph)):
            print(graph[row][col], end=' ')
        print()
