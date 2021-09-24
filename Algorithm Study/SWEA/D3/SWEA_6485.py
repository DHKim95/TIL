T = int(input()) # 테스트 케이스
for tc in range(T):
    N = int(input())
    # 정류장 5000개 만들어주기
    bus = [0] * 5000
    # 입력 받아서 정류장 지나가는 버스를 표시해주기
    for _ in range(N):
        a, b = map(int, input().split())
        # 카운팅
        for i in range(a, b+1):
            bus[i-1] += 1

    print("#{}".format(tc + 1), end=' ')
    # 궁금한 노선 인덱스로 검색해서 출력
    P = int(input())
    for _ in range(P):
        c = int(input())
        print(bus[c-1], end=' ')
    print()