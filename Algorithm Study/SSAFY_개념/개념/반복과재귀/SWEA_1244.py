def DFS(change_cnt, idx, number):
    number = int(number)
    # print("위치",idx, number)
    # 교환횟수가 도달하면 정답리스트 추가후 탈출
    if change_cnt == idx:
        # print(idx, number)
        answer.append(number)
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # 두개 교환
            arr[i], arr[j] = arr[j], arr[i]

            lst = ''.join(arr)
            DFS(change_cnt, idx+1, lst)
            # 원상태로 되돌리기
            arr[i], arr[j] = arr[j], arr[i]

# 첫번째 메모리초과..
T = int(input())

for tc in range(T):
    number, change_cnt = map(int, input().split())
    arr = list(str(number))
    answer = []

    # 두번째 시도
    # 교환 횟수를 줄여주기
    if change_cnt > 5:
        # 짝수
        if change_cnt % 2 == 0:
            change_cnt //= 2
        # 홀수
        else:
            change_cnt = change_cnt // 2 + 1
    ##

    DFS(change_cnt, 0, number)
    answer = list(set(answer))

    print("#{} {}".format(tc+1, max(answer)))