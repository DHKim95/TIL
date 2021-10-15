T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # 정렬을 한다.(선택정렬)
    for i in range(0, len(arr) - 1):
        min_value = i
        # 최소를 찾아 교환
        for j in range(i + 1, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]

    left = 0 # 왼쪽 위치
    right = len(arr)-1 # 오른쪽 위치
    answer = []
    cnt = 0
    while cnt < 5: # 왼쪽이 오른쪽보다 커지면 반복문 종료
        if left >= right:
            break
        answer.append(arr[right])
        answer.append(arr[left])
        left += 1
        right -= 1
        cnt += 1

    print("#{}".format(tc+1), end=' ')
    print(*answer, end=' ')
    print()