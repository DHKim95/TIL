T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = 0 # 최대값
    min_value = 1000000 # 최소값

    for num in arr:
        if num > max_value: # 최대값 찾기
            max_value = num
        if num < min_value: # 최소값 찾기
            min_value = num

    # 최대에서 최소를 빼준다.
    print("#{} {}".format(tc+1, max_value-min_value))