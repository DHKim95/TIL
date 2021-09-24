T = int(input()) # 테스트 케이스
for tc in range(T):
    N = int(input()) # 학생들 수
    room = [0 for _ in range(201)] # 복도 번호
    for i in range(N):
        a, b = map(int, input().split()) # 현재방, 돌아갈 방
        # 현재방이 숫자가 더 작을 때
        if a < b:
            # 홀수일 경우 그냥 나누면 한칸 작은 복도가 선택되므로 1번 2번방을 1번복도로 설정하려면 +1을 한 후에 나누기를 해준다.
            for j in range((a+1)//2, (b+1)//2+1):
                room[j] += 1
        # 현재방이 숫자가 더 클 때
        else:
            for j in range((b+1)//2, (a+1)//2+1):
                room[j] += 1

    max_value = 0 # 복도 지나가는 최대값
    # 최대값 찾기
    for k in room:
        if max_value < k:
            max_value = k

    print("#{} {}".format(tc+1, max_value))