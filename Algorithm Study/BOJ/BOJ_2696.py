# 다음번에는 heapq로 풀어보기

T = int(input())

for tc in range(T):
    M = int(input()) # 수열 크기

    lst = []
    # 리스트에 넣어주기, append가 아니라 요소별 삽입
    for i in range(M // 10 + 1):
        lst.extend(list(map(int, input().split())))

    # 중앙값 출력
    print(M // 2 + 1)
    print(lst[0], end=' ')
    # 1개가 아닐 경우에
    if M != 1:
        cnt = 1
        for j in range(2, M, 2):
            print(sorted(lst[:j+1])[(j+1)//2], end=' ')
            cnt += 1
            # 10개 도달할 경우 한칸 밑으로
            if cnt == 10:
                print()
                cnt = 0
        else:
            print()
