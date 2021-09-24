T = int(input())
for tc in range(T):
    # 한번씩만 검사하면 되기 때문에 set로 만든 후 리스트로 변환
    str1 = list(set(input()))
    str2 = input()
    cnt_lst = [] # 카운트 리스트


    for word in str1:
        cnt = 0 # 같은 문자 카운트
        for word2 in str2:
            if word == word2:
                cnt += 1
        cnt_lst.append(cnt) # 카운트해서 리스트에 추가

    max_value = 0 # 최대값 찾기
    for num in cnt_lst:
        if max_value < num:
            max_value = num

    print("#{} {}".format(tc+1, max_value))