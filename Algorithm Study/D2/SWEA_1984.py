T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    # 정렬하기
    sort_arr = sorted(arr)
    # 최대 최소 제외하고 반올림하여 정수로 만들어주기
    answer = int(round(sum(sort_arr[1:9]) / 8, 0))
    print("#{} {}".format(tc+1, answer))