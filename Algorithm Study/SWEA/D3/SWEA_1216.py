for _ in range(10):
    tc = int(input()) # 테스트 케이스
    cnt = 0 # 가장 긴 회문 찾는 변수

    # 입력 받기
    graph = []
    for _ in range(100):
        graph.append(input())

    # 가로줄 확인
    for word in graph:
        # 처음 길이
        for i in range(len(word)):
            # 끝에서 부터 접근
            for j in range(len(word), cnt, -1):
                # 현재 최대 길이보다 작으면 break 볼필요가 없음
                if j < cnt:
                    break
                # 회문이 맞다면 다시 길이 체크를 해주고 최대값 갱신
                if word[i:j] == word[i:j][::-1]:
                    if len(word[i:j]) > cnt:
                        cnt = len(word[i:j])

    # 세로줄 만들어주기
    lst = []
    for i in range(100):
        sub_lst = []
        for j in range(100):
            sub_lst.append(graph[j][i])
        lst.append(''.join(sub_lst))

    # 세로줄 확인
    for word in lst:
        # 처음 길이
        for i in range(len(word)):
            # 끝에서 부터 접근
            for j in range(len(word), cnt, -1):
                # 현재 최대 길이보다 작으면 break 볼필요가 없음
                if j < cnt:
                    break
                # 회문이 맞다면 다시 길이 체크를 해주고 최대값 갱신
                if word[i:j] == word[i:j][::-1]:
                    if len(word[i:j]) > cnt:
                        cnt = len(word[i:j])

    print("#{} {}".format(tc, cnt))