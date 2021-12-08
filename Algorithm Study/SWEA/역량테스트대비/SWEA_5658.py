T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    arr = input()
    answer = []

    arr += arr[:N // 4 - 1]  # 회전만큼 뒤에 추가

    # 모든 경우의 수 추가
    for i in range(N):
        answer.append(arr[i:i + N // 4])

    # 중복제거 후 정렬해서 K번째 숫자 출력
    answer = list(set(answer))
    answer.sort(reverse=True)
    print("#{} {}".format(tc + 1, int(answer[K - 1], 16)))