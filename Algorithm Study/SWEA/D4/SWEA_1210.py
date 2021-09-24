for _ in range(10):
    T = int(input()) # 테스트 케이스
    graph = [list(map(int, input().split())) for _ in range(100)]

    idx = 0 # 도착지점 찾는 변수

    # 위에서 시작하려 했는데 경우의 수가 너무 많아 에러가 떠서 아래에서 도착점을 찾아 시작
    for i in range(100):
        if graph[99][i] == 2:
            idx = i
            break

    x, y = 99, idx # 초기 출발하는 곳
    while True:
        # 젤 위에 도달하면 반복문 종료
        if x == 0:
            break

        # 왼쪽으로 가는 경우
        if (y > 0) and (graph[x][y-1] == 1):
            graph[x][y] = 0 # 다시 오른쪽으로 가는것을 방지하기 위해 0으로 만들어주기
            y -= 1 # 왼쪽 이동
            continue

        # 오른쪽으로 가는 경우
        if (y < 99) and (graph[x][y+1] == 1):
            graph[x][y] = 0 # 다시 왼쪽으로 가는것을 방지하기 위해 0으로 만들어주기
            y += 1 # 오른쪽 이동
            continue

        if x > 0: # 왼쪽이나 오른쪽으로 갈 수 없을 경우 위로 계속 가기
            x -= 1
            continue

    print("#{} {}".format(T, y))


