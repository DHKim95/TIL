T = int(input())

for tc in range(T):
    N = int(input()) # 신청서
    work_time = [list(map(int, input().split())) for _ in range(N)]
    # 끝나는시간 먼저 정렬, 시작시간 정렬
    sort_time = sorted(work_time, key=lambda x: (x[1],x[0]))


    cnt = 1
    truck = sort_time[0][1] # 가장 빨리 끝나는 신청서

    for i in range(1, N):
        # 출발 시간이 끝나는 시간보다 크면 +1을 해서 넣어주고 시간 갱신
        if sort_time[i][0] >= truck:
            cnt += 1
            truck = sort_time[i][1]

    print("#{} {}".format(tc+1, cnt))