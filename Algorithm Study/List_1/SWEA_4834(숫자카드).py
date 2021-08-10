T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))
    sort_lst = [0 for _ in range(10)] # 0으로 10칸 만들엊기

    # 개수 카운트
    for num in arr:
        sort_lst[num] += 1

    max_value = 0 # 가장 많은 수의 개수
    max_index = 0 # 가장 많은 수의 수
    for i in range(len(sort_lst)):
        if sort_lst[i] >= max_value:
            max_value = sort_lst[i] # 계속 비교하여 가장 많은 수를 찾는다.
            max_index = i # 큰값을 찾기 위해 인덱스도 같이 찾는다.

    print("#{} {} {}".format(tc+1, max_index, max_value))
