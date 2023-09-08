T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    max_value = arr[-1]
    # 역순계산
    for i in range(len(arr)-2, -1, -1):
        # 적으면 이익이 난 것
        if arr[i] < max_value:
            answer += (max_value - arr[i])
        # 값이 크면 최대값 갱신
        elif arr[i] > max_value:
            max_value = arr[i]

    print(answer)