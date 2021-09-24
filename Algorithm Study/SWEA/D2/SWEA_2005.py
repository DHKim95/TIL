T = int(input())
for tc in range(T):
    N = int(input())
    # 2차원 배열 만들어주기
    graph = [[0] * N for _ in range(N)]
    print("#{}".format(tc+1))

    # 열이 0번이거나 행과 열이 같은 경우 1로 만들어준다. (양끝)
    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                graph[i][j] = 1
            # 아닐경우 자신위에 한칸 왼쪽과 바로 위 숫자가 더한 값이기 때문에 계산해준다.
            else:
                graph[i][j] = graph[i-1][j-1] + graph[i-1][j]

    # 0일 경우에는 아무 숫자가 없기 때문에 pass 해주고 나머지 숫자는 차례대로 출력해준다.
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                pass
            else:
                print(graph[i][j], end=' ')
        print() # 다음줄로 가기 위함