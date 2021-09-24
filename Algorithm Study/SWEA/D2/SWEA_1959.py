T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))
    answer = []

    # A가 B보다 많을 경우
    if N > M:
        # 인덱스 갯수만큼 해주기 위하여 맞춰주기
        for i in range(N-M+1):
            hap = 0
            for j in range(M):
                hap += (A_arr[i+j] * B_arr[j])
            answer.append(hap)

    # B가 A보다 많을 경우
    else:
        # 인덱스 갯수만큼 해주기 위하여 맞춰주기
        for i in range(M-N+1):
            hap = 0
            for j in range(N):
                hap += (A_arr[j] * B_arr[i+j])
            answer.append(hap)

    print("#{} {}".format(tc+1, max(answer)))