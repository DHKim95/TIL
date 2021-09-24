T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split()) # K는 이동가능 정류장 수, N은 종점, M은 충전기가 설치된 정류장
    arr = map(int, input().split())
    station = [0 for _ in range(N+1)]

    for i in arr:
        station[i] += 1

    battery = 0 # 충전 횟수
    start = 0 # 시작점

    while True:
        if start >= N:  # 마지막에 도달하면 탈출
            break
        cnt = 0  # 몇 칸 이동하는지 계산하기
        for num in range(K, 0, -1): # 큰 수부터 차례로 내려온다.
            if start+num >= N: # 시작점이 종점을 넘어서면 그대로 탈출
                start += num
                break
            elif station[start+num] == 1: # 충전소에 도달하면 충전하고 시작점 더해주기
                start += num
                battery += 1
                break
            else:
                cnt += 1 # 충전소가 없으면 이동거리 + 1

        if cnt == K: # 이동거리가 최대이동거리와 같으면 충전횟수 0으로하고 탈출
            battery = 0
            break

    print("#{} {}".format(tc+1, battery))