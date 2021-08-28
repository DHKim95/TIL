T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split()) # N명 M초 K개
    arr = list(map(int, input().split()))

    arr.sort()

    fish = 0 # 현재 붕어빵 개수
    time = 1 # 현재시간

    if time == 0:
        print("#{} {}".format(tc+1, "Impossible"))
    else:
        while True:
            people = N
            # 시간이 되면 붕어빵 채우기
            if time % M == 0:
                fish += K

            # 한타임에 해당인원 넘어가면 탈출출
            if people == 0:
                break


