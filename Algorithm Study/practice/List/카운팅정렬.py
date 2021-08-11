arr = [5, 3, 2, 9, 8, 6, 4, 1, 5, 5, 5] # 원래 배열
cnt_lst = [0 for _ in range(10)] # 카운트 배열
sort_arr = [0 for _ in range(len(arr))] # 정렬될 배열

# 배열에 있는 숫자 카운트 해주기
for i in range(len(arr)):
    cnt_lst[arr[i]] += 1

# 누적 카운트 해주기
for i in range(1, len(cnt_lst)):
    cnt_lst[i] += cnt_lst[i-1]

# 원래 배열에 나온 값을 카운팅 배열에 넣어 인덱스를 찾아 정렬될 배열 인덱스에 값을 넣어준다.
for i in range(len(sort_arr)-1, -1, -1):
    sort_arr[cnt_lst[arr[i]]-1] = arr[i]
    cnt_lst[arr[i]] -= 1

print(sort_arr)