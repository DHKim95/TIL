T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    lst = [] # 파리 잡은 수 저장 리스트
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 인덱스가 초과하지 않게 돌면서
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            # 구간별 파리 수 카운트해서 리스트에 저장해주기
            for k in range(i, i+M):
                for l in range(j, j+M):
                    cnt += graph[k][l]
            lst.append(cnt)

    # 가장많은파리 제공
    max_kill = 0
    for kill in lst:
        if kill > max_kill:
            max_kill = kill

    print("#{} {}".format(tc+1, max_kill))