def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x,y):
    p[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # edges = [list(map(int, input().split())) for _ in range(E)]
    #
    # edges.sort(key=lambda x: x[2])

    edges = []

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))
    edges.srot()

    p = list(range(V+1))

    cnt = 0 # 간선을 선택한 횟수
    ans = 0 # 가중치를 더한 값
    idx = 0 # edges 인덱스

    while cnt < V:
        n1 = edges[idx][0]
        n2 = edges[idx][1]

        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            ans += edges[idx][2]

        idx += 1

    print("#{} {}".format(tc, ans))

######################################################

def prim():
    key = [987654321] * (V+1)
    visited = [0] * (V+1)

    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        # 최솟값 찾자
        for i in range(V+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = 1
        # 갱신할 수 있으면 갱신
        for i in range(V+1):
            if not visited[i] and adj_arr[min_idx][i] < key[i]:
                key[i] = adj_arr[min_idx][i]

    return sum(key)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 임의의 큰값으로 초기화 된 값 넣기
    adj_arr = [[987654321] * (V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj_arr[n1][n2] = adj_arr[n2][n1] = w

    ans = 0
