T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) # N은 길이, M은 회문 길이
    graph = []
    answer = ""
    for _ in range(N):
        graph.append(input())

    # 가로 체크
    for i in range(N):
        for j in range(N-M+1):
            reverse_str = ""
            check_str = ""
            for k in range(M):
                reverse_str += graph[i][N-k-1]
                check_str += graph[i][j+k]

            # 문자가 같을 경우 답안에 추가
            if reverse_str == check_str:
                answer = reverse_str

    # 세로 체크
    for i in range(N):
        for j in range(N-M+1):
            reverse_str = ""
            check_str = ""
            for k in range(M):
                reverse_str += graph[N-k-1][i]
                check_str += graph[j+k][i]

            # 문자가 같을 경우 답안에 추가
            if check_str == reverse_str:
                answer = check_str

    print("#{} {}".format(tc+1, answer))