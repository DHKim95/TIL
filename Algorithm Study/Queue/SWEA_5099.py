T = int(input())

for tc in range(T):
    N, M = map(int, input().split()) # N은 화덕크기, M은 피자 개수
    C = list(map(int, input().split())) # 치즈 양

    oven = [] # 오븐
    queue = [] # 저장소

    # 화덕크기만큼 인덱스랑 같이 넣어준다.
    for i in range(N):
        oven.append((i+1, C.pop(0)))

    # 남은것을 저장소에 인덱스랑 같이 넣어준다.
    for i in range(len(C)):
        queue.append((i+N+1, C.pop(0)))

    # 오븐에 있을때 까지 진행
    while len(oven) > 1:
        # 오븐이 넘치지 않고 큐에 있으면 저장소에 있는걸 오븐에 넣어준다.
        if len(oven) < N and queue:
            oven.append(queue.pop(0))

        # 오븐에 맨 앞에꺼를 꺼낸다
        idx, cheese = oven.pop(0)

        # 치즈가 0이되면 제거해야하니 continue로 넘어간다.
        if cheese // 2 == 0:
            continue
        # 치즈가 남아있으면 인덱스랑 치즈의 반을 없앤것을 다시 넣어준다.
        else:
            oven.append((idx, cheese//2))

    print("#{} {}".format(tc+1, oven.pop(0)[0]))