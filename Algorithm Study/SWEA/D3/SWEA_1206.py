for i in range(1, 11):
    N = int(input()) # 세대수
    cnt = 0 # 조망권이 보장된 세대
    build_lst = list(map(int, input().split()))
    for build in range(2, len(build_lst)-2):
        main_build = build_lst[build] # if문이 길어져서 따로 빼주기
        if (main_build > build_lst[build-1]) and (main_build > build_lst[build-2]) and (main_build > build_lst[build+1]) and (main_build > build_lst[build+2]):
            # cnt += (main_build - max(build_lst[build-1], build_lst[build-2], build_lst[build+1], build_lst[build+2]))
            arr = [build_lst[build-1], build_lst[build-2], build_lst[build+1], build_lst[build+2]] # 양옆 4개의 건물을 리스트로 만든다.
            max_value = 0
            for num in arr: # 4개의 건물중 가장 큰 값을 찾는다.
                if num > max_value:
                    max_value = num
            cnt += (main_build - max_value) # 가장 큰값이 조망을 방해하는 요소기 때문에 빼준 후 세대에 더해준다.

    print("#{} {}".format(i, cnt))