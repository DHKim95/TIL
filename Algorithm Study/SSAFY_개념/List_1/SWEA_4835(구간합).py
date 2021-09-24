# 정렬로 풀면 안됨
T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) # N은 정수의 개수, M은 구간의 개수
    arr = list(map(int, input().split()))
    lst = []

    for i in range(N-M+1): # 인덱스 지정
        cnt = 0
        for j in arr[i:i+M]: # M 개수만큼 더해서 리스트에 추가하기
            cnt += j
        lst.append(cnt)

    max_value = lst[0] # 최대값 찾기
    min_value = lst[0] # 최소값 찾기
    for num in lst:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    print("#{} {}".format(tc+1, max_value - min_value))