T = int(input()) # 테스트 케이스
for tc in range(T):
    N = int(input()) # N개의 자연수
    arr = list(map(int, input().split()))
    cnt = 0 # 이익

    min_value = arr[-1] # 시작부분
    for i in range(len(arr)-2, -1, -1): # 마지막 한칸 전 부터 시작
        if arr[i] > min_value: # 뒤에 가격이 앞에 가격보다 더 낮으면 가격 새로 갱신
            min_value = arr[i]

        if arr[i] < min_value: # 뒤에 가격이 앞에 가격보다 크면 이익이 갱신된 것이므로 계산해준다.
            cnt += (min_value - arr[i])

    print("#{} {}".format(tc+1, cnt))
