T = int(input())

for tc in range(T):
    N = int(input())
    room = []

    room_pos = [0] * (N*N+1) # 룸위 위치를 저장
    room_dist = [1] * (N*N+1) # 해당 번호까지 지나온 방의 개수 저장

    # 입력 받으며 위치 저장
    for i in range(N):
        # tmp = list(map(int, input().split()))
        # for j in range(N):
        #     room_pos[tmp[j]] = (i,j)

        room.append(list(map(int, input().split())))
        for j in range(N):
            room_pos[room[i][j]] = (i,j)

    # 거리정보 저장
    for i in range(2, N * N + 1):
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr = room_pos[i][0] + dr
            nc = room_pos[i][1] + dc

            # i는 방번호
            if 0 <= nr < N and 0 <= nc < N and room[nr][nc] == i-1:
                room_dist[i] = room_dist[i-1]+1
                break

    st_num = 0
    max_cnt = 0

    for i in range(1, N*N+1):
        if room_dist[i] > max_cnt:
            st_num = i
            max_cnt = room_dist[i]

    print("#{} {} {}".format(tc+1, st_num - max_cnt + 1, max_cnt))