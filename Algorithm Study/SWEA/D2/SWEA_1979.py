T = int(input()) # 테스트 케이스

for tc in range(T):
    N, K = map(int, input().split()) # 길이와 단어의 길이
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 1이 흰색 0이 검은색
    # 가로 검사하기
    for i in range(N):
        cnt = 0 # 흰색 숫자 체크
        for j in range(N):
            # 흰색이 보인다면 숫자를 1씩 늘려준다.
            if graph[i][j] == 1:
                cnt += 1
            # 검은색 벽이거나 마지막 인덱스에 도달한 경우 길이에 충족한다면 추가해준다.
            if graph[i][j] == 0 or (j == N-1):
                if cnt == K:
                    answer += 1
                # 벽에 도달하면 다시 체크
                cnt = 0

    # 세로 검사하기
    for j in range(N):
        cnt = 0 # 흰색 숫자 체크
        for i in range(N):
            # 흰색이 보인다면 숫자를 1씩 늘려준다.
            if graph[i][j] == 1:
                cnt += 1
            # 검은색이거나 마지막 인덱스에 도달한 경우 길이에 충족한다면 추가해준다.
            if graph[i][j] == 0 or (i == N - 1):
                if cnt == K:
                    answer += 1
                # 벽에 도달하면 다시 체크
                cnt = 0

    print("#{} {}".format(tc+1, answer))
