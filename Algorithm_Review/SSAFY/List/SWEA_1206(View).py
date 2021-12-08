for tc in range(1,11):
    N = int(input()) # 세대 수
    answer = 0 # 조망권 세대
    buildings = list(map(int, input().split()))

    for idx in range(2, len(buildings)):
        main_idx = buildings[idx]
        if (main_idx > buildings[idx-2]) and (main_idx > buildings[idx-1]) and (main_idx > buildings[idx+1]) and (main_idx > buildings[idx+2]):
            answer += (main_idx - max(buildings[idx-2],buildings[idx-1],buildings[idx+1],buildings[idx+2]))


    print("#{} {}".format(tc, answer))