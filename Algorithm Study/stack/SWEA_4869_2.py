# DP해결문제
T = int(input())
for tc in range(T):
    N = int(input()) // 10  # 10의 배수이므로 10으로 나누어서 인덱스로 만들어주기
    arr = [1, 3]
    for i in range(2, N+1):
        # 규칙을 찾아 더해서 추가해주기
        arr.append(arr[i-1] + arr[i-2] * 2)

    # 0번째 부터 시작하여 인덱스-1을 해서 리스트를 뽑아낸다.
    print("#{}".format(tc + 1), arr[N-1])