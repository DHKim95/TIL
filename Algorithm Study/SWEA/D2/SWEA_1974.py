T = int(input())
for tc in range(T):
    graph = [list(map(int, input().split())) for _ in range(9)]
    number_check = True

    # 가로 확인
    for i in range(9):
        sub_lst = []
        for j in range(9):
            if graph[i][j] in sub_lst:
                number_check = False # 같은게 또 있으면 False로 체크해준다.
                break
            sub_lst.append(graph[i][j])

    # 세로 확인
    for i in range(9):
        sub_lst = []
        for j in range(9):
            if graph[j][i] in sub_lst:
                number_check = False # 같은게 또 있으면 False로 체크해준다.
                break
            sub_lst.append(graph[j][i])

    # 네모칸 확인
    # 마스크형태로 0, 3, 6번째 인덱스에서 2칸씩만 확인해주면 된다.
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_lst = []
            for row in range(3):
                for col in range(3):
                    if graph[i+row][j+col] in sub_lst:
                        number_check = False # 같은게 또 있으면 False로 체크해준다.
                    sub_lst.append(graph[i+row][j+col])

    if number_check == True: # True이면 중복이 없다는 것이다.
        print("#{} 1".format(tc+1))
    else: # False면 중복이 있기에 0을 출력
        print("#{} 0".format(tc+1))
