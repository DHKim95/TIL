# 많이 틀림..

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    # 정렬......
    A_arr.sort()
    cnt = 0 # 갯수

    # B 리스트 탐색
    for i in range(M):
        target = B_arr[i]
        start, end = 0, N-1
        check = 0

        while start <= end:
            mid = (start + end) // 2
            # 타겟과 일치하면 +1 추가
            if target == A_arr[mid]:
                cnt += 1
                break

            # 타겟보다 크면 타겟 왼쪽 범위로 이동
            elif A_arr[mid] > target:
                end = mid - 1
                # 같은 방향으로 계속 가면 안된다고 해서 추가함...
                if check == 1:
                    break
                check = 1

            # 타겟보다 작으면 타겟 오른쪽 범위로 이동
            else:
                start = mid + 1
                # 마찬가지
                if check == 2:
                    break
                check = 2

    print("#{} {}".format(tc+1, cnt))
