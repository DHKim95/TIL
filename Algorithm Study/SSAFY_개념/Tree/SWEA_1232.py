def calc(v):
    # 해당 숫자 찾아서 계산해주기
    if arr[v] == '+':
        return calc(left[v]) + calc(right[v])
    elif arr[v] == '-':
        return calc(left[v]) - calc(right[v])
    elif arr[v] == '*':
        return calc(left[v]) * calc(right[v])
    elif arr[v] == '/':
        return calc(left[v]) // calc(right[v])
    else:
        return arr[v]

# 테스트 케이스 10개
for tc in range(1, 11):
    N = int(input()) # 숫자 입력
    graph = [list(input().split()) for _ in range(N)]
    arr = [0 for _ in range(N+1)] # Tree
    left = {} # 왼쪽
    right = {} # 오른쪽

    for i in range(N):
        # 4개일 경우
        if len(graph[i]) == 4:
            arr[int(graph[i][0])] = graph[i][1] # 기호를 Tree에 넣어주기
            # 왼쪽 오른쪽에 각각 넣어주기
            left[int(graph[i][0])] = int(graph[i][2])
            right[int(graph[i][0])] = int(graph[i][3])
        else:
            arr[int(graph[i][0])] = int(graph[i][1])

    print("#{} {}".format(tc, calc(1)))