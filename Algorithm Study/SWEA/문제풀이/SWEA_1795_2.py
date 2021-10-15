def dijstra():
    pass

T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    adj1 = [[987654321] * (N+1) for _ in range(N+1)] # 원래 입력(진출)
    adj2 = [[987654321] * (N+1) for _ in range(N+1)] # 뒤집은 입력(진입)

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[x][y] = c

    dist1 = [987654321] * (N+1)
    dist2 = [987654321] * (N+1)

    # 다익스트라 호출
    max_value = 0

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print("#{} {}".format(tc, dijstra()))