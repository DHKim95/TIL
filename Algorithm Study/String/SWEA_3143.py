T = int(input())
for tc in range(T):
    a, b = map(str, input().split())
    idx = 0 # 인덱스
    cnt = 0 # 입력 횟수

    while True:
        # 인덱스가 마지막까지 도달하면 종료
        if idx == len(a):
            break

        # 해당 인덱스에서 b크기만큼 슬라이싱 했을 때 b랑 같으면 횟수 1로 추가하고 길이만큼 인덱스 넘어간다.
        if a[idx:idx+len(b)] == b:
            idx += len(b)
            cnt += 1
        # 아닐경우 입력횟수 +1, 인덱스 +1
        else:
            idx += 1
            cnt += 1

    print("#{} {}".format(tc+1, cnt))