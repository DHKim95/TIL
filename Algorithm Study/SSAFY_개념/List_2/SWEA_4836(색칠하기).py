T = int(input())

for tc in range(T):
    N = int(input()) # 영역의 개수
    graph = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        # 각각 모서리와 색을 입력 받는다.
        r1, c1, r2, c2, color = map(int, input().split())

        # 같은 색끼리는 영역이 겹치지 않는다고 했으니 해당 영역에 색을 더해도 된다.
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                graph[row][col] += color

    cnt = 0 # 겹치는것 카운트
    for i in range(10):
        for j in range(10):
            # 빨강은 1, 파랑은 2 -> 겹치면 3
            if graph[i][j] == 3:
                cnt += 1

    print("#{} {}".format(tc+1, cnt))