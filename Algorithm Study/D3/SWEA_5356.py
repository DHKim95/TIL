# 처음에 길이가 다 똑같은 줄 알았는데 test_case 2부터 길이가 달라서 체크를 해주었다.
T = int(input()) # 테스트 케이스
for tc in range(T):
    # 입력 받기
    lst = [] # 전체 리스트
    len_check = []  # 길이 체크 리스트
    max_len = 0  # 최대길이
    answer = ""  # 정답입력

    # 입력을 받으면서 최대길이를 찾고 길이와 입력받은 것을 넣어준다.
    for i in range(5):
        sub_lst = list(input())
        lst.append(sub_lst)
        len_check.append(len(sub_lst))
        # 최대길이를 찾는다.
        if len(sub_lst) > max_len:
            max_len = len(sub_lst)

    # 최대로 길이가 큰 것을 기준으로 돌린다.
    for i in range(max_len):
        for j in range(5):
            # 행을 돌면서 길이를 전부 출력한 것들은 넘어가고 남아있는 것만 출력하게 설정
            if len_check[j] > i:
                answer += lst[j][i]

    print("#{} {}".format(tc+1, answer))