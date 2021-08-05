room = int(input())

if room == 1: # 1번방이면 그대로 1 출력
    print(1)
else:
    ans = 1 # 몇개의 방을 거치는지
    while room >= 2:
        room -= num * 6
        ans += 1
        
    print(ans)

    # 방이 6개씩 늘어남