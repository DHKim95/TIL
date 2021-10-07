def DFS(idx):
    global battery_cnt, cnt

    # 목적지에 도달하면
    if idx >= N - 1:
        # 현재 배터리가 더 작을경우 갱신
        if cnt > battery_cnt:
            cnt = battery_cnt
        return
    # 현재 배터리가 최소값을 초과하면
    if cnt < battery_cnt:
        return

    # 가장 멀리부터 탐색
    for i in range(idx+arr[idx], idx, -1):
        battery_cnt += 1
        DFS(i)
        battery_cnt -= 1

T = int(input())

for tc in range(T):
    arr = list(map(int, input().split()))
    N = arr[0] # 정류장 수
    arr = arr[1:] # 전기버스 충전

    cnt = N # 현재 최대
    battery_cnt = 0 # 횟수 카운트

    DFS(0)

    print("#{} {}".format(tc+1, cnt-1))