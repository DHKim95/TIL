T = int(input())

# 테스트 케이스
for tc in range(T):
    # N은 컨테이너수, M은 트럭 수
    N, M = map(int, input().split())
    visited = [0] * M # 최대 화물을 넣기 위한 리스트

    weight = list(map(int, input().split())) # 화물 무게
    # 트럭이 운반할 수 있는 적재 용량
    truck = list(map(int, input().split()))

    # 내림차순 정렬
    sort_weight = sorted(weight, reverse=True)
    sort_truck = sorted(truck, reverse=True)

    for i in range(N):
        for j in range(M):
            # 화물공간이 비어있고 운반할 수 있는 최대 화물을 넣어준다.
            if sort_weight[i] <= sort_truck[j] and visited[j] == 0:
                visited[j] = sort_weight[i]
                break

    print("#{} {}".format(tc+1, sum(visited)))
